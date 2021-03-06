import arcpy

arcpy.env.overwriteOutput = True
folder = arcpy.GetParameterAsText(0)
datapoints = arcpy.GetParameterAsText(1)
pieceofplace = arcpy.GetParameterAsText(2)
nameDataBase = arcpy.GetParameterAsText(3)

arcpy.CreateFileGDB_management(folder, nameDataBase + '.gdb')
arcpy.AddMessage('Created new File GDB: {}.gdb'.format(nameDataBase))
arcpy.env.workspace = folder + "\\" + nameDataBase + '.gdb'
amenities = ['school', 'hospital', 'place_of_worship']

place = arcpy.GetParameterAsText(4)
arcpy.MakeFeatureLayer_management(pieceofplace, 'zoneclip', '"NAME" = ' + "'"+place + "'")
arcpy.Clip_analysis(datapoints, 'zoneclip', 'clipshp')
arcpy.AddMessage('Objects are cut for a given area ({})'.format(place))

for i in amenities:
    arcpy.MakeFeatureLayer_management('clipshp', 'clip', '"amenity" = ' + "'" + i + "'")
    arcpy.CopyFeatures_management('clip', 'zones_' + i)
    arcpy.AddField_management('zones_' + i, 'source', 'TEXT')
    arcpy.AddField_management('zones_' + i, 'GID', 'DOUBLE')
    with arcpy.da.UpdateCursor('zones_' + i, ['source', 'GID', 'id']) as cursor:
        for row in cursor:
            row[1] = row[2]
            row[0] = "OpenStreetMap"
            cursor.updateRow(row)
    arcpy.AddMessage('Created file for location '+i)
arcpy.Delete_management('clipshp')