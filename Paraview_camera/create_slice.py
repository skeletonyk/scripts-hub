#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
slice1 = FindSource('Slice1')

# set active source
SetActiveSource(slice1)

# find source
calculator2 = FindSource('Calculator2')

# set active source
SetActiveSource(calculator2)

# create a new 'Slice'
slice2 = Slice(Input=calculator2)
slice2.SliceType = 'Plane'
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [22.778738021850586, 21.556150436401367, 19.75444221496582]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice2.SliceType)

# find source
calculator1 = FindSource('Calculator1')

# find source
cal_w_s = FindSource('cal_w_s')

# find source
tseries_bodypvd = FindSource('tseries_body.pvd')

# Properties modified on slice2.SliceType
slice2.SliceType.Origin = [20.4, 20.0, 20.0]

# Properties modified on slice2.SliceType
slice2.SliceType.Origin = [20.4, 20.0, 20.0]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1058, 820]

# get color transfer function/color map for 'w_x'
w_xLUT = GetColorTransferFunction('w_x')

# show data in view
slice2Display = Show(slice2, renderView1)
# trace defaults for the display properties.
slice2Display.Representation = 'Surface'
slice2Display.AmbientColor = [0.0, 0.0, 0.4980392156862745]
slice2Display.ColorArrayName = ['POINTS', 'w_x']
slice2Display.LookupTable = w_xLUT
slice2Display.OSPRayScaleArray = 'w_x'
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.SelectOrientationVectors = 'None'
slice2Display.ScaleFactor = 0.11582412719726563
slice2Display.SelectScaleArray = 'w_x'
slice2Display.GlyphType = 'Arrow'
slice2Display.GlyphTableIndexArray = 'w_x'
slice2Display.DataAxesGrid = 'GridAxesRepresentation'
slice2Display.PolarAxes = 'PolarAxesRepresentation'
slice2Display.GaussianRadius = 0.05791206359863282
slice2Display.SetScaleArray = ['POINTS', 'w_x']
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityArray = ['POINTS', 'w_x']
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice2Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.4980392156862745]
slice2Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice2Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
slice2Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
slice2Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
slice2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(calculator2, renderView1)

# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on w_xLUT
w_xLUT.RGBPoints = [-80.51363201545612, 0.231373, 0.298039, 0.752941, -3.0487865249545507, 1.0, 1.0, 1.0, 74.41605896554702, 0.705882, 0.0156863, 0.14902]

# Properties modified on w_xLUT
w_xLUT.RGBPoints = [-80.51363201545612, 0.231373, 0.298039, 0.752941, -3.0487865249545507, 1.0, 1.0, 1.0, -1.2043825387954712, 1.0, 0.984313725490196, 0.9647058823529412, 74.41605896554702, 0.705882, 0.0156863, 0.14902]

# Properties modified on w_xLUT
w_xLUT.RGBPoints = [-80.51363201545612, 0.231373, 0.298039, 0.752941, -3.0487865249545507, 1.0, 1.0, 1.0, 74.41605896554702, 0.705882, 0.0156863, 0.14902]

# Rescale transfer function
w_xLUT.RescaleTransferFunction(-10.0, 10.0)

# get opacity transfer function/opacity map for 'w_x'
w_xPWF = GetOpacityTransferFunction('w_x')

# Rescale transfer function
w_xPWF.RescaleTransferFunction(-10.0, 10.0)

# Rescale transfer function
w_xLUT.RescaleTransferFunction(-40.0, 40.0)

# Rescale transfer function
w_xPWF.RescaleTransferFunction(-40.0, 40.0)

# Rescale transfer function
w_xLUT.RescaleTransferFunction(-30.0, 30.0)

# Rescale transfer function
w_xPWF.RescaleTransferFunction(-30.0, 30.0)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [18.520729274557915, 20.604234849084865, 19.99001775190264]
renderView1.CameraFocalPoint = [20.499629438361733, 20.07617568969732, 20.011828422546426]
renderView1.CameraViewUp = [0.2579780037709997, 0.9659417526020896, -0.02009676964921968]
renderView1.CameraParallelScale = 0.776161334344501

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).