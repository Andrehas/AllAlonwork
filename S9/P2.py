import arcpy

data = arcpy.GetParameterAsText(0)
place = arcpy.GetParameterAsText(1)
clipoint = arcpy.GetParameterAsText(2)

#Local variables:
IDwWouter = r"E:\\KNU\\course2semestr\\codinginGIS\\alonwork\\S9\\Test.gdb\\IDWout2"
reclassou2 = r"E:\\KNU\\course2semestr\\codinginGIS\\alonwork\\S9\\Test.gdb\\reclassou2"
rasterout2 = r"E:\\KNU\\course2semestr\\codinginGIS\\alonwork\\S9\\Test.gdb\\rasterout2"

arcpy.gp.Idw_sa(data, "RASTERVALU", IDwWouter, "1850,46466995651", "2", "VARIABLE 12", "")

arcpy.gp.Reclassify_sa(IDwWouter, "VALUE", "27715,960938 46615,086060 1;46615,086060 64536,670227 2;64536,670227 82132,407410 3;82132,407410 111132,789063 4", reclassou2, "DATA")

arcpy.RasterToPolygon_conversion(reclassou2, rasterout2, "SIMPLIFY", "VALUE")

arcpy.Clip_analysis(rasterout2, place, clipoint, "")
arcpy.env.overwriteOutput = True
