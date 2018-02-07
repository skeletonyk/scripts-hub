#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
tseries_flowpvd = FindSource('tseries_flow.pvd')

# create a new 'Merge Blocks'
mergeBlocks1 = MergeBlocks(Input=tseries_flowpvd)

# find source
tseries_bodypvd = FindSource('tseries_body.pvd')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1964, 1086]

# show data in view
mergeBlocks1Display = Show(mergeBlocks1, renderView1)
# trace defaults for the display properties.
mergeBlocks1Display.Representation = 'Surface'
mergeBlocks1Display.AmbientColor = [0.0, 0.0, 0.4980392156862745]
mergeBlocks1Display.ColorArrayName = [None, '']
mergeBlocks1Display.OSPRayScaleArray = 'celldata:01:01'
mergeBlocks1Display.OSPRayScaleFunction = 'PiecewiseFunction'
mergeBlocks1Display.SelectOrientationVectors = 'None'
mergeBlocks1Display.ScaleFactor = 0.46042766571044924
mergeBlocks1Display.SelectScaleArray = 'None'
mergeBlocks1Display.GlyphType = 'Arrow'
mergeBlocks1Display.GlyphTableIndexArray = 'None'
mergeBlocks1Display.DataAxesGrid = 'GridAxesRepresentation'
mergeBlocks1Display.PolarAxes = 'PolarAxesRepresentation'
mergeBlocks1Display.ScalarOpacityUnitDistance = 0.048877003171014344
mergeBlocks1Display.GaussianRadius = 0.23021383285522462
mergeBlocks1Display.SetScaleArray = [None, '']
mergeBlocks1Display.ScaleTransferFunction = 'PiecewiseFunction'
mergeBlocks1Display.OpacityArray = [None, '']
mergeBlocks1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
mergeBlocks1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
mergeBlocks1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
mergeBlocks1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
mergeBlocks1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.4980392156862745]
mergeBlocks1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
mergeBlocks1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
mergeBlocks1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
mergeBlocks1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
mergeBlocks1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
mergeBlocks1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
mergeBlocks1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(tseries_flowpvd, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=mergeBlocks1)

# Properties modified on cellDatatoPointData1
cellDatatoPointData1.PassCellData = 1

# show data in view
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1)
# trace defaults for the display properties.
cellDatatoPointData1Display.Representation = 'Surface'
cellDatatoPointData1Display.AmbientColor = [0.0, 0.0, 0.4980392156862745]
cellDatatoPointData1Display.ColorArrayName = [None, '']
cellDatatoPointData1Display.OSPRayScaleArray = 'celldata:01:01'
cellDatatoPointData1Display.OSPRayScaleFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.SelectOrientationVectors = 'None'
cellDatatoPointData1Display.ScaleFactor = 0.46042766571044924
cellDatatoPointData1Display.SelectScaleArray = 'None'
cellDatatoPointData1Display.GlyphType = 'Arrow'
cellDatatoPointData1Display.GlyphTableIndexArray = 'None'
cellDatatoPointData1Display.DataAxesGrid = 'GridAxesRepresentation'
cellDatatoPointData1Display.PolarAxes = 'PolarAxesRepresentation'
cellDatatoPointData1Display.ScalarOpacityUnitDistance = 0.048877003171014344
cellDatatoPointData1Display.GaussianRadius = 0.23021383285522462
cellDatatoPointData1Display.SetScaleArray = ['POINTS', 'celldata:01:01']
cellDatatoPointData1Display.ScaleTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.OpacityArray = ['POINTS', 'celldata:01:01']
cellDatatoPointData1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
cellDatatoPointData1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.4980392156862745]
cellDatatoPointData1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
cellDatatoPointData1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(mergeBlocks1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(Input=cellDatatoPointData1)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.Function = 'sqrt((edgedata:01:01)^2 + (edgedata:01:02)^2 + (edgedata:01:03)^2)'

# get color transfer function/color map for 'Result'
resultLUT = GetColorTransferFunction('Result')

# get opacity transfer function/opacity map for 'Result'
resultPWF = GetOpacityTransferFunction('Result')

# show data in view
calculator1Display = Show(calculator1, renderView1)
# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.AmbientColor = [0.0, 0.0, 0.4980392156862745]
calculator1Display.ColorArrayName = ['POINTS', 'Result']
calculator1Display.LookupTable = resultLUT
calculator1Display.OSPRayScaleArray = 'Result'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'None'
calculator1Display.ScaleFactor = 0.46042766571044924
calculator1Display.SelectScaleArray = 'Result'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'Result'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = resultPWF
calculator1Display.ScalarOpacityUnitDistance = 0.048877003171014344
calculator1Display.GaussianRadius = 0.23021383285522462
calculator1Display.SetScaleArray = ['POINTS', 'Result']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'Result']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.4980392156862745]
calculator1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(cellDatatoPointData1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on calculator1
calculator1.ResultArrayName = 'w_l2'

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on calculator1Display
calculator1Display.SelectScaleArray = 'None'

# Properties modified on calculator1Display
calculator1Display.GlyphTableIndexArray = 'None'

# Properties modified on calculator1Display
calculator1Display.SetScaleArray = ['POINTS', 'celldata:01:01']

# Properties modified on calculator1Display
calculator1Display.OpacityArray = ['POINTS', 'celldata:01:01']

# Properties modified on calculator1Display
calculator1Display.OSPRayScaleArray = 'celldata:01:01'

# set scalar coloring
ColorBy(calculator1Display, ('POINTS', 'edgedata:01:01'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(resultLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
calculator1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'edgedata0101'
edgedata0101LUT = GetColorTransferFunction('edgedata0101')

# create a new 'Contour'
contour1 = Contour(Input=calculator1)
contour1.ContourBy = ['POINTS', 'w_l2']
contour1.Isosurfaces = [19.62546780932802]
contour1.PointMergeMethod = 'Uniform Binning'

# Properties modified on contour1
contour1.Isosurfaces = [0.0, 9.812725, 19.62545, 29.438175, 39.2509]

# show data in view
contour1Display = Show(contour1, renderView1)
# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.AmbientColor = [0.0, 0.0, 0.4980392156862745]
contour1Display.ColorArrayName = ['POINTS', 'edgedata:01:01']
contour1Display.LookupTable = edgedata0101LUT
contour1Display.OSPRayScaleArray = 'Normals'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 0.11232528686523438
contour1Display.SelectScaleArray = 'None'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'None'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'
contour1Display.GaussianRadius = 0.05616264343261719
contour1Display.SetScaleArray = ['POINTS', 'celldata:01:01']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'celldata:01:01']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
contour1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
contour1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
contour1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
contour1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.4980392156862745]
contour1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
contour1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
contour1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
contour1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
contour1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
contour1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
contour1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on contour1
contour1.Isosurfaces = [0.0, 2.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on contour1
contour1.ComputeNormals = 0

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on contour1Display
contour1Display.OSPRayScaleArray = 'celldata:01:01'

# Properties modified on contour1
contour1.GenerateTriangles = 0

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on contour1
contour1.Isosurfaces = [2.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on contour1
contour1.Isosurfaces = [1.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on contour1Display
contour1Display.Opacity = 0.3

# Properties modified on contour1Display
contour1Display.Opacity = 0.4

# Properties modified on contour1Display
contour1Display.Opacity = 0.5

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [21.646601676940918, 20.31972312927246, 27.335823624378847]
renderView1.CameraFocalPoint = [21.646601676940918, 20.31972312927246, 20.00621223449707]
renderView1.CameraViewUp = [-0.3420201433256687, 0.9396926207859084, 0.0]
renderView1.CameraParallelScale = 1.8970430209017617

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).