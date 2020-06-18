import arcpy
import os


def get_mean(feature_class):
    sum = 0
    cnt = 0
    with arcpy.da.SearchCursor(feature_class, ('TEMPERATUR',)) as cur:
        for row in cur:
            if row[0] != -9999:
                sum += row[0]
                cnt += 1
    return sum/cnt


input_city_layer = arcpy.GetParameterAsText(0)
input_raster = arcpy.GetParameterAsText(1)
input_boundary = arcpy.GetParameterAsText(2)
output_folder = arcpy.GetParameterAsText(3)

arcpy.env.overwriteOutput = True
arcpy.env.workspace = output_folder


arcpy.MakeFeatureLayer_management(input_city_layer, 'city')
arcpy.SelectLayerByAttribute_management('city', 'NEW_SELECTION', 'POPCLASS >=3')
arcpy.FeatureClassToFeatureClass_conversion ('city', output_folder, 'us_cities_level_3.shp')
out_city_lvl3 = os.path.join(output_folder, 'us_cities_level_3.shp')
arcpy.AddField_management(out_city_lvl3, 'TEMPERATUR', 'DOUBLE')
arcpy.AddField_management(out_city_lvl3, 'EXCESS','DOUBLE')

out_proj_raster = os.path.join(output_folder, 'us.tmax_nohads_ll_20140525_float_NAD.tif')
arcpy.ProjectRaster_management(input_raster, out_proj_raster, input_city_layer,
                               '#', '#', 'WGS_1984_(ITRF00)_To_NAD_1983')

out_extracted_raster = os.path.join(output_folder,
                                    'us.tmax_nohads_ll_20140525_float_NAD_extract_by_mask.tif')
arcpy.CheckOutExtension("Spatial")
arcpy.gp.ExtractByMask_sa(out_proj_raster, input_boundary, out_extracted_raster)
arcpy.CheckInExtension("Spatial")


with arcpy.da.UpdateCursor(out_city_lvl3, ('SHAPE@XY', 'TEMPERATUR')) as cursor:
    for row in cursor:
        coord = " ".join([str(row[0][0]),str(row[0][1])])
        cell_val = arcpy.GetCellValue_management(out_extracted_raster, coord)
        if cell_val.getOutput(0) == 'NoData':
            row[1] = -9999
        else:
            row[1] = cell_val.getOutput(0)
        cursor.updateRow(row)

mean_temp = get_mean(os.path.join(output_folder, 'us_cities_level_3.shp'))


with arcpy.da.UpdateCursor(out_city_lvl3, ('TEMPERATUR','EXCESS')) as cursor:
    for row in cursor:
        if row[0] == -9999:
            row[1] = -9999
        else:
            row[1] = row[0] - mean_temp
        cursor.updateRow(row)
