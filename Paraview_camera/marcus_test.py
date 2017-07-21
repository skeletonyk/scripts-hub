
### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1872, 947]

# get camera animation track for the view
cameraAnimationCue1 = GetCameraTrack(view=renderView1)

# create keyframes for this animation track

# create a key frame
# ====================================================================
keyFrame5000 = CameraKeyFrame()
keyFrame5000.KeyTime = 0.0
keyFrame5000.KeyValues = [0.0]
keyFrame5000.Position = [24.9999, 11.34, 65.0]
keyFrame5000.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5000.ViewUp = [0.4999, -0.866, 0.0]
keyFrame5000.ViewAngle = 30.0
keyFrame5000.ParallelScale = 0.97681
keyFrame5000.PositionPathPoints = [24.9999, 11.34, 65.0]
keyFrame5000.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5000.PositionMode = 'Path'
keyFrame5000.FocalPointMode = 'Path'
keyFrame5000.ClosedFocalPath = 0
keyFrame5000.ClosedPositionPath = 0

# ====================================================================
keyFrame5001 = CameraKeyFrame()
keyFrame5001.KeyTime = 0.0025
keyFrame5001.KeyValues = [0.0]
keyFrame5001.Position = [25.08989992998137, 11.34, 64.99991000004766]
keyFrame5001.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5001.ViewUp = [0.4998990002014599, -0.866, -0.000999798779647768]
keyFrame5001.ViewAngle = 30.0
keyFrame5001.ParallelScale = 0.97681
keyFrame5001.PositionPathPoints = [25.08989992998137, 11.34, 64.99991000004766]
keyFrame5001.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5001.PositionMode = 'Path'
keyFrame5001.FocalPointMode = 'Path'
keyFrame5001.ClosedFocalPath = 0
keyFrame5001.ClosedPositionPath = 0

# ====================================================================
keyFrame5002 = CameraKeyFrame()
keyFrame5002.KeyTime = 0.005
keyFrame5002.KeyValues = [0.0]
keyFrame5002.Position = [25.17989950548872, 11.34, 64.99964000053961]
keyFrame5002.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5002.ViewUp = [0.4998960008095479, -0.866, -0.0019995936359588225]
keyFrame5002.ViewAngle = 30.0
keyFrame5002.ParallelScale = 0.97681
keyFrame5002.PositionPathPoints = [25.17989950548872, 11.34, 64.99964000053961]
keyFrame5002.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5002.PositionMode = 'Path'
keyFrame5002.FocalPointMode = 'Path'
keyFrame5002.ClosedFocalPath = 0
keyFrame5002.ClosedPositionPath = 0

# ====================================================================
keyFrame5003 = CameraKeyFrame()
keyFrame5003.KeyTime = 0.0075
keyFrame5003.KeyValues = [0.0]
keyFrame5003.Position = [25.269898366609517, 11.34, 64.9991900025193]
keyFrame5003.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5003.ViewUp = [0.4998910018350169, -0.866, -0.002999380720447823]
keyFrame5003.ViewAngle = 30.0
keyFrame5003.ParallelScale = 0.97681
keyFrame5003.PositionPathPoints = [25.269898366609517, 11.34, 64.9991900025193]
keyFrame5003.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5003.PositionMode = 'Path'
keyFrame5003.FocalPointMode = 'Path'
keyFrame5003.ClosedFocalPath = 0
keyFrame5003.ClosedPositionPath = 0

# ====================================================================
keyFrame5004 = CameraKeyFrame()
keyFrame5004.KeyTime = 0.01
keyFrame5004.KeyValues = [0.0]
keyFrame5004.Position = [25.35989614661914, 11.34, 64.99856000780173]
keyFrame5004.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5004.ViewUp = [0.49988400330596444, -0.866, -0.003999155591701697]
keyFrame5004.ViewAngle = 30.0
keyFrame5004.ParallelScale = 0.97681
keyFrame5004.PositionPathPoints = [25.35989614661914, 11.34, 64.99856000780173]
keyFrame5004.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5004.PositionMode = 'Path'
keyFrame5004.FocalPointMode = 'Path'
keyFrame5004.ClosedFocalPath = 0
keyFrame5004.ClosedPositionPath = 0

# ====================================================================
keyFrame5005 = CameraKeyFrame()
keyFrame5005.KeyTime = 0.0125
keyFrame5005.KeyValues = [0.0]
keyFrame5005.Position = [25.449892486645044, 11.34, 64.9977500189454]
keyFrame5005.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5005.ViewUp = [0.49987500532502527, -0.866, -0.004998915873783566]
keyFrame5005.ViewAngle = 30.0
keyFrame5005.ParallelScale = 0.97681
keyFrame5005.PositionPathPoints = [25.449892486645044, 11.34, 64.9977500189454]
keyFrame5005.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5005.PositionMode = 'Path'
keyFrame5005.FocalPointMode = 'Path'
keyFrame5005.ClosedFocalPath = 0
keyFrame5005.ClosedPositionPath = 0

# ====================================================================
keyFrame5006 = CameraKeyFrame()
keyFrame5006.KeyTime = 0.015
keyFrame5006.KeyValues = [0.0]
keyFrame5006.Position = [25.539887026701766, 11.34, 64.99676003914605]
keyFrame5006.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5006.ViewUp = [0.49986400795839225, -0.866, -0.005998657098363074]
keyFrame5006.ViewAngle = 30.0
keyFrame5006.ParallelScale = 0.97681
keyFrame5006.PositionPathPoints = [25.539887026701766, 11.34, 64.99676003914605]
keyFrame5006.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5006.PositionMode = 'Path'
keyFrame5006.FocalPointMode = 'Path'
keyFrame5006.ClosedFocalPath = 0
keyFrame5006.ClosedPositionPath = 0

# ====================================================================
keyFrame5007 = CameraKeyFrame()
keyFrame5007.KeyTime = 0.0175
keyFrame5007.KeyValues = [0.0]
keyFrame5007.Position = [25.62987940681125, 11.34, 64.995590072364]
keyFrame5007.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5007.ViewUp = [0.4998510112466875, -0.866, -0.006998375054213215]
keyFrame5007.ViewAngle = 30.0
keyFrame5007.ParallelScale = 0.97681
keyFrame5007.PositionPathPoints = [25.62987940681125, 11.34, 64.995590072364]
keyFrame5007.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5007.PositionMode = 'Path'
keyFrame5007.FocalPointMode = 'Path'
keyFrame5007.ClosedFocalPath = 0
keyFrame5007.ClosedPositionPath = 0

# ====================================================================
keyFrame5008 = CameraKeyFrame()
keyFrame5008.KeyTime = 0.02
keyFrame5008.KeyValues = [0.0]
keyFrame5008.Position = [25.719869267004086, 11.34, 64.99424012328029]
keyFrame5008.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5008.ViewUp = [0.49983601523053345, -0.866, -0.007998065530106976]
keyFrame5008.ViewAngle = 30.0
keyFrame5008.ParallelScale = 0.97681
keyFrame5008.PositionPathPoints = [25.719869267004086, 11.34, 64.99424012328029]
keyFrame5008.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5008.PositionMode = 'Path'
keyFrame5008.FocalPointMode = 'Path'
keyFrame5008.ClosedFocalPath = 0
keyFrame5008.ClosedPositionPath = 0

# ====================================================================
keyFrame5009 = CameraKeyFrame()
keyFrame5009.KeyTime = 0.0225
keyFrame5009.KeyValues = [0.0]
keyFrame5009.Position = [25.80985624734039, 11.34, 64.99271019817606]
keyFrame5009.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5009.ViewUp = [0.49981901995055217, -0.866, -0.008997724314817353]
keyFrame5009.ViewAngle = 30.0
keyFrame5009.ParallelScale = 0.97681
keyFrame5009.PositionPathPoints = [25.80985624734039, 11.34, 64.99271019817606]
keyFrame5009.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5009.PositionMode = 'Path'
keyFrame5009.FocalPointMode = 'Path'
keyFrame5009.ClosedFocalPath = 0
keyFrame5009.ClosedPositionPath = 0

# ====================================================================
keyFrame5010 = CameraKeyFrame()
keyFrame5010.KeyTime = 0.025
keyFrame5010.KeyValues = [0.0]
keyFrame5010.Position = [25.899839987966978, 11.34, 64.99100030737043]
keyFrame5010.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5010.ViewUp = [0.499800025447366, -0.866, -0.00999734719711733]
keyFrame5010.ViewAngle = 30.0
keyFrame5010.ParallelScale = 0.97681
keyFrame5010.PositionPathPoints = [25.899839987966978, 11.34, 64.99100030737043]
keyFrame5010.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5010.PositionMode = 'Path'
keyFrame5010.FocalPointMode = 'Path'
keyFrame5010.ClosedFocalPath = 0
keyFrame5010.ClosedPositionPath = 0

# ====================================================================
keyFrame5011 = CameraKeyFrame()
keyFrame5011.KeyTime = 0.0275
keyFrame5011.KeyValues = [0.0]
keyFrame5011.Position = [25.98982012896351, 11.34, 64.9891104580409]
keyFrame5011.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5011.ViewUp = [0.4997790317615972, -0.866, -0.010996929965779903]
keyFrame5011.ViewAngle = 30.0
keyFrame5011.ParallelScale = 0.97681
keyFrame5011.PositionPathPoints = [25.98982012896351, 11.34, 64.9891104580409]
keyFrame5011.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5011.PositionMode = 'Path'
keyFrame5011.FocalPointMode = 'Path'
keyFrame5011.ClosedFocalPath = 0
keyFrame5011.ClosedPositionPath = 0

# ====================================================================
keyFrame5012 = CameraKeyFrame()
keyFrame5012.KeyTime = 0.03
keyFrame5012.KeyValues = [0.0]
keyFrame5012.Position = [26.07979631039882, 11.34, 64.9870406568597]
keyFrame5012.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5012.ViewUp = [0.499756038933868, -0.866, -0.01199646840957806]
keyFrame5012.ViewAngle = 30.0
keyFrame5012.ParallelScale = 0.97681
keyFrame5012.PositionPathPoints = [26.07979631039882, 11.34, 64.9870406568597]
keyFrame5012.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5012.PositionMode = 'Path'
keyFrame5012.FocalPointMode = 'Path'
keyFrame5012.ClosedFocalPath = 0
keyFrame5012.ClosedPositionPath = 0

# ====================================================================
keyFrame5013 = CameraKeyFrame()
keyFrame5013.KeyTime = 0.0325
keyFrame5013.KeyValues = [0.0]
keyFrame5013.Position = [26.169768172341744, 11.34, 64.98479091049904]
keyFrame5013.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5013.ViewUp = [0.4997310470048006, -0.866, -0.012995958317284796]
keyFrame5013.ViewAngle = 30.0
keyFrame5013.ParallelScale = 0.97681
keyFrame5013.PositionPathPoints = [26.169768172341744, 11.34, 64.98479091049904]
keyFrame5013.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5013.PositionMode = 'Path'
keyFrame5013.FocalPointMode = 'Path'
keyFrame5013.ClosedFocalPath = 0
keyFrame5013.ClosedPositionPath = 0

# ====================================================================
keyFrame5014 = CameraKeyFrame()
keyFrame5014.KeyTime = 0.035
keyFrame5014.KeyValues = [0.0]
keyFrame5014.Position = [26.259735354861117, 11.34, 64.98236122563111]
keyFrame5014.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5014.ViewUp = [0.4997040560150173, -0.866, -0.013995395477673096]
keyFrame5014.ViewAngle = 30.0
keyFrame5014.ParallelScale = 0.97681
keyFrame5014.PositionPathPoints = [26.259735354861117, 11.34, 64.98236122563111]
keyFrame5014.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5014.PositionMode = 'Path'
keyFrame5014.FocalPointMode = 'Path'
keyFrame5014.ClosedFocalPath = 0
keyFrame5014.ClosedPositionPath = 0

# ====================================================================
keyFrame5015 = CameraKeyFrame()
keyFrame5015.KeyTime = 0.0375
keyFrame5015.KeyValues = [0.0]
keyFrame5015.Position = [26.349697498025776, 11.34, 64.97975160892815]
keyFrame5015.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5015.ViewUp = [0.4996750660051403, -0.866, -0.014994775679515952]
keyFrame5015.ViewAngle = 30.0
keyFrame5015.ParallelScale = 0.97681
keyFrame5015.PositionPathPoints = [26.349697498025776, 11.34, 64.97975160892815]
keyFrame5015.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5015.PositionMode = 'Path'
keyFrame5015.FocalPointMode = 'Path'
keyFrame5015.ClosedFocalPath = 0
keyFrame5015.ClosedPositionPath = 0

# ====================================================================
keyFrame5016 = CameraKeyFrame()
keyFrame5016.KeyTime = 0.04
keyFrame5016.KeyValues = [0.0]
keyFrame5016.Position = [26.439654241904556, 11.34, 64.97696206706237]
keyFrame5016.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5016.ViewUp = [0.4996440771893387, -0.866, -0.015994095170387343]
keyFrame5016.ViewAngle = 30.0
keyFrame5016.ParallelScale = 0.97681
keyFrame5016.PositionPathPoints = [26.439654241904556, 11.34, 64.97696206706237]
keyFrame5016.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5016.PositionMode = 'Path'
keyFrame5016.FocalPointMode = 'Path'
keyFrame5016.ClosedFocalPath = 0
keyFrame5016.ClosedPositionPath = 0

# ====================================================================
keyFrame5017 = CameraKeyFrame()
keyFrame5017.KeyTime = 0.0425
keyFrame5017.KeyValues = [0.0]
keyFrame5017.Position = [26.529605226631354, 11.34, 64.97399260919684]
keyFrame5017.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5017.ViewUp = [0.4996110899627806, -0.866, -0.016993350676363803]
keyFrame5017.ViewAngle = 30.0
keyFrame5017.ParallelScale = 0.97681
keyFrame5017.PositionPathPoints = [26.529605226631354, 11.34, 64.97399260919684]
keyFrame5017.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5017.PositionMode = 'Path'
keyFrame5017.FocalPointMode = 'Path'
keyFrame5017.ClosedFocalPath = 0
keyFrame5017.ClosedPositionPath = 0

# ====================================================================
keyFrame5018 = CameraKeyFrame()
keyFrame5018.KeyTime = 0.045
keyFrame5018.KeyValues = [0.0]
keyFrame5018.Position = [26.619550092754594, 11.34, 64.97084326036499]
keyFrame5018.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5018.ViewUp = [0.4995761044527533, -0.866, -0.017992538215332372]
keyFrame5018.ViewAngle = 30.0
keyFrame5018.ParallelScale = 0.97681
keyFrame5018.PositionPathPoints = [26.619550092754594, 11.34, 64.97084326036499]
keyFrame5018.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5018.PositionMode = 'Path'
keyFrame5018.FocalPointMode = 'Path'
keyFrame5018.ClosedFocalPath = 0
keyFrame5018.ClosedPositionPath = 0

# ====================================================================
keyFrame5019 = CameraKeyFrame()
keyFrame5019.KeyTime = 0.0475
keyFrame5019.KeyValues = [0.0]
keyFrame5019.Position = [26.709488480552004, 11.34, 64.96751403523652]
keyFrame5019.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5019.ViewUp = [0.49953912078087065, -0.866, -0.018991653790181105]
keyFrame5019.ViewAngle = 30.0
keyFrame5019.ParallelScale = 0.97681
keyFrame5019.PositionPathPoints = [26.709488480552004, 11.34, 64.96751403523652]
keyFrame5019.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5019.PositionMode = 'Path'
keyFrame5019.FocalPointMode = 'Path'
keyFrame5019.ClosedFocalPath = 0
keyFrame5019.ClosedPositionPath = 0

# ====================================================================
keyFrame5020 = CameraKeyFrame()
keyFrame5020.KeyTime = 0.05
keyFrame5020.KeyValues = [0.0]
keyFrame5020.Position = [26.799420030228827, 11.34, 64.96400494570614]
keyFrame5020.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5020.ViewUp = [0.49950013906874635, -0.866, -0.019990693403798054]
keyFrame5020.ViewAngle = 30.0
keyFrame5020.ParallelScale = 0.97681
keyFrame5020.PositionPathPoints = [26.799420030228827, 11.34, 64.96400494570614]
keyFrame5020.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5020.PositionMode = 'Path'
keyFrame5020.FocalPointMode = 'Path'
keyFrame5020.ClosedFocalPath = 0
keyFrame5020.ClosedPositionPath = 0

# ====================================================================
keyFrame5021 = CameraKeyFrame()
keyFrame5021.KeyTime = 0.0525
keyFrame5021.KeyValues = [0.0]
keyFrame5021.Position = [26.88934438199031, 11.34, 64.96031600366854]
keyFrame5021.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5021.ViewUp = [0.4994591594379941, -0.866, -0.02098965305907128]
keyFrame5021.ViewAngle = 30.0
keyFrame5021.ParallelScale = 0.97681
keyFrame5021.PositionPathPoints = [26.88934438199031, 11.34, 64.96031600366854]
keyFrame5021.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5021.PositionMode = 'Path'
keyFrame5021.FocalPointMode = 'Path'
keyFrame5021.ClosedFocalPath = 0
keyFrame5021.ClosedPositionPath = 0

# ====================================================================
keyFrame5022 = CameraKeyFrame()
keyFrame5022.KeyTime = 0.055
keyFrame5022.KeyValues = [0.0]
keyFrame5022.Position = [26.979261176041696, 11.34, 64.9564472210184]
keyFrame5022.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5022.ViewUp = [0.49941618201022775, -0.866, -0.021988528758888827]
keyFrame5022.ViewAngle = 30.0
keyFrame5022.ParallelScale = 0.97681
keyFrame5022.PositionPathPoints = [26.979261176041696, 11.34, 64.9564472210184]
keyFrame5022.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5022.PositionMode = 'Path'
keyFrame5022.FocalPointMode = 'Path'
keyFrame5022.ClosedFocalPath = 0
keyFrame5022.ClosedPositionPath = 0

# ====================================================================
keyFrame5023 = CameraKeyFrame()
keyFrame5023.KeyTime = 0.0575
keyFrame5023.KeyValues = [0.0]
keyFrame5023.Position = [27.069170052588234, 11.34, 64.95239860965042]
keyFrame5023.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5023.ViewUp = [0.49937120690706094, -0.866, -0.022987316506138757]
keyFrame5023.ViewAngle = 30.0
keyFrame5023.ParallelScale = 0.97681
keyFrame5023.PositionPathPoints = [27.069170052588234, 11.34, 64.95239860965042]
keyFrame5023.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5023.PositionMode = 'Path'
keyFrame5023.FocalPointMode = 'Path'
keyFrame5023.ClosedFocalPath = 0
keyFrame5023.ClosedPositionPath = 0

# ====================================================================
keyFrame5024 = CameraKeyFrame()
keyFrame5024.KeyTime = 0.06
keyFrame5024.KeyValues = [0.0]
keyFrame5024.Position = [27.15907065183517, 11.34, 64.94817018145929]
keyFrame5024.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5024.ViewUp = [0.4993242342501075, -0.866, -0.02398601230370912]
keyFrame5024.ViewAngle = 30.0
keyFrame5024.ParallelScale = 0.97681
keyFrame5024.PositionPathPoints = [27.15907065183517, 11.34, 64.94817018145929]
keyFrame5024.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5024.PositionMode = 'Path'
keyFrame5024.FocalPointMode = 'Path'
keyFrame5024.ClosedFocalPath = 0
keyFrame5024.ClosedPositionPath = 0

# ====================================================================
keyFrame5025 = CameraKeyFrame()
keyFrame5025.KeyTime = 0.0625
keyFrame5025.KeyValues = [0.0]
keyFrame5025.Position = [27.248962614059888, 11.34, 64.94376195009824]
keyFrame5025.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5025.ViewUp = [0.4992752641609812, -0.866, -0.024984612154487974]
keyFrame5025.ViewAngle = 30.0
keyFrame5025.ParallelScale = 0.97681
keyFrame5025.PositionPathPoints = [27.248962614059888, 11.34, 64.94376195009824]
keyFrame5025.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5025.PositionMode = 'Path'
keyFrame5025.FocalPointMode = 'Path'
keyFrame5025.ClosedFocalPath = 0
keyFrame5025.ClosedPositionPath = 0

# ====================================================================
keyFrame5026 = CameraKeyFrame()
keyFrame5026.KeyTime = 0.065
keyFrame5026.KeyValues = [0.0]
keyFrame5026.Position = [27.33884558027733, 11.34, 64.93917394719719]
keyFrame5026.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5026.ViewUp = [0.4992242967612957, -0.866, -0.025983112061363372]
keyFrame5026.ViewAngle = 30.0
keyFrame5026.ParallelScale = 0.97681
keyFrame5026.PositionPathPoints = [27.33884558027733, 11.34, 64.93917394719719]
keyFrame5026.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5026.PositionMode = 'Path'
keyFrame5026.FocalPointMode = 'Path'
keyFrame5026.ClosedFocalPath = 0
keyFrame5026.ClosedPositionPath = 0

# ====================================================================
keyFrame5027 = CameraKeyFrame()
keyFrame5027.KeyTime = 0.0675
keyFrame5027.KeyValues = [0.0]
keyFrame5027.Position = [27.428719191107877, 11.34, 64.93440619476937]
keyFrame5027.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5027.ViewUp = [0.49917133220525184, -0.866, -0.026981508028545566]
keyFrame5027.ViewAngle = 30.0
keyFrame5027.ParallelScale = 0.97681
keyFrame5027.PositionPathPoints = [27.428719191107877, 11.34, 64.93440619476937]
keyFrame5027.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5027.PositionMode = 'Path'
keyFrame5027.FocalPointMode = 'Path'
keyFrame5027.ClosedFocalPath = 0
keyFrame5027.ClosedPositionPath = 0

# ====================================================================
keyFrame5028 = CameraKeyFrame()
keyFrame5028.KeyTime = 0.07
keyFrame5028.KeyValues = [0.0]
keyFrame5028.Position = [27.5185830869957, 11.34, 64.92945871053305]
keyFrame5028.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5028.ViewUp = [0.49911637103199524, -0.866, -0.027979796075863938]
keyFrame5028.ViewAngle = 30.0
keyFrame5028.ParallelScale = 0.97681
keyFrame5028.PositionPathPoints = [27.5185830869957, 11.34, 64.92945871053305]
keyFrame5028.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5028.PositionMode = 'Path'
keyFrame5028.FocalPointMode = 'Path'
keyFrame5028.ClosedFocalPath = 0
keyFrame5028.ClosedPositionPath = 0

# ====================================================================
keyFrame5029 = CameraKeyFrame()
keyFrame5029.KeyTime = 0.0725
keyFrame5029.KeyValues = [0.0]
keyFrame5029.Position = [27.608436908384977, 11.34, 64.92433151220658]
keyFrame5029.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5029.ViewUp = [0.49905941356183214, -0.866, -0.02897797221426844]
keyFrame5029.ViewAngle = 30.0
keyFrame5029.ParallelScale = 0.97681
keyFrame5029.PositionPathPoints = [27.608436908384977, 11.34, 64.92433151220658]
keyFrame5029.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5029.PositionMode = 'Path'
keyFrame5029.FocalPointMode = 'Path'
keyFrame5029.ClosedFocalPath = 0
keyFrame5029.ClosedPositionPath = 0

# ====================================================================
keyFrame5030 = CameraKeyFrame()
keyFrame5030.KeyTime = 0.075
keyFrame5030.KeyValues = [0.0]
keyFrame5030.Position = [27.69828029571988, 11.34, 64.91902461750828]
keyFrame5030.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5030.ViewUp = [0.49900046000781084, -0.866, -0.02997603245035708]
keyFrame5030.ViewAngle = 30.0
keyFrame5030.ParallelScale = 0.97681
keyFrame5030.PositionPathPoints = [27.69828029571988, 11.34, 64.91902461750828]
keyFrame5030.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5030.PositionMode = 'Path'
keyFrame5030.FocalPointMode = 'Path'
keyFrame5030.ClosedFocalPath = 0
keyFrame5030.ClosedPositionPath = 0

# ====================================================================
keyFrame5031 = CameraKeyFrame()
keyFrame5031.KeyTime = 0.0775
keyFrame5031.KeyValues = [0.0]
keyFrame5031.Position = [27.788112889444584, 11.34, 64.91353804415648]
keyFrame5031.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5031.ViewUp = [0.4989395105829797, -0.866, -0.03097397279072786]
keyFrame5031.ViewAngle = 30.0
keyFrame5031.ParallelScale = 0.97681
keyFrame5031.PositionPathPoints = [27.788112889444584, 11.34, 64.91353804415648]
keyFrame5031.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5031.PositionMode = 'Path'
keyFrame5031.FocalPointMode = 'Path'
keyFrame5031.ClosedFocalPath = 0
keyFrame5031.ClosedPositionPath = 0

# ====================================================================
keyFrame5032 = CameraKeyFrame()
keyFrame5032.KeyTime = 0.08
keyFrame5032.KeyValues = [0.0]
keyFrame5032.Position = [27.877934330003264, 11.34, 64.9078718098695]
keyFrame5032.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5032.ViewUp = [0.49887656550038706, -0.866, -0.03197178924197877]
keyFrame5032.ViewAngle = 30.0
keyFrame5032.ParallelScale = 0.97681
keyFrame5032.PositionPathPoints = [27.877934330003264, 11.34, 64.9078718098695]
keyFrame5032.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5032.PositionMode = 'Path'
keyFrame5032.FocalPointMode = 'Path'
keyFrame5032.ClosedFocalPath = 0
keyFrame5032.ClosedPositionPath = 0

# ====================================================================
keyFrame5033 = CameraKeyFrame()
keyFrame5033.KeyTime = 0.0825
keyFrame5033.KeyValues = [0.0]
keyFrame5033.Position = [27.96774425789609, 11.34, 64.90202593334135]
keyFrame5033.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5033.ViewUp = [0.49881162497308124, -0.866, -0.03296947781070782]
keyFrame5033.ViewAngle = 30.0
keyFrame5033.ParallelScale = 0.97681
keyFrame5033.PositionPathPoints = [27.96774425789609, 11.34, 64.90202593334135]
keyFrame5033.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5033.PositionMode = 'Path'
keyFrame5033.FocalPointMode = 'Path'
keyFrame5033.ClosedFocalPath = 0
keyFrame5033.ClosedPositionPath = 0

# ====================================================================
keyFrame5034 = CameraKeyFrame()
keyFrame5034.KeyTime = 0.085
keyFrame5034.KeyValues = [0.0]
keyFrame5034.Position = [28.057542314632617, 11.34, 64.89600045085214]
keyFrame5034.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5034.ViewUp = [0.4987446892141106, -0.866, -0.033967034503513]
keyFrame5034.ViewAngle = 30.0
keyFrame5034.ParallelScale = 0.97681
keyFrame5034.PositionPathPoints = [28.057542314632617, 11.34, 64.89600045085214]
keyFrame5034.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5034.PositionMode = 'Path'
keyFrame5034.FocalPointMode = 'Path'
keyFrame5034.ClosedFocalPath = 0
keyFrame5034.ClosedPositionPath = 0

# ====================================================================
keyFrame5035 = CameraKeyFrame()
keyFrame5035.KeyTime = 0.0875
keyFrame5035.KeyValues = [0.0]
keyFrame5035.Position = [28.147328141316706, 11.34, 64.88979539161406]
keyFrame5035.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5035.ViewUp = [0.49867575843652345, -0.866, -0.03496445532699232]
keyFrame5035.ViewAngle = 30.0
keyFrame5035.ParallelScale = 0.97681
keyFrame5035.PositionPathPoints = [28.147328141316706, 11.34, 64.88979539161406]
keyFrame5035.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5035.PositionMode = 'Path'
keyFrame5035.FocalPointMode = 'Path'
keyFrame5035.ClosedFocalPath = 0
keyFrame5035.ClosedPositionPath = 0

# ====================================================================
keyFrame5036 = CameraKeyFrame()
keyFrame5036.KeyTime = 0.09
keyFrame5036.KeyValues = [0.0]
keyFrame5036.Position = [28.237101378726546, 11.34, 64.88341077916476]
keyFrame5036.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5036.ViewUp = [0.49860483285336815, -0.866, -0.035961736287743774]
keyFrame5036.ViewAngle = 30.0
keyFrame5036.ParallelScale = 0.97681
keyFrame5036.PositionPathPoints = [28.237101378726546, 11.34, 64.88341077916476]
keyFrame5036.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5036.PositionMode = 'Path'
keyFrame5036.FocalPointMode = 'Path'
keyFrame5036.ClosedFocalPath = 0
keyFrame5036.ClosedPositionPath = 0

# ====================================================================
keyFrame5037 = CameraKeyFrame()
keyFrame5037.KeyTime = 0.0925
keyFrame5037.KeyValues = [0.0]
keyFrame5037.Position = [28.326861667640316, 11.34, 64.87684663704192]
keyFrame5037.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5037.ViewUp = [0.4985319126776931, -0.866, -0.03695887339236536]
keyFrame5037.ViewAngle = 30.0
keyFrame5037.ParallelScale = 0.97681
keyFrame5037.PositionPathPoints = [28.326861667640316, 11.34, 64.87684663704192]
keyFrame5037.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5037.PositionMode = 'Path'
keyFrame5037.FocalPointMode = 'Path'
keyFrame5037.ClosedFocalPath = 0
keyFrame5037.ClosedPositionPath = 0

# ====================================================================
keyFrame5038 = CameraKeyFrame()
keyFrame5038.KeyTime = 0.095
keyFrame5038.KeyValues = [0.0]
keyFrame5038.Position = [28.416608648836196, 11.34, 64.87010298878326]
keyFrame5038.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5038.ViewUp = [0.4984569981225465, -0.866, -0.03795586264745508]
keyFrame5038.ViewAngle = 30.0
keyFrame5038.ParallelScale = 0.97681
keyFrame5038.PositionPathPoints = [28.416608648836196, 11.34, 64.87010298878326]
keyFrame5038.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5038.PositionMode = 'Path'
keyFrame5038.FocalPointMode = 'Path'
keyFrame5038.ClosedFocalPath = 0
keyFrame5038.ClosedPositionPath = 0

# ====================================================================
keyFrame5039 = CameraKeyFrame()
keyFrame5039.KeyTime = 0.0975
keyFrame5039.KeyValues = [0.0]
keyFrame5039.Position = [28.506341963092368, 11.34, 64.86317985792644]
keyFrame5039.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5039.ViewUp = [0.49838009386564974, -0.866, -0.03895270035303934]
keyFrame5039.ViewAngle = 30.0
keyFrame5039.ParallelScale = 0.97681
keyFrame5039.PositionPathPoints = [28.506341963092368, 11.34, 64.86317985792644]
keyFrame5039.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5039.PositionMode = 'Path'
keyFrame5039.FocalPointMode = 'Path'
keyFrame5039.ClosedFocalPath = 0
keyFrame5039.ClosedPositionPath = 0

# ====================================================================
keyFrame5040 = CameraKeyFrame()
keyFrame5040.KeyTime = 0.1
keyFrame5040.KeyValues = [0.0]
keyFrame5040.Position = [28.596061251187017, 11.34, 64.85607726800916]
keyFrame5040.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5040.ViewUp = [0.498301190602249, -0.866, -0.039949381890184654]
keyFrame5040.ViewAngle = 30.0
keyFrame5040.ParallelScale = 0.97681
keyFrame5040.PositionPathPoints = [28.596061251187017, 11.34, 64.85607726800916]
keyFrame5040.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5040.PositionMode = 'Path'
keyFrame5040.FocalPointMode = 'Path'
keyFrame5040.ClosedFocalPath = 0
keyFrame5040.ClosedPositionPath = 0

# ====================================================================
keyFrame5041 = CameraKeyFrame()
keyFrame5041.KeyTime = 0.1025
keyFrame5041.KeyValues = [0.0]
keyFrame5041.Position = [28.685766153937696, 11.34, 64.84879524309163]
keyFrame5041.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5041.ViewUp = [0.49822029466745454, -0.866, -0.040945903667844785]
keyFrame5041.ViewAngle = 30.0
keyFrame5041.ParallelScale = 0.97681
keyFrame5041.PositionPathPoints = [28.685766153937696, 11.34, 64.84879524309163]
keyFrame5041.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5041.PositionMode = 'Path'
keyFrame5041.FocalPointMode = 'Path'
keyFrame5041.ClosedFocalPath = 0
keyFrame5041.ClosedPositionPath = 0

# ====================================================================
keyFrame5042 = CameraKeyFrame()
keyFrame5042.KeyTime = 0.105
keyFrame5042.KeyValues = [0.0]
keyFrame5042.Position = [28.77545631366802, 11.34, 64.84133382722203]
keyFrame5042.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5042.ViewUp = [0.4981374062931046, -0.866, -0.04194226169385264]
keyFrame5042.ViewAngle = 30.0
keyFrame5042.ParallelScale = 0.97681
keyFrame5042.PositionPathPoints = [28.77545631366802, 11.34, 64.84133382722203]
keyFrame5042.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5042.PositionMode = 'Path'
keyFrame5042.FocalPointMode = 'Path'
keyFrame5042.ClosedFocalPath = 0
keyFrame5042.ClosedPositionPath = 0

# ====================================================================
keyFrame5043 = CameraKeyFrame()
keyFrame5043.KeyTime = 0.1075
keyFrame5043.KeyValues = [0.0]
keyFrame5043.Position = [28.865131372264326, 11.34, 64.83369305864505]
keyFrame5043.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5043.ViewUp = [0.498052525719019, -0.866, -0.0429384519765657]
keyFrame5043.ViewAngle = 30.0
keyFrame5043.ParallelScale = 0.97681
keyFrame5043.PositionPathPoints = [28.865131372264326, 11.34, 64.83369305864505]
keyFrame5043.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5043.PositionMode = 'Path'
keyFrame5043.FocalPointMode = 'Path'
keyFrame5043.ClosedFocalPath = 0
keyFrame5043.ClosedPositionPath = 0

# ====================================================================
keyFrame5044 = CameraKeyFrame()
keyFrame5044.KeyTime = 0.11
keyFrame5044.KeyValues = [0.0]
keyFrame5044.Position = [28.954790970931516, 11.34, 64.82587296656168]
keyFrame5044.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5044.ViewUp = [0.497965653192999, -0.866, -0.043934470524866]
keyFrame5044.ViewAngle = 30.0
keyFrame5044.ParallelScale = 0.97681
keyFrame5044.PositionPathPoints = [28.954790970931516, 11.34, 64.82587296656168]
keyFrame5044.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5044.PositionMode = 'Path'
keyFrame5044.FocalPointMode = 'Path'
keyFrame5044.ClosedFocalPath = 0
keyFrame5044.ClosedPositionPath = 0

# ====================================================================
keyFrame5045 = CameraKeyFrame()
keyFrame5045.KeyTime = 0.1125
keyFrame5045.KeyValues = [0.0]
keyFrame5045.Position = [29.044434750874494, 11.34, 64.81787358017286]
keyFrame5045.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5045.ViewUp = [0.49787678897082754, -0.866, -0.044930313348160174]
keyFrame5045.ViewAngle = 30.0
keyFrame5045.ParallelScale = 0.97681
keyFrame5045.PositionPathPoints = [29.044434750874494, 11.34, 64.81787358017286]
keyFrame5045.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5045.PositionMode = 'Path'
keyFrame5045.FocalPointMode = 'Path'
keyFrame5045.ClosedFocalPath = 0
keyFrame5045.ClosedPositionPath = 0

# ====================================================================
keyFrame5046 = CameraKeyFrame()
keyFrame5046.KeyTime = 0.115
keyFrame5046.KeyValues = [0.0]
keyFrame5046.Position = [29.134062353298162, 11.34, 64.80969492867959]
keyFrame5046.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5046.ViewUp = [0.49778593331626897, -0.866, -0.04592597645637938]
keyFrame5046.ViewAngle = 30.0
keyFrame5046.ParallelScale = 0.97681
keyFrame5046.PositionPathPoints = [29.134062353298162, 11.34, 64.80969492867959]
keyFrame5046.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5046.PositionMode = 'Path'
keyFrame5046.FocalPointMode = 'Path'
keyFrame5046.ClosedFocalPath = 0
keyFrame5046.ClosedPositionPath = 0

# ====================================================================
keyFrame5047 = CameraKeyFrame()
keyFrame5047.KeyTime = 0.1175
keyFrame5047.KeyValues = [0.0]
keyFrame5047.Position = [29.223673419407422, 11.34, 64.8013370412828]
keyFrame5047.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5047.ViewUp = [0.4976930865010693, -0.866, -0.04692145585997936]
keyFrame5047.ViewAngle = 30.0
keyFrame5047.ParallelScale = 0.97681
keyFrame5047.PositionPathPoints = [29.223673419407422, 11.34, 64.8013370412828]
keyFrame5047.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5047.PositionMode = 'Path'
keyFrame5047.FocalPointMode = 'Path'
keyFrame5047.ClosedFocalPath = 0
keyFrame5047.ClosedPositionPath = 0

# ====================================================================
keyFrame5048 = CameraKeyFrame()
keyFrame5048.KeyTime = 0.12
keyFrame5048.KeyValues = [0.0]
keyFrame5048.Position = [29.313267590407175, 11.34, 64.79279994718351]
keyFrame5048.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5048.ViewUp = [0.49759824880495596, -0.866, -0.04791674756994042]
keyFrame5048.ViewAngle = 30.0
keyFrame5048.ParallelScale = 0.97681
keyFrame5048.PositionPathPoints = [29.313267590407175, 11.34, 64.79279994718351]
keyFrame5048.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5048.PositionMode = 'Path'
keyFrame5048.FocalPointMode = 'Path'
keyFrame5048.ClosedFocalPath = 0
keyFrame5048.ClosedPositionPath = 0

# ====================================================================
keyFrame5049 = CameraKeyFrame()
keyFrame5049.KeyTime = 0.1225
keyFrame5049.KeyValues = [0.0]
keyFrame5049.Position = [29.402844507502326, 11.34, 64.78408367558265]
keyFrame5049.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5049.ViewUp = [0.49750142051563806, -0.866, -0.04891184759776743]
keyFrame5049.ViewAngle = 30.0
keyFrame5049.ParallelScale = 0.97681
keyFrame5049.PositionPathPoints = [29.402844507502326, 11.34, 64.78408367558265]
keyFrame5049.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5049.PositionMode = 'Path'
keyFrame5049.FocalPointMode = 'Path'
keyFrame5049.ClosedFocalPath = 0
keyFrame5049.ClosedPositionPath = 0

# ====================================================================
keyFrame5050 = CameraKeyFrame()
keyFrame5050.KeyTime = 0.125
keyFrame5050.KeyValues = [0.0]
keyFrame5050.Position = [29.492403811897773, 11.34, 64.7751882556812]
keyFrame5050.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5050.ViewUp = [0.4974026019593449, -0.866, -0.04990675195874769]
keyFrame5050.ViewAngle = 30.0
keyFrame5050.ParallelScale = 0.97681
keyFrame5050.PositionPathPoints = [29.492403811897773, 11.34, 64.7751882556812]
keyFrame5050.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5050.PositionMode = 'Path'
keyFrame5050.FocalPointMode = 'Path'
keyFrame5050.ClosedFocalPath = 0
keyFrame5050.ClosedPositionPath = 0

# ====================================================================
keyFrame5051 = CameraKeyFrame()
keyFrame5051.KeyTime = 0.1275
keyFrame5051.KeyValues = [0.0]
keyFrame5051.Position = [29.58194514479842, 11.34, 64.76611371668011]
keyFrame5051.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5051.ViewUp = [0.49730179380370815, -0.866, -0.050901456704262646]
keyFrame5051.ViewAngle = 30.0
keyFrame5051.ParallelScale = 0.97681
keyFrame5051.PositionPathPoints = [29.58194514479842, 11.34, 64.76611371668011]
keyFrame5051.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5051.PositionMode = 'Path'
keyFrame5051.FocalPointMode = 'Path'
keyFrame5051.ClosedFocalPath = 0
keyFrame5051.ClosedPositionPath = 0

# ====================================================================
keyFrame5052 = CameraKeyFrame()
keyFrame5052.KeyTime = 0.13
keyFrame5052.KeyValues = [0.0]
keyFrame5052.Position = [29.671468149063628, 11.34, 64.75686010594517]
keyFrame5052.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5052.ViewUp = [0.4971989965163678, -0.866, -0.05189595786403153]
keyFrame5052.ViewAngle = 30.0
keyFrame5052.ParallelScale = 0.97681
keyFrame5052.PositionPathPoints = [29.671468149063628, 11.34, 64.75686010594517]
keyFrame5052.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5052.PositionMode = 'Path'
keyFrame5052.FocalPointMode = 'Path'
keyFrame5052.ClosedFocalPath = 0
keyFrame5052.ClosedPositionPath = 0

# ====================================================================
keyFrame5053 = CameraKeyFrame()
keyFrame5053.KeyTime = 0.1325
keyFrame5053.KeyValues = [0.0]
keyFrame5053.Position = [29.760972468378956, 11.34, 64.74742747991317]
keyFrame5053.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5053.ViewUp = [0.49709421048299324, -0.866, -0.05289025145870205]
keyFrame5053.ViewAngle = 30.0
keyFrame5053.ParallelScale = 0.97681
keyFrame5053.PositionPathPoints = [29.760972468378956, 11.34, 64.74742747991317]
keyFrame5053.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5053.PositionMode = 'Path'
keyFrame5053.FocalPointMode = 'Path'
keyFrame5053.ClosedFocalPath = 0
keyFrame5053.ClosedPositionPath = 0

# ====================================================================
keyFrame5054 = CameraKeyFrame()
keyFrame5054.KeyTime = 0.135
keyFrame5054.KeyValues = [0.0]
keyFrame5054.Position = [29.850457744637236, 11.34, 64.73781587533811]
keyFrame5054.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5054.ViewUp = [0.49698743609990953, -0.866, -0.05388433350973172]
keyFrame5054.ViewAngle = 30.0
keyFrame5054.ParallelScale = 0.97681
keyFrame5054.PositionPathPoints = [29.850457744637236, 11.34, 64.73781587533811]
keyFrame5054.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5054.PositionMode = 'Path'
keyFrame5054.FocalPointMode = 'Path'
keyFrame5054.ClosedFocalPath = 0
keyFrame5054.ClosedPositionPath = 0

# ====================================================================
keyFrame5055 = CameraKeyFrame()
keyFrame5055.KeyTime = 0.1375
keyFrame5055.KeyValues = [0.0]
keyFrame5055.Position = [29.9399236197259, 11.34, 64.7280253289146]
keyFrame5055.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5055.ViewUp = [0.49687867377409745, -0.866, -0.054878200039387925]
keyFrame5055.ViewAngle = 30.0
keyFrame5055.ParallelScale = 0.97681
keyFrame5055.PositionPathPoints = [29.9399236197259, 11.34, 64.7280253289146]
keyFrame5055.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5055.PositionMode = 'Path'
keyFrame5055.FocalPointMode = 'Path'
keyFrame5055.ClosedFocalPath = 0
keyFrame5055.ClosedPositionPath = 0

# ====================================================================
keyFrame5056 = CameraKeyFrame()
keyFrame5056.KeyTime = 0.14
keyFrame5056.KeyValues = [0.0]
keyFrame5056.Position = [30.029369735532367, 11.34, 64.71805587733724]
keyFrame5056.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5056.ViewUp = [0.4967679239231932, -0.866, -0.05587184707074788]
keyFrame5056.ViewAngle = 30.0
keyFrame5056.ParallelScale = 0.97681
keyFrame5056.PositionPathPoints = [30.029369735532367, 11.34, 64.71805587733724]
keyFrame5056.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5056.PositionMode = 'Path'
keyFrame5056.FocalPointMode = 'Path'
keyFrame5056.ClosedFocalPath = 0
keyFrame5056.ClosedPositionPath = 0

# ====================================================================
keyFrame5057 = CameraKeyFrame()
keyFrame5057.KeyTime = 0.1425
keyFrame5057.KeyValues = [0.0]
keyFrame5057.Position = [30.118795733944072, 11.34, 64.70790755730066]
keyFrame5057.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5057.ViewUp = [0.4966551869754888, -0.866, -0.05686527062769863]
keyFrame5057.ViewAngle = 30.0
keyFrame5057.ParallelScale = 0.97681
keyFrame5057.PositionPathPoints = [30.118795733944072, 11.34, 64.70790755730066]
keyFrame5057.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5057.PositionMode = 'Path'
keyFrame5057.FocalPointMode = 'Path'
keyFrame5057.ClosedFocalPath = 0
keyFrame5057.ClosedPositionPath = 0

# ====================================================================
keyFrame5058 = CameraKeyFrame()
keyFrame5058.KeyTime = 0.145
keyFrame5058.KeyValues = [0.0]
keyFrame5058.Position = [30.208201256848444, 11.34, 64.69758040549947]
keyFrame5058.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5058.ViewUp = [0.49654046336993185, -0.866, -0.05785846673493706]
keyFrame5058.ViewAngle = 30.0
keyFrame5058.ParallelScale = 0.97681
keyFrame5058.PositionPathPoints = [30.208201256848444, 11.34, 64.69758040549947]
keyFrame5058.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5058.PositionMode = 'Path'
keyFrame5058.FocalPointMode = 'Path'
keyFrame5058.ClosedFocalPath = 0
keyFrame5058.ClosedPositionPath = 0

# ====================================================================
keyFrame5059 = CameraKeyFrame()
keyFrame5059.KeyTime = 0.1475
keyFrame5059.KeyValues = [0.0]
keyFrame5059.Position = [30.2975859461329, 11.34, 64.68707445862827]
keyFrame5059.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5059.ViewUp = [0.4964237535561256, -0.866, -0.05885143141796989]
keyFrame5059.ViewAngle = 30.0
keyFrame5059.ParallelScale = 0.97681
keyFrame5059.PositionPathPoints = [30.2975859461329, 11.34, 64.68707445862827]
keyFrame5059.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5059.PositionMode = 'Path'
keyFrame5059.FocalPointMode = 'Path'
keyFrame5059.ClosedFocalPath = 0
keyFrame5059.ClosedPositionPath = 0

# ====================================================================
keyFrame5060 = CameraKeyFrame()
keyFrame5060.KeyTime = 0.15
keyFrame5060.KeyValues = [0.0]
keyFrame5060.Position = [30.38694944368488, 11.34, 64.6763897533817]
keyFrame5060.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5060.ViewUp = [0.49630505799432884, -0.866, -0.05984416070311369]
keyFrame5060.ViewAngle = 30.0
keyFrame5060.ParallelScale = 0.97681
keyFrame5060.PositionPathPoints = [30.38694944368488, 11.34, 64.6763897533817]
keyFrame5060.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5060.PositionMode = 'Path'
keyFrame5060.FocalPointMode = 'Path'
keyFrame5060.ClosedFocalPath = 0
keyFrame5060.ClosedPositionPath = 0

# ====================================================================
keyFrame5061 = CameraKeyFrame()
keyFrame5061.KeyTime = 0.1525
keyFrame5061.KeyValues = [0.0]
keyFrame5061.Position = [30.476291391391804, 11.34, 64.66552632645437]
keyFrame5061.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5061.ViewUp = [0.49618437715545605, -0.866, -0.06083665061749487]
keyFrame5061.ViewAngle = 30.0
keyFrame5061.ParallelScale = 0.97681
keyFrame5061.PositionPathPoints = [30.476291391391804, 11.34, 64.66552632645437]
keyFrame5061.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5061.PositionMode = 'Path'
keyFrame5061.FocalPointMode = 'Path'
keyFrame5061.ClosedFocalPath = 0
keyFrame5061.ClosedPositionPath = 0

# ====================================================================
keyFrame5062 = CameraKeyFrame()
keyFrame5062.KeyTime = 0.155
keyFrame5062.KeyValues = [0.0]
keyFrame5062.Position = [30.565611432226223, 11.34, 64.65448422415531]
keyFrame5062.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5062.ViewUp = [0.49606171152107736, -0.866, -0.06182889718904966]
keyFrame5062.ViewAngle = 30.0
keyFrame5062.ParallelScale = 0.97681
keyFrame5062.PositionPathPoints = [30.565611432226223, 11.34, 64.65448422415531]
keyFrame5062.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5062.PositionMode = 'Path'
keyFrame5062.FocalPointMode = 'Path'
keyFrame5062.ClosedFocalPath = 0
keyFrame5062.ClosedPositionPath = 0

# ====================================================================
keyFrame5063 = CameraKeyFrame()
keyFrame5063.KeyTime = 0.1575
keyFrame5063.KeyValues = [0.0]
keyFrame5063.Position = [30.654909211619366, 11.34, 64.64326351457791]
keyFrame5063.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5063.ViewUp = [0.49593706158341855, -0.866, -0.06282089644652414]
keyFrame5063.ViewAngle = 30.0
keyFrame5063.ParallelScale = 0.97681
keyFrame5063.PositionPathPoints = [30.654909211619366, 11.34, 64.64326351457791]
keyFrame5063.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5063.PositionMode = 'Path'
keyFrame5063.FocalPointMode = 'Path'
keyFrame5063.ClosedFocalPath = 0
keyFrame5063.ClosedPositionPath = 0

# ====================================================================
keyFrame5064 = CameraKeyFrame()
keyFrame5064.KeyTime = 0.16
keyFrame5064.KeyValues = [0.0]
keyFrame5064.Position = [30.74418437247287, 11.34, 64.6318642434029]
keyFrame5064.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5064.ViewUp = [0.495810427845361, -0.866, -0.06381264441947423]
keyFrame5064.ViewAngle = 30.0
keyFrame5064.ParallelScale = 0.97681
keyFrame5064.PositionPathPoints = [30.74418437247287, 11.34, 64.6318642434029]
keyFrame5064.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5064.PositionMode = 'Path'
keyFrame5064.FocalPointMode = 'Path'
keyFrame5064.ClosedFocalPath = 0
keyFrame5064.ClosedPositionPath = 0

# ====================================================================
keyFrame5065 = CameraKeyFrame()
keyFrame5065.KeyTime = 0.1625
keyFrame5065.KeyValues = [0.0]
keyFrame5065.Position = [30.83343655750134, 11.34, 64.62028645465392]
keyFrame5065.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5065.ViewUp = [0.4956818108204416, -0.866, -0.06480413713826569]
keyFrame5065.ViewAngle = 30.0
keyFrame5065.ParallelScale = 0.97681
keyFrame5065.PositionPathPoints = [30.83343655750134, 11.34, 64.62028645465392]
keyFrame5065.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5065.PositionMode = 'Path'
keyFrame5065.FocalPointMode = 'Path'
keyFrame5065.ClosedFocalPath = 0
keyFrame5065.ClosedPositionPath = 0

# ====================================================================
keyFrame5066 = CameraKeyFrame()
keyFrame5066.KeyTime = 0.165
keyFrame5066.KeyValues = [0.0]
keyFrame5066.Position = [30.9226654094194, 11.34, 64.6085301923546]
keyFrame5066.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5066.ViewUp = [0.49555121103285316, -0.866, -0.0657953706340741]
keyFrame5066.ViewAngle = 30.0
keyFrame5066.ParallelScale = 0.97681
keyFrame5066.PositionPathPoints = [30.9226654094194, 11.34, 64.6085301923546]
keyFrame5066.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5066.PositionMode = 'Path'
keyFrame5066.FocalPointMode = 'Path'
keyFrame5066.ClosedFocalPath = 0
keyFrame5066.ClosedPositionPath = 0

# ====================================================================
keyFrame5067 = CameraKeyFrame()
keyFrame5067.KeyTime = 0.1675
keyFrame5067.KeyValues = [0.0]
keyFrame5067.Position = [31.011870570941642, 11.34, 64.59659550052857]
keyFrame5067.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5067.ViewUp = [0.49541862901744377, -0.866, -0.0667863409388849]
keyFrame5067.ViewAngle = 30.0
keyFrame5067.ParallelScale = 0.97681
keyFrame5067.PositionPathPoints = [31.011870570941642, 11.34, 64.59659550052857]
keyFrame5067.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5067.PositionMode = 'Path'
keyFrame5067.FocalPointMode = 'Path'
keyFrame5067.ClosedFocalPath = 0
keyFrame5067.ClosedPositionPath = 0

# ====================================================================
keyFrame5068 = CameraKeyFrame()
keyFrame5068.KeyTime = 0.17
keyFrame5068.KeyValues = [0.0]
keyFrame5068.Position = [31.101051684782693, 11.34, 64.58448242319943]
keyFrame5068.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5068.ViewUp = [0.49528406531971747, -0.866, -0.06777704408549336]
keyFrame5068.ViewAngle = 30.0
keyFrame5068.ParallelScale = 0.97681
keyFrame5068.PositionPathPoints = [31.101051684782693, 11.34, 64.58448242319943]
keyFrame5068.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5068.PositionMode = 'Path'
keyFrame5068.FocalPointMode = 'Path'
keyFrame5068.ClosedFocalPath = 0
keyFrame5068.ClosedPositionPath = 0

# ====================================================================
keyFrame5069 = CameraKeyFrame()
keyFrame5069.KeyTime = 0.1725
keyFrame5069.KeyValues = [0.0]
keyFrame5069.Position = [31.19020839365715, 11.34, 64.57219100439085]
keyFrame5069.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5069.ViewUp = [0.4951475204958337, -0.866, -0.06876747610750458]
keyFrame5069.ViewAngle = 30.0
keyFrame5069.ParallelScale = 0.97681
keyFrame5069.PositionPathPoints = [31.19020839365715, 11.34, 64.57219100439085]
keyFrame5069.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5069.PositionMode = 'Path'
keyFrame5069.FocalPointMode = 'Path'
keyFrame5069.ClosedFocalPath = 0
keyFrame5069.ClosedPositionPath = 0

# ====================================================================
keyFrame5070 = CameraKeyFrame()
keyFrame5070.KeyTime = 0.175
keyFrame5070.KeyValues = [0.0]
keyFrame5070.Position = [31.279340340279635, 11.34, 64.55972128812641]
keyFrame5070.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5070.ViewUp = [0.4950089951126077, -0.866, -0.06975763303933354]
keyFrame5070.ViewAngle = 30.0
keyFrame5070.ParallelScale = 0.97681
keyFrame5070.PositionPathPoints = [31.279340340279635, 11.34, 64.55972128812641]
keyFrame5070.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5070.PositionMode = 'Path'
keyFrame5070.FocalPointMode = 'Path'
keyFrame5070.ClosedFocalPath = 0
keyFrame5070.ClosedPositionPath = 0

# ====================================================================
keyFrame5071 = CameraKeyFrame()
keyFrame5071.KeyTime = 0.1775
keyFrame5071.KeyValues = [0.0]
keyFrame5071.Position = [31.368447167364753, 11.34, 64.54707331842977]
keyFrame5071.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5071.ViewUp = [0.49486848974751024, -0.866, -0.07074751091620497]
keyFrame5071.ViewAngle = 30.0
keyFrame5071.ParallelScale = 0.97681
keyFrame5071.PositionPathPoints = [31.368447167364753, 11.34, 64.54707331842977]
keyFrame5071.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5071.PositionMode = 'Path'
keyFrame5071.FocalPointMode = 'Path'
keyFrame5071.ClosedFocalPath = 0
keyFrame5071.ClosedPositionPath = 0

# ====================================================================
keyFrame5072 = CameraKeyFrame()
keyFrame5072.KeyTime = 0.18
keyFrame5072.KeyValues = [0.0]
keyFrame5072.Position = [31.45752855464386, 11.34, 64.53424741633727]
keyFrame5072.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5072.ViewUp = [0.4947260049886677, -0.866, -0.07173710577415354]
keyFrame5072.ViewAngle = 30.0
keyFrame5072.ParallelScale = 0.97681
keyFrame5072.PositionPathPoints = [31.45752855464386, 11.34, 64.53424741633727]
keyFrame5072.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5072.PositionMode = 'Path'
keyFrame5072.FocalPointMode = 'Path'
keyFrame5072.ClosedFocalPath = 0
keyFrame5072.ClosedPositionPath = 0

# ====================================================================
keyFrame5073 = CameraKeyFrame()
keyFrame5073.KeyTime = 0.1825
keyFrame5073.KeyValues = [0.0]
keyFrame5073.Position = [31.54658406329152, 11.34, 64.52124301567221]
keyFrame5073.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5073.ViewUp = [0.4945815414008557, -0.866, -0.07272641365618296]
keyFrame5073.ViewAngle = 30.0
keyFrame5073.ParallelScale = 0.97681
keyFrame5073.PositionPathPoints = [31.54658406329152, 11.34, 64.52124301567221]
keyFrame5073.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5073.PositionMode = 'Path'
keyFrame5073.FocalPointMode = 'Path'
keyFrame5073.ClosedFocalPath = 0
keyFrame5073.ClosedPositionPath = 0

# ====================================================================
keyFrame5074 = CameraKeyFrame()
keyFrame5074.KeyTime = 0.185
keyFrame5074.KeyValues = [0.0]
keyFrame5074.Position = [31.63561339066253, 11.34, 64.50806056935497]
keyFrame5074.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5074.ViewUp = [0.4944350993962434, -0.866, -0.07371543063567708]
keyFrame5074.ViewAngle = 30.0
keyFrame5074.ParallelScale = 0.97681
keyFrame5074.PositionPathPoints = [31.63561339066253, 11.34, 64.50806056935497]
keyFrame5074.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5074.PositionMode = 'Path'
keyFrame5074.FocalPointMode = 'Path'
keyFrame5074.ClosedFocalPath = 0
keyFrame5074.ClosedPositionPath = 0

# ====================================================================
keyFrame5075 = CameraKeyFrame()
keyFrame5075.KeyTime = 0.1875
keyFrame5075.KeyValues = [0.0]
keyFrame5075.Position = [31.724616179657996, 11.34, 64.49470012280474]
keyFrame5075.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5075.ViewUp = [0.49428667953526234, -0.866, -0.07470415276190603]
keyFrame5075.ViewAngle = 30.0
keyFrame5075.ParallelScale = 0.97681
keyFrame5075.PositionPathPoints = [31.724616179657996, 11.34, 64.49470012280474]
keyFrame5075.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5075.PositionMode = 'Path'
keyFrame5075.FocalPointMode = 'Path'
keyFrame5075.ClosedFocalPath = 0
keyFrame5075.ClosedPositionPath = 0

# ====================================================================
keyFrame5076 = CameraKeyFrame()
keyFrame5076.KeyTime = 0.19
keyFrame5076.KeyValues = [0.0]
keyFrame5076.Position = [31.813592073274368, 11.34, 64.48116172215438]
keyFrame5076.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5076.ViewUp = [0.4941362824142006, -0.866, -0.07569257608038538]
keyFrame5076.ViewAngle = 30.0
keyFrame5076.ParallelScale = 0.97681
keyFrame5076.PositionPathPoints = [31.813592073274368, 11.34, 64.48116172215438]
keyFrame5076.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5076.PositionMode = 'Path'
keyFrame5076.FocalPointMode = 'Path'
keyFrame5076.ClosedFocalPath = 0
keyFrame5076.ClosedPositionPath = 0

# ====================================================================
keyFrame5077 = CameraKeyFrame()
keyFrame5077.KeyTime = 0.1925
keyFrame5077.KeyValues = [0.0]
keyFrame5077.Position = [31.902540714603465, 11.34, 64.4674454142503]
keyFrame5077.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5077.ViewUp = [0.4939839086386158, -0.866, -0.07668069663769159]
keyFrame5077.ViewAngle = 30.0
keyFrame5077.ParallelScale = 0.97681
keyFrame5077.PositionPathPoints = [31.902540714603465, 11.34, 64.4674454142503]
keyFrame5077.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5077.PositionMode = 'Path'
keyFrame5077.FocalPointMode = 'Path'
keyFrame5077.ClosedFocalPath = 0
keyFrame5077.ClosedPositionPath = 0

# ====================================================================
keyFrame5078 = CameraKeyFrame()
keyFrame5078.KeyTime = 0.195
keyFrame5078.KeyValues = [0.0]
keyFrame5078.Position = [31.991461746832474, 11.34, 64.45355124665261]
keyFrame5078.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5078.ViewUp = [0.4938295588233348, -0.866, -0.07766851048146206]
keyFrame5078.ViewAngle = 30.0
keyFrame5078.ParallelScale = 0.97681
keyFrame5078.PositionPathPoints = [31.991461746832474, 11.34, 64.45355124665261]
keyFrame5078.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5078.PositionMode = 'Path'
keyFrame5078.FocalPointMode = 'Path'
keyFrame5078.ClosedFocalPath = 0
keyFrame5078.ClosedPositionPath = 0

# ====================================================================
keyFrame5079 = CameraKeyFrame()
keyFrame5079.KeyTime = 0.1975
keyFrame5079.KeyValues = [0.0]
keyFrame5079.Position = [32.080354813243936, 11.34, 64.439479267635]
keyFrame5079.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5079.ViewUp = [0.4936732335924539, -0.866, -0.07865601366039507]
keyFrame5079.ViewAngle = 30.0
keyFrame5079.ParallelScale = 0.97681
keyFrame5079.PositionPathPoints = [32.080354813243936, 11.34, 64.439479267635]
keyFrame5079.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5079.PositionMode = 'Path'
keyFrame5079.FocalPointMode = 'Path'
keyFrame5079.ClosedFocalPath = 0
keyFrame5079.ClosedPositionPath = 0

# ====================================================================
keyFrame5080 = CameraKeyFrame()
keyFrame5080.KeyTime = 0.2
keyFrame5080.KeyValues = [0.0]
keyFrame5080.Position = [32.169219557215754, 11.34, 64.42522952618486]
keyFrame5080.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5080.ViewUp = [0.493514933579339, -0.866, -0.07964320222424985]
keyFrame5080.ViewAngle = 30.0
keyFrame5080.ParallelScale = 0.97681
keyFrame5080.PositionPathPoints = [32.169219557215754, 11.34, 64.42522952618486]
keyFrame5080.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5080.PositionMode = 'Path'
keyFrame5080.FocalPointMode = 'Path'
keyFrame5080.ClosedFocalPath = 0
keyFrame5080.ClosedPositionPath = 0

# ====================================================================
keyFrame5081 = CameraKeyFrame()
keyFrame5081.KeyTime = 0.2025
keyFrame5081.KeyValues = [0.0]
keyFrame5081.Position = [32.25805562222121, 11.34, 64.41080207200318]
keyFrame5081.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5081.ViewUp = [0.49335465942662526, -0.866, -0.08063007222384651]
keyFrame5081.ViewAngle = 30.0
keyFrame5081.ParallelScale = 0.97681
keyFrame5081.PositionPathPoints = [32.25805562222121, 11.34, 64.41080207200318]
keyFrame5081.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5081.PositionMode = 'Path'
keyFrame5081.FocalPointMode = 'Path'
keyFrame5081.ClosedFocalPath = 0
keyFrame5081.ClosedPositionPath = 0

# ====================================================================
keyFrame5082 = CameraKeyFrame()
keyFrame5082.KeyTime = 0.205
keyFrame5082.KeyValues = [0.0]
keyFrame5082.Position = [32.34686265192198, 11.34, 64.39619695607797]
keyFrame5082.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5082.ViewUp = [0.4931924117862173, -0.866, -0.08161661971106608]
keyFrame5082.ViewAngle = 30.0
keyFrame5082.ParallelScale = 0.97681
keyFrame5082.PositionPathPoints = [32.34686265192198, 11.34, 64.39619695607797]
keyFrame5082.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5082.PositionMode = 'Path'
keyFrame5082.FocalPointMode = 'Path'
keyFrame5082.ClosedFocalPath = 0
keyFrame5082.ClosedPositionPath = 0

# ====================================================================
keyFrame5083 = CameraKeyFrame()
keyFrame5083.KeyTime = 0.2075
keyFrame5083.KeyValues = [0.0]
keyFrame5083.Position = [32.43564029298398, 11.34, 64.3814142480318]
keyFrame5083.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5083.ViewUp = [0.49302819131928904, -0.866, -0.08260284073885049]
keyFrame5083.ViewAngle = 30.0
keyFrame5083.ParallelScale = 0.97681
keyFrame5083.PositionPathPoints = [32.43564029298398, 11.34, 64.3814142480318]
keyFrame5083.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5083.PositionMode = 'Path'
keyFrame5083.FocalPointMode = 'Path'
keyFrame5083.ClosedFocalPath = 0
keyFrame5083.ClosedPositionPath = 0

# ====================================================================
keyFrame5084 = CameraKeyFrame()
keyFrame5084.KeyTime = 0.21
keyFrame5084.KeyValues = [0.0]
keyFrame5084.Position = [32.52438819129746, 11.34, 64.36645401283457]
keyFrame5084.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5084.ViewUp = [0.49286199869628405, -0.866, -0.08358873136120262]
keyFrame5084.ViewAngle = 30.0
keyFrame5084.ParallelScale = 0.97681
keyFrame5084.PositionPathPoints = [32.52438819129746, 11.34, 64.36645401283457]
keyFrame5084.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5084.PositionMode = 'Path'
keyFrame5084.FocalPointMode = 'Path'
keyFrame5084.ClosedFocalPath = 0
keyFrame5084.ClosedPositionPath = 0

# ====================================================================
keyFrame5085 = CameraKeyFrame()
keyFrame5085.KeyTime = 0.2125
keyFrame5085.KeyValues = [0.0]
keyFrame5085.Position = [32.61310599170248, 11.34, 64.35131630911252]
keyFrame5085.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5085.ViewUp = [0.4926938345969151, -0.866, -0.0845742876331862]
keyFrame5085.ViewAngle = 30.0
keyFrame5085.ParallelScale = 0.97681
keyFrame5085.PositionPathPoints = [32.61310599170248, 11.34, 64.35131630911252]
keyFrame5085.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5085.PositionMode = 'Path'
keyFrame5085.FocalPointMode = 'Path'
keyFrame5085.ClosedFocalPath = 0
keyFrame5085.ClosedPositionPath = 0

# ====================================================================
keyFrame5086 = CameraKeyFrame()
keyFrame5086.KeyTime = 0.215
keyFrame5086.KeyValues = [0.0]
keyFrame5086.Position = [32.70179333919705, 11.34, 64.3360011965909]
keyFrame5086.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5086.ViewUp = [0.4925236997101645, -0.866, -0.08555950561092593]
keyFrame5086.ViewAngle = 30.0
keyFrame5086.ParallelScale = 0.97681
keyFrame5086.PositionPathPoints = [32.70179333919705, 11.34, 64.3360011965909]
keyFrame5086.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5086.PositionMode = 'Path'
keyFrame5086.FocalPointMode = 'Path'
keyFrame5086.ClosedFocalPath = 0
keyFrame5086.ClosedPositionPath = 0

# ====================================================================
keyFrame5087 = CameraKeyFrame()
keyFrame5087.KeyTime = 0.2175
keyFrame5087.KeyValues = [0.0]
keyFrame5087.Position = [32.790449878937096, 11.34, 64.32050873609397]
keyFrame5087.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5087.ViewUp = [0.49235159473428397, -0.866, -0.08654438135160739]
keyFrame5087.ViewAngle = 30.0
keyFrame5087.ParallelScale = 0.97681
keyFrame5087.PositionPathPoints = [32.790449878937096, 11.34, 64.32050873609397]
keyFrame5087.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5087.PositionMode = 'Path'
keyFrame5087.FocalPointMode = 'Path'
keyFrame5087.ClosedFocalPath = 0
keyFrame5087.ClosedPositionPath = 0

# ====================================================================
keyFrame5088 = CameraKeyFrame()
keyFrame5088.KeyTime = 0.22
keyFrame5088.KeyValues = [0.0]
keyFrame5088.Position = [32.87907525623643, 11.34, 64.304838989545]
keyFrame5088.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5088.ViewUp = [0.49217752037679463, -0.866, -0.08752891091347706]
keyFrame5088.ViewAngle = 30.0
keyFrame5088.ParallelScale = 0.97681
keyFrame5088.PositionPathPoints = [32.87907525623643, 11.34, 64.304838989545]
keyFrame5088.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5088.PositionMode = 'Path'
keyFrame5088.FocalPointMode = 'Path'
keyFrame5088.ClosedFocalPath = 0
keyFrame5088.ClosedPositionPath = 0

# ====================================================================
keyFrame5089 = CameraKeyFrame()
keyFrame5089.KeyTime = 0.2225
keyFrame5089.KeyValues = [0.0]
keyFrame5089.Position = [32.96766911656681, 11.34, 64.28899201996629]
keyFrame5089.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5089.ViewUp = [0.4920014773544869, -0.866, -0.08851309035584237]
keyFrame5089.ViewAngle = 30.0
keyFrame5089.ParallelScale = 0.97681
keyFrame5089.PositionPathPoints = [32.96766911656681, 11.34, 64.28899201996629]
keyFrame5089.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5089.PositionMode = 'Path'
keyFrame5089.FocalPointMode = 'Path'
keyFrame5089.ClosedFocalPath = 0
keyFrame5089.ClosedPositionPath = 0

# ====================================================================
keyFrame5090 = CameraKeyFrame()
keyFrame5090.KeyTime = 0.225
keyFrame5090.KeyValues = [0.0]
keyFrame5090.Position = [33.056231105557885, 11.34, 64.27296789147913]
keyFrame5090.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5090.ViewUp = [0.49182346639342084, -0.866, -0.08949691573907162]
keyFrame5090.ViewAngle = 30.0
keyFrame5090.ParallelScale = 0.97681
keyFrame5090.PositionPathPoints = [33.056231105557885, 11.34, 64.27296789147913]
keyFrame5090.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5090.PositionMode = 'Path'
keyFrame5090.FocalPointMode = 'Path'
keyFrame5090.ClosedFocalPath = 0
keyFrame5090.ClosedPositionPath = 0

# ====================================================================
keyFrame5091 = CameraKeyFrame()
keyFrame5091.KeyTime = 0.2275
keyFrame5091.KeyValues = [0.0]
keyFrame5091.Position = [33.14476086899724, 11.34, 64.25676666930386]
keyFrame5091.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5091.ViewUp = [0.49164348822892573, -0.866, -0.09048038312459407]
keyFrame5091.ViewAngle = 30.0
keyFrame5091.ParallelScale = 0.97681
keyFrame5091.PositionPathPoints = [33.14476086899724, 11.34, 64.25676666930386]
keyFrame5091.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5091.PositionMode = 'Path'
keyFrame5091.FocalPointMode = 'Path'
keyFrame5091.ClosedFocalPath = 0
keyFrame5091.ClosedPositionPath = 0

# ====================================================================
keyFrame5092 = CameraKeyFrame()
keyFrame5092.KeyTime = 0.23
keyFrame5092.KeyValues = [0.0]
keyFrame5092.Position = [33.233258052830365, 11.34, 64.2403884197598]
keyFrame5092.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5092.ViewUp = [0.4914615436056004, -0.866, -0.09146348857489982]
keyFrame5092.ViewAngle = 30.0
keyFrame5092.ParallelScale = 0.97681
keyFrame5092.PositionPathPoints = [33.233258052830365, 11.34, 64.2403884197598]
keyFrame5092.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5092.PositionMode = 'Path'
keyFrame5092.FocalPointMode = 'Path'
keyFrame5092.ClosedFocalPath = 0
keyFrame5092.ClosedPositionPath = 0

# ====================================================================
keyFrame5093 = CameraKeyFrame()
keyFrame5093.KeyTime = 0.2325
keyFrame5093.KeyValues = [0.0]
keyFrame5093.Position = [33.321722303160655, 11.34, 64.22383321026533]
keyFrame5093.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5093.ViewUp = [0.491277633277313, -0.866, -0.09244622815353995]
keyFrame5093.ViewAngle = 30.0
keyFrame5093.ParallelScale = 0.97681
keyFrame5093.PositionPathPoints = [33.321722303160655, 11.34, 64.22383321026533]
keyFrame5093.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5093.PositionMode = 'Path'
keyFrame5093.FocalPointMode = 'Path'
keyFrame5093.ClosedFocalPath = 0
keyFrame5093.ClosedPositionPath = 0

# ====================================================================
keyFrame5094 = CameraKeyFrame()
keyFrame5094.KeyTime = 0.235
keyFrame5094.KeyValues = [0.0]
keyFrame5094.Position = [33.41015326624944, 11.34, 64.2071011093378]
keyFrame5094.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5094.ViewUp = [0.4910917580072012, -0.866, -0.09342859792512641]
keyFrame5094.ViewAngle = 30.0
keyFrame5094.ParallelScale = 0.97681
keyFrame5094.PositionPathPoints = [33.41015326624944, 11.34, 64.2071011093378]
keyFrame5094.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5094.PositionMode = 'Path'
keyFrame5094.FocalPointMode = 'Path'
keyFrame5094.ClosedFocalPath = 0
keyFrame5094.ClosedPositionPath = 0

# ====================================================================
keyFrame5095 = CameraKeyFrame()
keyFrame5095.KeyTime = 0.2375
keyFrame5095.KeyValues = [0.0]
keyFrame5095.Position = [33.49855058851594, 11.34, 64.1901921865936]
keyFrame5095.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5095.ViewUp = [0.49090391856767196, -0.866, -0.09441059395533208]
keyFrame5095.ViewAngle = 30.0
keyFrame5095.ParallelScale = 0.97681
keyFrame5095.PositionPathPoints = [33.49855058851594, 11.34, 64.1901921865936]
keyFrame5095.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5095.PositionMode = 'Path'
keyFrame5095.FocalPointMode = 'Path'
keyFrame5095.ClosedFocalPath = 0
keyFrame5095.ClosedPositionPath = 0

# ====================================================================
keyFrame5096 = CameraKeyFrame()
keyFrame5096.KeyTime = 0.24
keyFrame5096.KeyValues = [0.0]
keyFrame5096.Position = [33.586913916525525, 11.34, 64.17310651250133]
keyFrame5096.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5096.ViewUp = [0.49071411568130807, -0.866, -0.09539221232283793]
keyFrame5096.ViewAngle = 30.0
keyFrame5096.ParallelScale = 0.97681
keyFrame5096.PositionPathPoints = [33.586913916525525, 11.34, 64.17310651250133]
keyFrame5096.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5096.PositionMode = 'Path'
keyFrame5096.FocalPointMode = 'Path'
keyFrame5096.ClosedFocalPath = 0
keyFrame5096.ClosedPositionPath = 0

# ====================================================================
keyFrame5097 = CameraKeyFrame()
keyFrame5097.KeyTime = 0.2425
keyFrame5097.KeyValues = [0.0]
keyFrame5097.Position = [33.67524289644895, 11.34, 64.15584414707916]
keyFrame5097.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5097.ViewUp = [0.49052234994692545, -0.866, -0.09637344913428213]
keyFrame5097.ViewAngle = 30.0
keyFrame5097.ParallelScale = 0.97681
keyFrame5097.PositionPathPoints = [33.67524289644895, 11.34, 64.15584414707916]
keyFrame5097.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5097.PositionMode = 'Path'
keyFrame5097.FocalPointMode = 'Path'
keyFrame5097.ClosedFocalPath = 0
keyFrame5097.ClosedPositionPath = 0

# ====================================================================
keyFrame5098 = CameraKeyFrame()
keyFrame5098.KeyTime = 0.245
keyFrame5098.KeyValues = [0.0]
keyFrame5098.Position = [33.763537174736456, 11.34, 64.13840515398502]
keyFrame5098.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5098.ViewUp = [0.49032862212019596, -0.866, -0.0973543004675258]
keyFrame5098.ViewAngle = 30.0
keyFrame5098.ParallelScale = 0.97681
keyFrame5098.PositionPathPoints = [33.763537174736456, 11.34, 64.13840515398502]
keyFrame5098.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5098.PositionMode = 'Path'
keyFrame5098.FocalPointMode = 'Path'
keyFrame5098.ClosedFocalPath = 0
keyFrame5098.ClosedPositionPath = 0

# ====================================================================
keyFrame5099 = CameraKeyFrame()
keyFrame5099.KeyTime = 0.2475
keyFrame5099.KeyValues = [0.0]
keyFrame5099.Position = [33.85179639824585, 11.34, 64.1207896031955]
keyFrame5099.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5099.ViewUp = [0.49013293297600524, -0.866, -0.0983347623994805]
keyFrame5099.ViewAngle = 30.0
keyFrame5099.ParallelScale = 0.97681
keyFrame5099.PositionPathPoints = [33.85179639824585, 11.34, 64.1207896031955]
keyFrame5099.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5099.PositionMode = 'Path'
keyFrame5099.FocalPointMode = 'Path'
keyFrame5099.ClosedFocalPath = 0
keyFrame5099.ClosedPositionPath = 0

# ====================================================================
keyFrame5100 = CameraKeyFrame()
keyFrame5100.KeyTime = 0.25
keyFrame5100.KeyValues = [0.0]
keyFrame5100.Position = [33.94002021398063, 11.34, 64.10299756552942]
keyFrame5100.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5100.ViewUp = [0.48993528329712577, -0.866, -0.09931483100839814]
keyFrame5100.ViewAngle = 30.0
keyFrame5100.ParallelScale = 0.97681
keyFrame5100.PositionPathPoints = [33.94002021398063, 11.34, 64.10299756552942]
keyFrame5100.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5100.PositionMode = 'Path'
keyFrame5100.FocalPointMode = 'Path'
keyFrame5100.ClosedFocalPath = 0
keyFrame5100.ClosedPositionPath = 0

# ====================================================================
keyFrame5101 = CameraKeyFrame()
keyFrame5101.KeyTime = 0.2525
keyFrame5101.KeyValues = [0.0]
keyFrame5101.Position = [34.02820826908987, 11.34, 64.08502911264767]
keyFrame5101.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5101.ViewUp = [0.48973567387421674, -0.866, -0.10029450237387112]
keyFrame5101.ViewAngle = 30.0
keyFrame5101.ParallelScale = 0.97681
keyFrame5101.PositionPathPoints = [34.02820826908987, 11.34, 64.08502911264767]
keyFrame5101.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5101.PositionMode = 'Path'
keyFrame5101.FocalPointMode = 'Path'
keyFrame5101.ClosedFocalPath = 0
keyFrame5101.ClosedPositionPath = 0

# ====================================================================
keyFrame5102 = CameraKeyFrame()
keyFrame5102.KeyTime = 0.255
keyFrame5102.KeyValues = [0.0]
keyFrame5102.Position = [34.11636021086829, 11.34, 64.06688431705334]
keyFrame5102.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5102.ViewUp = [0.48953410550582444, -0.866, -0.10127377257683229]
keyFrame5102.ViewAngle = 30.0
keyFrame5102.ParallelScale = 0.97681
keyFrame5102.PositionPathPoints = [34.11636021086829, 11.34, 64.06688431705334]
keyFrame5102.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5102.PositionMode = 'Path'
keyFrame5102.FocalPointMode = 'Path'
keyFrame5102.ClosedFocalPath = 0
keyFrame5102.ClosedPositionPath = 0

# ====================================================================
keyFrame5103 = CameraKeyFrame()
keyFrame5103.KeyTime = 0.2575
keyFrame5103.KeyValues = [0.0]
keyFrame5103.Position = [34.204475686756226, 11.34, 64.04856325209161]
keyFrame5103.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5103.ViewUp = [0.4893305789983817, -0.866, -0.10225263769955484]
keyFrame5103.ViewAngle = 30.0
keyFrame5103.ParallelScale = 0.97681
keyFrame5103.PositionPathPoints = [34.204475686756226, 11.34, 64.04856325209161]
keyFrame5103.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5103.PositionMode = 'Path'
keyFrame5103.FocalPointMode = 'Path'
keyFrame5103.ClosedFocalPath = 0
keyFrame5103.ClosedPositionPath = 0

# ====================================================================
keyFrame5104 = CameraKeyFrame()
keyFrame5104.KeyTime = 0.26
keyFrame5104.KeyValues = [0.0]
keyFrame5104.Position = [34.29255434433966, 11.34, 64.03006599194984]
keyFrame5104.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5104.ViewUp = [0.48912509516620856, -0.866, -0.10323109382565249]
keyFrame5104.ViewAngle = 30.0
keyFrame5104.ParallelScale = 0.97681
keyFrame5104.PositionPathPoints = [34.29255434433966, 11.34, 64.03006599194984]
keyFrame5104.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5104.PositionMode = 'Path'
keyFrame5104.FocalPointMode = 'Path'
keyFrame5104.ClosedFocalPath = 0
keyFrame5104.ClosedPositionPath = 0

# ====================================================================
keyFrame5105 = CameraKeyFrame()
keyFrame5105.KeyTime = 0.2625
keyFrame5105.KeyValues = [0.0]
keyFrame5105.Position = [34.38059583135019, 11.34, 64.01139261165753]
keyFrame5105.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5105.ViewUp = [0.4889176548315116, -0.866, -0.1042091370400793]
keyFrame5105.ViewAngle = 30.0
keyFrame5105.ParallelScale = 0.97681
keyFrame5105.PositionPathPoints = [34.38059583135019, 11.34, 64.01139261165753]
keyFrame5105.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5105.PositionMode = 'Path'
keyFrame5105.FocalPointMode = 'Path'
keyFrame5105.ClosedFocalPath = 0
keyFrame5105.ClosedPositionPath = 0

# ====================================================================
keyFrame5106 = CameraKeyFrame()
keyFrame5106.KeyTime = 0.265
keyFrame5106.KeyValues = [0.0]
keyFrame5106.Position = [34.46859979566506, 11.34, 63.99254318708627]
keyFrame5106.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5106.ViewUp = [0.48870825882438446, -0.866, -0.10518676342912985]
keyFrame5106.ViewAngle = 30.0
keyFrame5106.ParallelScale = 0.97681
keyFrame5106.PositionPathPoints = [34.46859979566506, 11.34, 63.99254318708627]
keyFrame5106.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5106.PositionMode = 'Path'
keyFrame5106.FocalPointMode = 'Path'
keyFrame5106.ClosedFocalPath = 0
keyFrame5106.ClosedPositionPath = 0

# ====================================================================
keyFrame5107 = CameraKeyFrame()
keyFrame5107.KeyTime = 0.2675
keyFrame5107.KeyValues = [0.0]
keyFrame5107.Position = [34.55656588530708, 11.34, 63.973517794949856]
keyFrame5107.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5107.ViewUp = [0.4884969079828075, -0.866, -0.10616396908043906]
keyFrame5107.ViewAngle = 30.0
keyFrame5107.ParallelScale = 0.97681
keyFrame5107.PositionPathPoints = [34.55656588530708, 11.34, 63.973517794949856]
keyFrame5107.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5107.PositionMode = 'Path'
keyFrame5107.FocalPointMode = 'Path'
keyFrame5107.ClosedFocalPath = 0
keyFrame5107.ClosedPositionPath = 0

# ====================================================================
keyFrame5108 = CameraKeyFrame()
keyFrame5108.KeyTime = 0.27
keyFrame5108.KeyValues = [0.0]
keyFrame5108.Position = [34.64449374844477, 11.34, 63.95431651280419]
keyFrame5108.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5108.ViewUp = [0.48828360315264796, -0.866, -0.10714075008298234]
keyFrame5108.ViewAngle = 30.0
keyFrame5108.ParallelScale = 0.97681
keyFrame5108.PositionPathPoints = [34.64449374844477, 11.34, 63.95431651280419]
keyFrame5108.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5108.PositionMode = 'Path'
keyFrame5108.FocalPointMode = 'Path'
keyFrame5108.ClosedFocalPath = 0
keyFrame5108.ClosedPositionPath = 0

# ====================================================================
keyFrame5109 = CameraKeyFrame()
keyFrame5109.KeyTime = 0.2725
keyFrame5109.KeyValues = [0.0]
keyFrame5109.Position = [34.732383033392225, 11.34, 63.934939419047325]
keyFrame5109.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5109.ViewUp = [0.48806834518765996, -0.866, -0.10811710252707549]
keyFrame5109.ViewAngle = 30.0
keyFrame5109.ParallelScale = 0.97681
keyFrame5109.PositionPathPoints = [34.732383033392225, 11.34, 63.934939419047325]
keyFrame5109.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5109.PositionMode = 'Path'
keyFrame5109.FocalPointMode = 'Path'
keyFrame5109.ClosedFocalPath = 0
keyFrame5109.ClosedPositionPath = 0

# ====================================================================
keyFrame5110 = CameraKeyFrame()
keyFrame5110.KeyTime = 0.275
keyFrame5110.KeyValues = [0.0]
keyFrame5110.Position = [34.82023338861006, 11.34, 63.91538659284404]
keyFrame5110.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5110.ViewUp = [0.4878511349494845, -0.866, -0.10909302250437478]
keyFrame5110.ViewAngle = 30.0
keyFrame5110.ParallelScale = 0.97681
keyFrame5110.PositionPathPoints = [34.82023338861006, 11.34, 63.91538659284404]
keyFrame5110.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5110.PositionMode = 'Path'
keyFrame5110.FocalPointMode = 'Path'
keyFrame5110.ClosedFocalPath = 0
keyFrame5110.ClosedPositionPath = 0

# ====================================================================
keyFrame5111 = CameraKeyFrame()
keyFrame5111.KeyTime = 0.2775
keyFrame5111.KeyValues = [0.0]
keyFrame5111.Position = [34.90804446277404, 11.34, 63.89565810828641]
keyFrame5111.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5111.ViewUp = [0.48763197330764935, -0.866, -0.11006850610787687]
keyFrame5111.ViewAngle = 30.0
keyFrame5111.ParallelScale = 0.97681
keyFrame5111.PositionPathPoints = [34.90804446277404, 11.34, 63.89565810828641]
keyFrame5111.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5111.PositionMode = 'Path'
keyFrame5111.FocalPointMode = 'Path'
keyFrame5111.ClosedFocalPath = 0
keyFrame5111.ClosedPositionPath = 0

# ====================================================================
keyFrame5112 = CameraKeyFrame()
keyFrame5112.KeyTime = 0.28
keyFrame5112.KeyValues = [0.0]
keyFrame5112.Position = [34.995815904696585, 11.34, 63.87575404107145]
keyFrame5112.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5112.ViewUp = [0.48741086113956916, -0.866, -0.11104354943191888]
keyFrame5112.ViewAngle = 30.0
keyFrame5112.ParallelScale = 0.97681
keyFrame5112.PositionPathPoints = [34.995815904696585, 11.34, 63.87575404107145]
keyFrame5112.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5112.PositionMode = 'Path'
keyFrame5112.FocalPointMode = 'Path'
keyFrame5112.ClosedFocalPath = 0
keyFrame5112.ClosedPositionPath = 0

# ====================================================================
keyFrame5113 = CameraKeyFrame()
keyFrame5113.KeyTime = 0.2825
keyFrame5113.KeyValues = [0.0]
keyFrame5113.Position = [35.08354736329959, 11.34, 63.85567447081524]
keyFrame5113.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5113.ViewUp = [0.4871877993305455, -0.866, -0.11201814857217832]
keyFrame5113.ViewAngle = 30.0
keyFrame5113.ParallelScale = 0.97681
keyFrame5113.PositionPathPoints = [35.08354736329959, 11.34, 63.85567447081524]
keyFrame5113.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5113.PositionMode = 'Path'
keyFrame5113.FocalPointMode = 'Path'
keyFrame5113.ClosedFocalPath = 0
keyFrame5113.ClosedPositionPath = 0

# ====================================================================
keyFrame5114 = CameraKeyFrame()
keyFrame5114.KeyTime = 0.285
keyFrame5114.KeyValues = [0.0]
keyFrame5114.Position = [35.17123848765216, 11.34, 63.83541947783875]
keyFrame5114.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5114.ViewUp = [0.4869627887737667, -0.866, -0.11299229962567317]
keyFrame5114.ViewAngle = 30.0
keyFrame5114.ParallelScale = 0.97681
keyFrame5114.PositionPathPoints = [35.17123848765216, 11.34, 63.83541947783875]
keyFrame5114.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5114.PositionMode = 'Path'
keyFrame5114.FocalPointMode = 'Path'
keyFrame5114.ClosedFocalPath = 0
keyFrame5114.ClosedPositionPath = 0

# ====================================================================
keyFrame5115 = CameraKeyFrame()
keyFrame5115.KeyTime = 0.2875
keyFrame5115.KeyValues = [0.0]
keyFrame5115.Position = [35.258888926970684, 11.34, 63.81498914316787]
keyFrame5115.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5115.ViewUp = [0.48673583037030793, -0.866, -0.11396599869076181]
keyFrame5115.ViewAngle = 30.0
keyFrame5115.ParallelScale = 0.97681
keyFrame5115.PositionPathPoints = [35.258888926970684, 11.34, 63.81498914316787]
keyFrame5115.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5115.PositionMode = 'Path'
keyFrame5115.FocalPointMode = 'Path'
keyFrame5115.ClosedFocalPath = 0
keyFrame5115.ClosedPositionPath = 0

# ====================================================================
keyFrame5116 = CameraKeyFrame()
keyFrame5116.KeyTime = 0.29
keyFrame5116.KeyValues = [0.0]
keyFrame5116.Position = [35.34649833061877, 11.34, 63.79438354853338]
keyFrame5116.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5116.ViewUp = [0.4865069250291313, -0.866, -0.11493924186714308]
keyFrame5116.ViewAngle = 30.0
keyFrame5116.ParallelScale = 0.97681
keyFrame5116.PositionPathPoints = [35.34649833061877, 11.34, 63.79438354853338]
keyFrame5116.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5116.PositionMode = 'Path'
keyFrame5116.FocalPointMode = 'Path'
keyFrame5116.ClosedFocalPath = 0
keyFrame5116.ClosedPositionPath = 0

# ====================================================================
keyFrame5117 = CameraKeyFrame()
keyFrame5117.KeyTime = 0.2925
keyFrame5117.KeyValues = [0.0]
keyFrame5117.Position = [35.434066348107265, 11.34, 63.77360277637097]
keyFrame5117.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5117.ViewUp = [0.4862760736670857, -0.866, -0.1159120252558562]
keyFrame5117.ViewAngle = 30.0
keyFrame5117.ParallelScale = 0.97681
keyFrame5117.PositionPathPoints = [35.434066348107265, 11.34, 63.77360277637097]
keyFrame5117.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5117.PositionMode = 'Path'
keyFrame5117.FocalPointMode = 'Path'
keyFrame5117.ClosedFocalPath = 0
keyFrame5117.ClosedPositionPath = 0

# ====================================================================
keyFrame5118 = CameraKeyFrame()
keyFrame5118.KeyTime = 0.295
keyFrame5118.KeyValues = [0.0]
keyFrame5118.Position = [35.52159262909424, 11.34, 63.75264690982124]
keyFrame5118.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5118.ViewUp = [0.48604327720890694, -0.866, -0.11688434495928086]
keyFrame5118.ViewAngle = 30.0
keyFrame5118.ParallelScale = 0.97681
keyFrame5118.PositionPathPoints = [35.52159262909424, 11.34, 63.75264690982124]
keyFrame5118.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5118.PositionMode = 'Path'
keyFrame5118.FocalPointMode = 'Path'
keyFrame5118.ClosedFocalPath = 0
keyFrame5118.ClosedPositionPath = 0

# ====================================================================
keyFrame5119 = CameraKeyFrame()
keyFrame5119.KeyTime = 0.2975
keyFrame5119.KeyValues = [0.0]
keyFrame5119.Position = [35.60907682338505, 11.34, 63.73151603272966]
keyFrame5119.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5119.ViewUp = [0.48580853658240397, -0.866, -0.11785619710435885]
keyFrame5119.ViewAngle = 30.0
keyFrame5119.ParallelScale = 0.97681
keyFrame5119.PositionPathPoints = [35.60907682338505, 11.34, 63.73151603272966]
keyFrame5119.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5119.PositionMode = 'Path'
keyFrame5119.FocalPointMode = 'Path'
keyFrame5119.ClosedFocalPath = 0
keyFrame5119.ClosedPositionPath = 0

# ====================================================================
keyFrame5120 = CameraKeyFrame()
keyFrame5120.KeyTime = 0.3
keyFrame5120.KeyValues = [0.0]
keyFrame5120.Position = [35.69651858093225, 11.34, 63.71021022964663]
keyFrame5120.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5120.ViewUp = [0.4855718527189277, -0.866, -0.11882757784033317]
keyFrame5120.ViewAngle = 30.0
keyFrame5120.ParallelScale = 0.97681
keyFrame5120.PositionPathPoints = [35.69651858093225, 11.34, 63.71021022964663]
keyFrame5120.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5120.PositionMode = 'Path'
keyFrame5120.FocalPointMode = 'Path'
keyFrame5120.ClosedFocalPath = 0
keyFrame5120.ClosedPositionPath = 0

# ====================================================================
keyFrame5121 = CameraKeyFrame()
keyFrame5121.KeyTime = 0.3025
keyFrame5121.KeyValues = [0.0]
keyFrame5121.Position = [35.78391755183564, 11.34, 63.688729585827446]
keyFrame5121.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5121.ViewUp = [0.4853332265649849, -0.866, -0.11979848328272055]
keyFrame5121.ViewAngle = 30.0
keyFrame5121.ParallelScale = 0.97681
keyFrame5121.PositionPathPoints = [35.78391755183564, 11.34, 63.688729585827446]
keyFrame5121.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5121.PositionMode = 'Path'
keyFrame5121.FocalPointMode = 'Path'
keyFrame5121.ClosedFocalPath = 0
keyFrame5121.ClosedPositionPath = 0

# ====================================================================
keyFrame5122 = CameraKeyFrame()
keyFrame5122.KeyTime = 0.305
keyFrame5122.KeyValues = [0.0]
keyFrame5122.Position = [35.87127338634228, 11.34, 63.66707418723231]
keyFrame5122.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5122.ViewUp = [0.48509265907502574, -0.866, -0.12076890954810453]
keyFrame5122.ViewAngle = 30.0
keyFrame5122.ParallelScale = 0.97681
keyFrame5122.PositionPathPoints = [35.87127338634228, 11.34, 63.66707418723231]
keyFrame5122.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5122.PositionMode = 'Path'
keyFrame5122.FocalPointMode = 'Path'
keyFrame5122.ClosedFocalPath = 0
keyFrame5122.ClosedPositionPath = 0

# ====================================================================
keyFrame5123 = CameraKeyFrame()
keyFrame5123.KeyTime = 0.3075
keyFrame5123.KeyValues = [0.0]
keyFrame5123.Position = [35.958585734846466, 11.34, 63.64524412052631]
keyFrame5123.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5123.ViewUp = [0.48485015121131464, -0.866, -0.12173885275476011]
keyFrame5123.ViewAngle = 30.0
keyFrame5123.ParallelScale = 0.97681
keyFrame5123.PositionPathPoints = [35.958585734846466, 11.34, 63.64524412052631]
keyFrame5123.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5123.PositionMode = 'Path'
keyFrame5123.FocalPointMode = 'Path'
keyFrame5123.ClosedFocalPath = 0
keyFrame5123.ClosedPositionPath = 0

# ====================================================================
keyFrame5124 = CameraKeyFrame()
keyFrame5124.KeyTime = 0.31
keyFrame5124.KeyValues = [0.0]
keyFrame5124.Position = [36.04585424789461, 11.34, 63.62323947307827]
keyFrame5124.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5124.ViewUp = [0.4846057039439301, -0.866, -0.12270830902265374]
keyFrame5124.ViewAngle = 30.0
keyFrame5124.ParallelScale = 0.97681
keyFrame5124.PositionPathPoints = [36.04585424789461, 11.34, 63.62323947307827]
keyFrame5124.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5124.PositionMode = 'Path'
keyFrame5124.FocalPointMode = 'Path'
keyFrame5124.ClosedFocalPath = 0
keyFrame5124.ClosedPositionPath = 0

# ====================================================================
keyFrame5125 = CameraKeyFrame()
keyFrame5125.KeyTime = 0.3125
keyFrame5125.KeyValues = [0.0]
keyFrame5125.Position = [36.133078576973176, 11.34, 63.6010603327728]
keyFrame5125.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5125.ViewUp = [0.48435931825076456, -0.866, -0.12367727447344327]
keyFrame5125.ViewAngle = 30.0
keyFrame5125.ParallelScale = 0.97681
keyFrame5125.PositionPathPoints = [36.133078576973176, 11.34, 63.6010603327728]
keyFrame5125.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5125.PositionMode = 'Path'
keyFrame5125.FocalPointMode = 'Path'
keyFrame5125.ClosedFocalPath = 0
keyFrame5125.ClosedPositionPath = 0

# ====================================================================
keyFrame5126 = CameraKeyFrame()
keyFrame5126.KeyTime = 0.315
keyFrame5126.KeyValues = [0.0]
keyFrame5126.Position = [36.22025837369789, 11.34, 63.5787067882037]
keyFrame5126.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5126.ViewUp = [0.48411099511752476, -0.866, -0.12464574523047803]
keyFrame5126.ViewAngle = 30.0
keyFrame5126.ParallelScale = 0.97681
keyFrame5126.PositionPathPoints = [36.22025837369789, 11.34, 63.5787067882037]
keyFrame5126.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5126.PositionMode = 'Path'
keyFrame5126.FocalPointMode = 'Path'
keyFrame5126.ClosedFocalPath = 0
keyFrame5126.ClosedPositionPath = 0

# ====================================================================
keyFrame5127 = CameraKeyFrame()
keyFrame5127.KeyTime = 0.3175
keyFrame5127.KeyValues = [0.0]
keyFrame5127.Position = [36.307393289354806, 11.34, 63.5561789287834]
keyFrame5127.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5127.ViewUp = [0.4838607355377314, -0.866, -0.12561371741879876]
keyFrame5127.ViewAngle = 30.0
keyFrame5127.ParallelScale = 0.97681
keyFrame5127.PositionPathPoints = [36.307393289354806, 11.34, 63.5561789287834]
keyFrame5127.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5127.PositionMode = 'Path'
keyFrame5127.FocalPointMode = 'Path'
keyFrame5127.ClosedFocalPath = 0
keyFrame5127.ClosedPositionPath = 0

# ====================================================================
keyFrame5128 = CameraKeyFrame()
keyFrame5128.KeyTime = 0.32
keyFrame5128.KeyValues = [0.0]
keyFrame5128.Position = [36.39448297539661, 11.34, 63.53347684462467]
keyFrame5128.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5128.ViewUp = [0.4836085405127193, -0.866, -0.1265811871651376]
keyFrame5128.ViewAngle = 30.0
keyFrame5128.ParallelScale = 0.97681
keyFrame5128.PositionPathPoints = [36.39448297539661, 11.34, 63.53347684462467]
keyFrame5128.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5128.PositionMode = 'Path'
keyFrame5128.FocalPointMode = 'Path'
keyFrame5128.ClosedFocalPath = 0
keyFrame5128.ClosedPositionPath = 0

# ====================================================================
keyFrame5129 = CameraKeyFrame()
keyFrame5129.KeyTime = 0.3225
keyFrame5129.KeyValues = [0.0]
keyFrame5129.Position = [36.481527083442614, 11.34, 63.51060062654052]
keyFrame5129.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5129.ViewUp = [0.4833544110516373, -0.866, -0.12754815059791821]
keyFrame5129.ViewAngle = 30.0
keyFrame5129.ParallelScale = 0.97681
keyFrame5129.PositionPathPoints = [36.481527083442614, 11.34, 63.51060062654052]
keyFrame5129.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5129.PositionMode = 'Path'
keyFrame5129.FocalPointMode = 'Path'
keyFrame5129.ClosedFocalPath = 0
keyFrame5129.ClosedPositionPath = 0

# ====================================================================
keyFrame5130 = CameraKeyFrame()
keyFrame5130.KeyTime = 0.325
keyFrame5130.KeyValues = [0.0]
keyFrame5130.Position = [36.56852526527872, 11.34, 63.48755036604425]
keyFrame5130.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5130.ViewUp = [0.48309834817144853, -0.866, -0.12851460384725566]
keyFrame5130.ViewAngle = 30.0
keyFrame5130.ParallelScale = 0.97681
keyFrame5130.PositionPathPoints = [36.56852526527872, 11.34, 63.48755036604425]
keyFrame5130.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5130.PositionMode = 'Path'
keyFrame5130.FocalPointMode = 'Path'
keyFrame5130.ClosedFocalPath = 0
keyFrame5130.ClosedPositionPath = 0

# ====================================================================
keyFrame5131 = CameraKeyFrame()
keyFrame5131.KeyTime = 0.3275
keyFrame5131.KeyValues = [0.0]
keyFrame5131.Position = [36.65547717285747, 11.34, 63.46432615534944]
keyFrame5131.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5131.ViewUp = [0.48284035289693, -0.866, -0.12948054304495638]
keyFrame5131.ViewAngle = 30.0
keyFrame5131.ParallelScale = 0.97681
keyFrame5131.PositionPathPoints = [36.65547717285747, 11.34, 63.46432615534944]
keyFrame5131.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5131.PositionMode = 'Path'
keyFrame5131.FocalPointMode = 'Path'
keyFrame5131.ClosedFocalPath = 0
keyFrame5131.ClosedPositionPath = 0

# ====================================================================
keyFrame5132 = CameraKeyFrame()
keyFrame5132.KeyTime = 0.33
keyFrame5132.KeyValues = [0.0]
keyFrame5132.Position = [36.74238245829801, 11.34, 63.44092808736995]
keyFrame5132.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5132.ViewUp = [0.4825804262606729, -0.866, -0.1304459643245183]
keyFrame5132.ViewAngle = 30.0
keyFrame5132.ParallelScale = 0.97681
keyFrame5132.PositionPathPoints = [36.74238245829801, 11.34, 63.44092808736995]
keyFrame5132.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5132.PositionMode = 'Path'
keyFrame5132.FocalPointMode = 'Path'
keyFrame5132.ClosedFocalPath = 0
keyFrame5132.ClosedPositionPath = 0

# ====================================================================
keyFrame5133 = CameraKeyFrame()
keyFrame5133.KeyTime = 0.3325
keyFrame5133.KeyValues = [0.0]
keyFrame5133.Position = [36.829240773886106, 11.34, 63.4173562557199]
keyFrame5133.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5133.ViewUp = [0.4823185693030825, -0.866, -0.1314108638211308]
keyFrame5133.ViewAngle = 30.0
keyFrame5133.ParallelScale = 0.97681
keyFrame5133.PositionPathPoints = [36.829240773886106, 11.34, 63.4173562557199]
keyFrame5133.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5133.PositionMode = 'Path'
keyFrame5133.FocalPointMode = 'Path'
keyFrame5133.ClosedFocalPath = 0
keyFrame5133.ClosedPositionPath = 0

# ====================================================================
keyFrame5134 = CameraKeyFrame()
keyFrame5134.KeyTime = 0.335
keyFrame5134.KeyValues = [0.0]
keyFrame5134.Position = [36.916051772074134, 11.34, 63.393610754713734]
keyFrame5134.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5134.ViewUp = [0.4820547830723782, -0.866, -0.13237523767167467]
keyFrame5134.ViewAngle = 30.0
keyFrame5134.ParallelScale = 0.97681
keyFrame5134.PositionPathPoints = [36.916051772074134, 11.34, 63.393610754713734]
keyFrame5134.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5134.PositionMode = 'Path'
keyFrame5134.FocalPointMode = 'Path'
keyFrame5134.ClosedFocalPath = 0
keyFrame5134.ClosedPositionPath = 0

# ====================================================================
keyFrame5135 = CameraKeyFrame()
keyFrame5135.KeyTime = 0.3375
keyFrame5135.KeyValues = [0.0]
keyFrame5135.Position = [37.00281510548109, 11.34, 63.369691679366134]
keyFrame5135.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5135.ViewUp = [0.4817890686245934, -0.866, -0.13333908201472214]
keyFrame5135.ViewAngle = 30.0
keyFrame5135.ParallelScale = 0.97681
keyFrame5135.PositionPathPoints = [37.00281510548109, 11.34, 63.369691679366134]
keyFrame5135.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5135.PositionMode = 'Path'
keyFrame5135.FocalPointMode = 'Path'
keyFrame5135.ClosedFocalPath = 0
keyFrame5135.ClosedPositionPath = 0

# ====================================================================
keyFrame5136 = CameraKeyFrame()
keyFrame5136.KeyTime = 0.34
keyFrame5136.KeyValues = [0.0]
keyFrame5136.Position = [37.089530426892594, 11.34, 63.345599125392084]
keyFrame5136.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5136.ViewUp = [0.4815214270235757, -0.866, -0.1343023929905369]
keyFrame5136.ViewAngle = 30.0
keyFrame5136.ParallelScale = 0.97681
keyFrame5136.PositionPathPoints = [37.089530426892594, 11.34, 63.345599125392084]
keyFrame5136.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5136.PositionMode = 'Path'
keyFrame5136.FocalPointMode = 'Path'
keyFrame5136.ClosedFocalPath = 0
keyFrame5136.ClosedPositionPath = 0

# ====================================================================
keyFrame5137 = CameraKeyFrame()
keyFrame5137.KeyTime = 0.3425
keyFrame5137.KeyValues = [0.0]
keyFrame5137.Position = [37.176197389260864, 11.34, 63.321333189206825]
keyFrame5137.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5137.ViewUp = [0.4812518593409867, -0.866, -0.135265166741074]
keyFrame5137.ViewAngle = 30.0
keyFrame5137.ParallelScale = 0.97681
keyFrame5137.PositionPathPoints = [37.176197389260864, 11.34, 63.321333189206825]
keyFrame5137.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5137.PositionMode = 'Path'
keyFrame5137.FocalPointMode = 'Path'
keyFrame5137.ClosedFocalPath = 0
keyFrame5137.ClosedPositionPath = 0

# ====================================================================
keyFrame5138 = CameraKeyFrame()
keyFrame5138.KeyTime = 0.345
keyFrame5138.KeyValues = [0.0]
keyFrame5138.Position = [37.26281563941042, 11.34, 63.296893969489645]
keyFrame5138.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5138.ViewUp = [0.4809803666563021, -0.866, -0.13622739940998002]
keyFrame5138.ViewAngle = 30.0
keyFrame5138.ParallelScale = 0.97681
keyFrame5138.PositionPathPoints = [37.26281563941042, 11.34, 63.296893969489645]
keyFrame5138.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5138.PositionMode = 'Path'
keyFrame5138.FocalPointMode = 'Path'
keyFrame5138.ClosedFocalPath = 0
keyFrame5138.ClosedPositionPath = 0

# ====================================================================
keyFrame5139 = CameraKeyFrame()
keyFrame5139.KeyTime = 0.3475
keyFrame5139.KeyValues = [0.0]
keyFrame5139.Position = [37.34938484592864, 11.34, 63.27228156025479]
keyFrame5139.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5139.ViewUp = [0.48070695005681174, -0.866, -0.1371890871425929]
keyFrame5139.ViewAngle = 30.0
keyFrame5139.ParallelScale = 0.97681
keyFrame5139.PositionPathPoints = [37.34938484592864, 11.34, 63.27228156025479]
keyFrame5139.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5139.PositionMode = 'Path'
keyFrame5139.FocalPointMode = 'Path'
keyFrame5139.ClosedFocalPath = 0
keyFrame5139.ClosedPositionPath = 0

# ====================================================================
keyFrame5140 = CameraKeyFrame()
keyFrame5140.KeyTime = 0.35
keyFrame5140.KeyValues = [0.0]
keyFrame5140.Position = [37.43590465434508, 11.34, 63.2474960619866]
keyFrame5140.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5140.ViewUp = [0.4804316106376196, -0.866, -0.1381502260859421]
keyFrame5140.ViewAngle = 30.0
keyFrame5140.ParallelScale = 0.97681
keyFrame5140.PositionPathPoints = [37.43590465434508, 11.34, 63.2474960619866]
keyFrame5140.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5140.PositionMode = 'Path'
keyFrame5140.FocalPointMode = 'Path'
keyFrame5140.ClosedFocalPath = 0
keyFrame5140.ClosedPositionPath = 0

# ====================================================================
keyFrame5141 = CameraKeyFrame()
keyFrame5141.KeyTime = 0.3525
keyFrame5141.KeyValues = [0.0]
keyFrame5141.Position = [37.52237471869647, 11.34, 63.2225375737976]
keyFrame5141.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5141.ViewUp = [0.4801543496943449, -0.866, -0.13911081158284416]
keyFrame5141.ViewAngle = 30.0
keyFrame5141.ParallelScale = 0.97681
keyFrame5141.PositionPathPoints = [37.52237471869647, 11.34, 63.2225375737976]
keyFrame5141.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5141.PositionMode = 'Path'
keyFrame5141.FocalPointMode = 'Path'
keyFrame5141.ClosedFocalPath = 0
keyFrame5141.ClosedPositionPath = 0

# ====================================================================
keyFrame5142 = CameraKeyFrame()
keyFrame5142.KeyTime = 0.355
keyFrame5142.KeyValues = [0.0]
keyFrame5142.Position = [37.60879469318901, 11.34, 63.197406195499866]
keyFrame5142.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5142.ViewUp = [0.47987516790551815, -0.866, -0.14007084159123967]
keyFrame5142.ViewAngle = 30.0
keyFrame5142.ParallelScale = 0.97681
keyFrame5142.PositionPathPoints = [37.60879469318901, 11.34, 63.197406195499866]
keyFrame5142.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5142.PositionMode = 'Path'
keyFrame5142.FocalPointMode = 'Path'
keyFrame5142.ClosedFocalPath = 0
keyFrame5142.ClosedPositionPath = 0

# ====================================================================
keyFrame5143 = CameraKeyFrame()
keyFrame5143.KeyTime = 0.3575
keyFrame5143.KeyValues = [0.0]
keyFrame5143.Position = [37.695164232199815, 11.34, 63.172102027604694]
keyFrame5143.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5143.ViewUp = [0.4795940666187654, -0.866, -0.14103031130518823]
keyFrame5143.ViewAngle = 30.0
keyFrame5143.ParallelScale = 0.97681
keyFrame5143.PositionPathPoints = [37.695164232199815, 11.34, 63.172102027604694]
keyFrame5143.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5143.PositionMode = 'Path'
keyFrame5143.FocalPointMode = 'Path'
keyFrame5143.ClosedFocalPath = 0
keyFrame5143.ClosedPositionPath = 0

# ====================================================================
keyFrame5144 = CameraKeyFrame()
keyFrame5144.KeyTime = 0.36
keyFrame5144.KeyValues = [0.0]
keyFrame5144.Position = [37.78148299027829, 11.34, 63.146625171322256]
keyFrame5144.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5144.ViewUp = [0.47931104695751453, -0.866, -0.14198921689074828]
keyFrame5144.ViewAngle = 30.0
keyFrame5144.ParallelScale = 0.97681
keyFrame5144.PositionPathPoints = [37.78148299027829, 11.34, 63.146625171322256]
keyFrame5144.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5144.PositionMode = 'Path'
keyFrame5144.FocalPointMode = 'Path'
keyFrame5144.ClosedFocalPath = 0
keyFrame5144.ClosedPositionPath = 0

# ====================================================================
keyFrame5145 = CameraKeyFrame()
keyFrame5145.KeyTime = 0.3625
keyFrame5145.KeyValues = [0.0]
keyFrame5145.Position = [37.8677506221476, 11.34, 63.12097572856122]
keyFrame5145.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5145.ViewUp = [0.4790261100530001, -0.866, -0.1429475545157012]
keyFrame5145.ViewAngle = 30.0
keyFrame5145.ParallelScale = 0.97681
keyFrame5145.PositionPathPoints = [37.8677506221476, 11.34, 63.12097572856122]
keyFrame5145.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5145.PositionMode = 'Path'
keyFrame5145.FocalPointMode = 'Path'
keyFrame5145.ClosedFocalPath = 0
keyFrame5145.ClosedPositionPath = 0

# ====================================================================
keyFrame5146 = CameraKeyFrame()
keyFrame5146.KeyTime = 0.365
keyFrame5146.KeyValues = [0.0]
keyFrame5146.Position = [37.953966782706004, 11.34, 63.09515380192844]
keyFrame5146.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5146.ViewUp = [0.4787392570442594, -0.866, -0.14390532034956732]
keyFrame5146.ViewAngle = 30.0
keyFrame5146.ParallelScale = 0.97681
keyFrame5146.PositionPathPoints = [37.953966782706004, 11.34, 63.09515380192844]
keyFrame5146.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5146.PositionMode = 'Path'
keyFrame5146.FocalPointMode = 'Path'
keyFrame5146.ClosedFocalPath = 0
keyFrame5146.ClosedPositionPath = 0

# ====================================================================
keyFrame5147 = CameraKeyFrame()
keyFrame5147.KeyTime = 0.3675
keyFrame5147.KeyValues = [0.0]
keyFrame5147.Position = [38.04013112702829, 11.34, 63.06915949472857]
keyFrame5147.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5147.ViewUp = [0.47845048907812876, -0.866, -0.14486251056362115]
keyFrame5147.ViewAngle = 30.0
keyFrame5147.ParallelScale = 0.97681
keyFrame5147.PositionPathPoints = [38.04013112702829, 11.34, 63.06915949472857]
keyFrame5147.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5147.PositionMode = 'Path'
keyFrame5147.FocalPointMode = 'Path'
keyFrame5147.ClosedFocalPath = 0
keyFrame5147.ClosedPositionPath = 0

# ====================================================================
keyFrame5148 = CameraKeyFrame()
keyFrame5148.KeyTime = 0.37
keyFrame5148.KeyValues = [0.0]
keyFrame5148.Position = [38.12624331036719, 11.34, 63.04299291096373]
keyFrame5148.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5148.ViewUp = [0.47815980730923974, -0.866, -0.14581912133090738]
keyFrame5148.ViewAngle = 30.0
keyFrame5148.ParallelScale = 0.97681
keyFrame5148.PositionPathPoints = [38.12624331036719, 11.34, 63.04299291096373]
keyFrame5148.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5148.PositionMode = 'Path'
keyFrame5148.FocalPointMode = 'Path'
keyFrame5148.ClosedFocalPath = 0
keyFrame5148.ClosedPositionPath = 0

# ====================================================================
keyFrame5149 = CameraKeyFrame()
keyFrame5149.KeyTime = 0.3725
keyFrame5149.KeyValues = [0.0]
keyFrame5149.Position = [38.212302988154775, 11.34, 63.01665415533317]
keyFrame5149.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5149.ViewUp = [0.47786721290001555, -0.866, -0.14677514882625636]
keyFrame5149.ViewAngle = 30.0
keyFrame5149.ParallelScale = 0.97681
keyFrame5149.PositionPathPoints = [38.212302988154775, 11.34, 63.01665415533317]
keyFrame5149.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5149.PositionMode = 'Path'
keyFrame5149.FocalPointMode = 'Path'
keyFrame5149.ClosedFocalPath = 0
keyFrame5149.ClosedPositionPath = 0

# ====================================================================
keyFrame5150 = CameraKeyFrame()
keyFrame5150.KeyTime = 0.375
keyFrame5150.KeyValues = [0.0]
keyFrame5150.Position = [38.29830981600391, 11.34, 62.99014333323289]
keyFrame5150.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5150.ViewUp = [0.4775727070206671, -0.866, -0.1477305892262998]
keyFrame5150.ViewAngle = 30.0
keyFrame5150.ParallelScale = 0.97681
keyFrame5150.PositionPathPoints = [38.29830981600391, 11.34, 62.99014333323289]
keyFrame5150.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5150.PositionMode = 'Path'
keyFrame5150.FocalPointMode = 'Path'
keyFrame5150.ClosedFocalPath = 0
keyFrame5150.ClosedPositionPath = 0

# ====================================================================
keyFrame5151 = CameraKeyFrame()
keyFrame5151.KeyTime = 0.3775
keyFrame5151.KeyValues = [0.0]
keyFrame5151.Position = [38.38426344970955, 11.34, 62.963460550755336]
keyFrame5151.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5151.ViewUp = [0.47727629084918954, -0.866, -0.14868543870948647]
keyFrame5151.ViewAngle = 30.0
keyFrame5151.ParallelScale = 0.97681
keyFrame5151.PositionPathPoints = [38.38426344970955, 11.34, 62.963460550755336]
keyFrame5151.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5151.PositionMode = 'Path'
keyFrame5151.FocalPointMode = 'Path'
keyFrame5151.ClosedFocalPath = 0
keyFrame5151.ClosedPositionPath = 0

# ====================================================================
keyFrame5152 = CameraKeyFrame()
keyFrame5152.KeyTime = 0.38
keyFrame5152.KeyValues = [0.0]
keyFrame5152.Position = [38.470163545250315, 11.34, 62.936605914688975]
keyFrame5152.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5152.ViewUp = [0.4769779655713582, -0.866, -0.14963969345609773]
keyFrame5152.ViewAngle = 30.0
keyFrame5152.ParallelScale = 0.97681
keyFrame5152.PositionPathPoints = [38.470163545250315, 11.34, 62.936605914688975]
keyFrame5152.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5152.PositionMode = 'Path'
keyFrame5152.FocalPointMode = 'Path'
keyFrame5152.ClosedFocalPath = 0
keyFrame5152.ClosedPositionPath = 0

# ====================================================================
keyFrame5153 = CameraKeyFrame()
keyFrame5153.KeyTime = 0.3825
keyFrame5153.KeyValues = [0.0]
keyFrame5153.Position = [38.556009759975765, 11.34, 62.90957953216448]
keyFrame5153.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5153.ViewUp = [0.4766777323807249, -0.866, -0.15059334964826332]
keyFrame5153.ViewAngle = 30.0
keyFrame5153.ParallelScale = 0.97681
keyFrame5153.PositionPathPoints = [38.556009759975765, 11.34, 62.90957953216448]
keyFrame5153.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5153.PositionMode = 'Path'
keyFrame5153.FocalPointMode = 'Path'
keyFrame5153.ClosedFocalPath = 0
keyFrame5153.ClosedPositionPath = 0

# ====================================================================
keyFrame5154 = CameraKeyFrame()
keyFrame5154.KeyTime = 0.385
keyFrame5154.KeyValues = [0.0]
keyFrame5154.Position = [38.641801751591146, 11.34, 62.882381510957416]
keyFrame5154.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5154.ViewUp = [0.47637559247861455, -0.866, -0.1515464034699769]
keyFrame5154.ViewAngle = 30.0
keyFrame5154.ParallelScale = 0.97681
keyFrame5154.PositionPathPoints = [38.641801751591146, 11.34, 62.882381510957416]
keyFrame5154.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5154.PositionMode = 'Path'
keyFrame5154.FocalPointMode = 'Path'
keyFrame5154.ClosedFocalPath = 0
keyFrame5154.ClosedPositionPath = 0

# ====================================================================
keyFrame5155 = CameraKeyFrame()
keyFrame5155.KeyTime = 0.3875
keyFrame5155.KeyValues = [0.0]
keyFrame5155.Position = [38.72753917693346, 11.34, 62.855011959853165]
keyFrame5155.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5155.ViewUp = [0.4760715470741209, -0.866, -0.15249885110711178]
keyFrame5155.ViewAngle = 30.0
keyFrame5155.ParallelScale = 0.97681
keyFrame5155.PositionPathPoints = [38.72753917693346, 11.34, 62.855011959853165]
keyFrame5155.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5155.PositionMode = 'Path'
keyFrame5155.FocalPointMode = 'Path'
keyFrame5155.ClosedFocalPath = 0
keyFrame5155.ClosedPositionPath = 0

# ====================================================================
keyFrame5156 = CameraKeyFrame()
keyFrame5156.KeyTime = 0.39
keyFrame5156.KeyValues = [0.0]
keyFrame5156.Position = [38.813221693044696, 11.34, 62.82747098832707]
keyFrame5156.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5156.ViewUp = [0.4757655973841033, -0.866, -0.1534506887474366]
keyFrame5156.ViewAngle = 30.0
keyFrame5156.ParallelScale = 0.97681
keyFrame5156.PositionPathPoints = [38.813221693044696, 11.34, 62.82747098832707]
keyFrame5156.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5156.PositionMode = 'Path'
keyFrame5156.FocalPointMode = 'Path'
keyFrame5156.ClosedFocalPath = 0
keyFrame5156.ClosedPositionPath = 0

# ====================================================================
keyFrame5157 = CameraKeyFrame()
keyFrame5157.KeyTime = 0.3925
keyFrame5157.KeyValues = [0.0]
keyFrame5157.Position = [38.89884895717354, 11.34, 62.799758706544004]
keyFrame5157.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5157.ViewUp = [0.4754577446331824, -0.866, -0.15440191258063085]
keyFrame5157.ViewAngle = 30.0
keyFrame5157.ParallelScale = 0.97681
keyFrame5157.PositionPathPoints = [38.89884895717354, 11.34, 62.799758706544004]
keyFrame5157.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5157.PositionMode = 'Path'
keyFrame5157.FocalPointMode = 'Path'
keyFrame5157.ClosedFocalPath = 0
keyFrame5157.ClosedPositionPath = 0

# ====================================================================
keyFrame5158 = CameraKeyFrame()
keyFrame5158.KeyTime = 0.395
keyFrame5158.KeyValues = [0.0]
keyFrame5158.Position = [38.984420626777165, 11.34, 62.7718752253579]
keyFrame5158.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5158.ViewUp = [0.475147990053737, -0.866, -0.1553525187983007]
keyFrame5158.ViewAngle = 30.0
keyFrame5158.ParallelScale = 0.97681
keyFrame5158.PositionPathPoints = [38.984420626777165, 11.34, 62.7718752253579]
keyFrame5158.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5158.PositionMode = 'Path'
keyFrame5158.FocalPointMode = 'Path'
keyFrame5158.ClosedFocalPath = 0
keyFrame5158.ClosedPositionPath = 0

# ====================================================================
keyFrame5159 = CameraKeyFrame()
keyFrame5159.KeyTime = 0.3975
keyFrame5159.KeyValues = [0.0]
keyFrame5159.Position = [39.06993635952287, 11.34, 62.743820656311314]
keyFrame5159.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5159.ViewUp = [0.4748363348858998, -0.866, -0.15630250359399447]
keyFrame5159.ViewAngle = 30.0
keyFrame5159.ParallelScale = 0.97681
keyFrame5159.PositionPathPoints = [39.06993635952287, 11.34, 62.743820656311314]
keyFrame5159.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5159.PositionMode = 'Path'
keyFrame5159.FocalPointMode = 'Path'
keyFrame5159.ClosedFocalPath = 0
keyFrame5159.ClosedPositionPath = 0

# ====================================================================
keyFrame5160 = CameraKeyFrame()
keyFrame5160.KeyTime = 0.4
keyFrame5160.KeyValues = [0.0]
keyFrame5160.Position = [39.15539581328997, 11.34, 62.71559511163497]
keyFrame5160.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5160.ViewUp = [0.47452278037755413, -0.866, -0.15725186316321843]
keyFrame5160.ViewAngle = 30.0
keyFrame5160.ParallelScale = 0.97681
keyFrame5160.PositionPathPoints = [39.15539581328997, 11.34, 62.71559511163497]
keyFrame5160.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5160.PositionMode = 'Path'
keyFrame5160.FocalPointMode = 'Path'
keyFrame5160.ClosedFocalPath = 0
keyFrame5160.ClosedPositionPath = 0

# ====================================================================
keyFrame5161 = CameraKeyFrame()
keyFrame5161.KeyTime = 0.4025
keyFrame5161.KeyValues = [0.0]
keyFrame5161.Position = [39.24079864617141, 11.34, 62.6871987042473]
keyFrame5161.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5161.ViewUp = [0.47420732778432967, -0.866, -0.15820059370345244]
keyFrame5161.ViewAngle = 30.0
keyFrame5161.ParallelScale = 0.97681
keyFrame5161.PositionPathPoints = [39.24079864617141, 11.34, 62.6871987042473]
keyFrame5161.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5161.PositionMode = 'Path'
keyFrame5161.FocalPointMode = 'Path'
keyFrame5161.ClosedFocalPath = 0
keyFrame5161.ClosedPositionPath = 0

# ====================================================================
keyFrame5162 = CameraKeyFrame()
keyFrame5162.KeyTime = 0.405
keyFrame5162.KeyValues = [0.0]
keyFrame5162.Position = [39.326144516475594, 11.34, 62.658631547754034]
keyFrame5162.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5162.ViewUp = [0.4738899783695991, -0.866, -0.15914869141416546]
keyFrame5162.ViewAngle = 30.0
keyFrame5162.ParallelScale = 0.97681
keyFrame5162.PositionPathPoints = [39.326144516475594, 11.34, 62.658631547754034]
keyFrame5162.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5162.PositionMode = 'Path'
keyFrame5162.FocalPointMode = 'Path'
keyFrame5162.ClosedFocalPath = 0
keyFrame5162.ClosedPositionPath = 0

# ====================================================================
keyFrame5163 = CameraKeyFrame()
keyFrame5163.KeyTime = 0.4075
keyFrame5163.KeyValues = [0.0]
keyFrame5163.Position = [39.41143308272808, 11.34, 62.62989375644769]
keyFrame5163.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5163.ViewUp = [0.47357073340447436, -0.866, -0.1600961524968314]
keyFrame5163.ViewAngle = 30.0
keyFrame5163.ParallelScale = 0.97681
keyFrame5163.PositionPathPoints = [39.41143308272808, 11.34, 62.62989375644769]
keyFrame5163.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5163.PositionMode = 'Path'
keyFrame5163.FocalPointMode = 'Path'
keyFrame5163.ClosedFocalPath = 0
keyFrame5163.ClosedPositionPath = 0

# ====================================================================
keyFrame5164 = CameraKeyFrame()
keyFrame5164.KeyTime = 0.41
keyFrame5164.KeyValues = [0.0]
keyFrame5164.Position = [39.49666400367332, 11.34, 62.60098544530719]
keyFrame5164.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5164.ViewUp = [0.473249594167308, -0.866, -0.16104297315655855]
keyFrame5164.ViewAngle = 30.0
keyFrame5164.ParallelScale = 0.97681
keyFrame5164.PositionPathPoints = [39.49666400367332, 11.34, 62.60098544530719]
keyFrame5164.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5164.PositionMode = 'Path'
keyFrame5164.FocalPointMode = 'Path'
keyFrame5164.ClosedFocalPath = 0
keyFrame5164.ClosedPositionPath = 0

# ====================================================================
keyFrame5165 = CameraKeyFrame()
keyFrame5165.KeyTime = 0.4125
keyFrame5165.KeyValues = [0.0]
keyFrame5165.Position = [39.58183693827645, 11.34, 62.57190672999734]
keyFrame5165.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5165.ViewUp = [0.4729265619257819, -0.866, -0.16198914966053699]
keyFrame5165.ViewAngle = 30.0
keyFrame5165.ParallelScale = 0.97681
keyFrame5165.PositionPathPoints = [39.58183693827645, 11.34, 62.57190672999734]
keyFrame5165.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5165.PositionMode = 'Path'
keyFrame5165.FocalPointMode = 'Path'
keyFrame5165.ClosedFocalPath = 0
keyFrame5165.ClosedPositionPath = 0

# ====================================================================
keyFrame5166 = CameraKeyFrame()
keyFrame5166.KeyTime = 0.415
keyFrame5166.KeyValues = [0.0]
keyFrame5166.Position = [39.66695154572503, 11.34, 62.54265772686844]
keyFrame5166.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5166.ViewUp = [0.47260163796275206, -0.866, -0.16293467825371252]
keyFrame5166.ViewAngle = 30.0
keyFrame5166.ParallelScale = 0.97681
keyFrame5166.PositionPathPoints = [39.66695154572503, 11.34, 62.54265772686844]
keyFrame5166.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5166.PositionMode = 'Path'
keyFrame5166.FocalPointMode = 'Path'
keyFrame5166.ClosedFocalPath = 0
keyFrame5166.ClosedPositionPath = 0

# ====================================================================
keyFrame5167 = CameraKeyFrame()
keyFrame5167.KeyTime = 0.4175
keyFrame5167.KeyValues = [0.0]
keyFrame5167.Position = [39.75200748543068, 11.34, 62.51323855295582]
keyFrame5167.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5167.ViewUp = [0.4722748235777172, -0.866, -0.1638795551539971]
keyFrame5167.ViewAngle = 30.0
keyFrame5167.ParallelScale = 0.97681
keyFrame5167.PositionPathPoints = [39.75200748543068, 11.34, 62.51323855295582]
keyFrame5167.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5167.PositionMode = 'Path'
keyFrame5167.FocalPointMode = 'Path'
keyFrame5167.ClosedFocalPath = 0
keyFrame5167.ClosedPositionPath = 0

# ====================================================================
keyFrame5168 = CameraKeyFrame()
keyFrame5168.KeyTime = 0.42
keyFrame5168.KeyValues = [0.0]
keyFrame5168.Position = [39.83700441703098, 11.34, 62.48364932597934]
keyFrame5168.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5168.ViewUp = [0.47194612007780345, -0.866, -0.1648237765816904]
keyFrame5168.ViewAngle = 30.0
keyFrame5168.ParallelScale = 0.97681
keyFrame5168.PositionPathPoints = [39.83700441703098, 11.34, 62.48364932597934]
keyFrame5168.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5168.PositionMode = 'Path'
keyFrame5168.FocalPointMode = 'Path'
keyFrame5168.ClosedFocalPath = 0
keyFrame5168.ClosedPositionPath = 0

# ====================================================================
keyFrame5169 = CameraKeyFrame()
keyFrame5169.KeyTime = 0.4225
keyFrame5169.KeyValues = [0.0]
keyFrame5169.Position = [39.92194200039111, 11.34, 62.453890164343036]
keyFrame5169.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5169.ViewUp = [0.4716155287777587, -0.866, -0.16576733875949984]
keyFrame5169.ViewAngle = 30.0
keyFrame5169.ParallelScale = 0.97681
keyFrame5169.PositionPathPoints = [39.92194200039111, 11.34, 62.453890164343036]
keyFrame5169.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5169.PositionMode = 'Path'
keyFrame5169.FocalPointMode = 'Path'
keyFrame5169.ClosedFocalPath = 0
keyFrame5169.ClosedPositionPath = 0

# ====================================================================
keyFrame5170 = CameraKeyFrame()
keyFrame5170.KeyTime = 0.425
keyFrame5170.KeyValues = [0.0]
keyFrame5170.Position = [40.00681989560566, 11.34, 62.42396118713457]
keyFrame5170.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5170.ViewUp = [0.4712830509999477, -0.866, -0.166710237912561]
keyFrame5170.ViewAngle = 30.0
keyFrame5170.ParallelScale = 0.97681
keyFrame5170.PositionPathPoints = [40.00681989560566, 11.34, 62.42396118713457]
keyFrame5170.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5170.PositionMode = 'Path'
keyFrame5170.FocalPointMode = 'Path'
keyFrame5170.ClosedFocalPath = 0
keyFrame5170.ClosedPositionPath = 0

# ====================================================================
keyFrame5171 = CameraKeyFrame()
keyFrame5171.KeyTime = 0.4275
keyFrame5171.KeyValues = [0.0]
keyFrame5171.Position = [40.091637763000264, 11.34, 62.39386251412485]
keyFrame5171.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5171.ViewUp = [0.4709486880743469, -0.866, -0.1676524702684577]
keyFrame5171.ViewAngle = 30.0
keyFrame5171.ParallelScale = 0.97681
keyFrame5171.PositionPathPoints = [40.091637763000264, 11.34, 62.39386251412485]
keyFrame5171.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5171.PositionMode = 'Path'
keyFrame5171.FocalPointMode = 'Path'
keyFrame5171.ClosedFocalPath = 0
keyFrame5171.ClosedPositionPath = 0

# ====================================================================
keyFrame5172 = CameraKeyFrame()
keyFrame5172.KeyTime = 0.43
keyFrame5172.KeyValues = [0.0]
keyFrame5172.Position = [40.17639526313347, 11.34, 62.36359426576754]
keyFrame5172.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5172.ViewUp = [0.4706124413385394, -0.866, -0.16859403205724222]
keyFrame5172.ViewAngle = 30.0
keyFrame5172.ParallelScale = 0.97681
keyFrame5172.PositionPathPoints = [40.17639526313347, 11.34, 62.36359426576754]
keyFrame5172.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5172.PositionMode = 'Path'
keyFrame5172.FocalPointMode = 'Path'
keyFrame5172.ClosedFocalPath = 0
keyFrame5172.ClosedPositionPath = 0

# ====================================================================
keyFrame5173 = CameraKeyFrame()
keyFrame5173.KeyTime = 0.4325
keyFrame5173.KeyValues = [0.0]
keyFrame5173.Position = [40.26109205679843, 11.34, 62.33315656319864]
keyFrame5173.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5173.ViewUp = [0.4702743121377096, -0.866, -0.16953491951145558]
keyFrame5173.ViewAngle = 30.0
keyFrame5173.ParallelScale = 0.97681
keyFrame5173.PositionPathPoints = [40.26109205679843, 11.34, 62.33315656319864]
keyFrame5173.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5173.PositionMode = 'Path'
keyFrame5173.FocalPointMode = 'Path'
keyFrame5173.ClosedFocalPath = 0
keyFrame5173.ClosedPositionPath = 0

# ====================================================================
keyFrame5174 = CameraKeyFrame()
keyFrame5174.KeyTime = 0.435
keyFrame5174.KeyValues = [0.0]
keyFrame5174.Position = [40.34572780502461, 11.34, 62.30254952823602]
keyFrame5174.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5174.ViewUp = [0.4699343018246381, -0.866, -0.17047512886614774]
keyFrame5174.ViewAngle = 30.0
keyFrame5174.ParallelScale = 0.97681
keyFrame5174.PositionPathPoints = [40.34572780502461, 11.34, 62.30254952823602]
keyFrame5174.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5174.PositionMode = 'Path'
keyFrame5174.FocalPointMode = 'Path'
keyFrame5174.ClosedFocalPath = 0
keyFrame5174.ClosedPositionPath = 0

# ====================================================================
keyFrame5175 = CameraKeyFrame()
keyFrame5175.KeyTime = 0.4375
keyFrame5175.KeyValues = [0.0]
keyFrame5175.Position = [40.43030216907961, 11.34, 62.27177328337896]
keyFrame5175.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5175.ViewUp = [0.4695924117596968, -0.866, -0.17141465635889766]
keyFrame5175.ViewAngle = 30.0
keyFrame5175.ParallelScale = 0.97681
keyFrame5175.PositionPathPoints = [40.43030216907961, 11.34, 62.27177328337896]
keyFrame5175.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5175.PositionMode = 'Path'
keyFrame5175.FocalPointMode = 'Path'
keyFrame5175.ClosedFocalPath = 0
keyFrame5175.ClosedPositionPath = 0

# ====================================================================
keyFrame5176 = CameraKeyFrame()
keyFrame5176.KeyTime = 0.44
keyFrame5176.KeyValues = [0.0]
keyFrame5176.Position = [40.51481481047081, 11.34, 62.24082795180774]
keyFrame5176.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5176.ViewUp = [0.4692486433108434, -0.866, -0.1723534982298337]
keyFrame5176.ViewAngle = 30.0
keyFrame5176.ParallelScale = 0.97681
keyFrame5176.PositionPathPoints = [40.51481481047081, 11.34, 62.24082795180774]
keyFrame5176.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5176.PositionMode = 'Path'
keyFrame5176.FocalPointMode = 'Path'
keyFrame5176.ClosedFocalPath = 0
keyFrame5176.ClosedPositionPath = 0

# ====================================================================
keyFrame5177 = CameraKeyFrame()
keyFrame5177.KeyTime = 0.4425
keyFrame5177.KeyValues = [0.0]
keyFrame5177.Position = [40.59926539094721, 11.34, 62.20971365738312]
keyFrame5177.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5177.ViewUp = [0.4689029978536167, -0.866, -0.17329165072165384]
keyFrame5177.ViewAngle = 30.0
keyFrame5177.ParallelScale = 0.97681
keyFrame5177.PositionPathPoints = [40.59926539094721, 11.34, 62.20971365738312]
keyFrame5177.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5177.PositionMode = 'Path'
keyFrame5177.FocalPointMode = 'Path'
keyFrame5177.ClosedFocalPath = 0
keyFrame5177.ClosedPositionPath = 0

# ====================================================================
keyFrame5178 = CameraKeyFrame()
keyFrame5178.KeyTime = 0.445
keyFrame5178.KeyValues = [0.0]
keyFrame5178.Position = [40.68365357250113, 11.34, 62.178430524645975]
keyFrame5178.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5178.ViewUp = [0.468555476771131, -0.866, -0.17422911007964564]
keyFrame5178.ViewAngle = 30.0
keyFrame5178.ParallelScale = 0.97681
keyFrame5178.PositionPathPoints = [40.68365357250113, 11.34, 62.178430524645975]
keyFrame5178.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5178.PositionMode = 'Path'
keyFrame5178.FocalPointMode = 'Path'
keyFrame5178.ClosedFocalPath = 0
keyFrame5178.ClosedPositionPath = 0

# ====================================================================
keyFrame5179 = CameraKeyFrame()
keyFrame5179.KeyTime = 0.4475
keyFrame5179.KeyValues = [0.0]
keyFrame5179.Position = [40.76797901736991, 11.34, 62.14697867881678]
keyFrame5179.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5179.ViewUp = [0.4682060814540713, -0.866, -0.17516587255170676]
keyFrame5179.ViewAngle = 30.0
keyFrame5179.ParallelScale = 0.97681
keyFrame5179.PositionPathPoints = [40.76797901736991, 11.34, 62.14697867881678]
keyFrame5179.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5179.PositionMode = 'Path'
keyFrame5179.FocalPointMode = 'Path'
keyFrame5179.ClosedFocalPath = 0
keyFrame5179.ClosedPositionPath = 0

# ====================================================================
keyFrame5180 = CameraKeyFrame()
keyFrame5180.KeyTime = 0.45
keyFrame5180.KeyValues = [0.0]
keyFrame5180.Position = [40.852241388037726, 11.34, 62.11535824579518]
keyFrame5180.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5180.ViewUp = [0.46785481330068784, -0.866, -0.17610193438836494]
keyFrame5180.ViewAngle = 30.0
keyFrame5180.ParallelScale = 0.97681
keyFrame5180.PositionPathPoints = [40.852241388037726, 11.34, 62.11535824579518]
keyFrame5180.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5180.PositionMode = 'Path'
keyFrame5180.FocalPointMode = 'Path'
keyFrame5180.ClosedFocalPath = 0
keyFrame5180.ClosedPositionPath = 0

# ====================================================================
keyFrame5181 = CameraKeyFrame()
keyFrame5181.KeyTime = 0.4525
keyFrame5181.KeyValues = [0.0]
keyFrame5181.Position = [40.93644034723734, 11.34, 62.083569352159564]
keyFrame5181.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5181.ViewUp = [0.4675016737167914, -0.866, -0.17703729184279832]
keyFrame5181.ViewAngle = 30.0
keyFrame5181.ParallelScale = 0.97681
keyFrame5181.PositionPathPoints = [40.93644034723734, 11.34, 62.083569352159564]
keyFrame5181.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5181.PositionMode = 'Path'
keyFrame5181.FocalPointMode = 'Path'
keyFrame5181.ClosedFocalPath = 0
keyFrame5181.ClosedPositionPath = 0

# ====================================================================
keyFrame5182 = CameraKeyFrame()
keyFrame5182.KeyTime = 0.455
keyFrame5182.KeyValues = [0.0]
keyFrame5182.Position = [41.02057555795507, 11.34, 62.05161212516468]
keyFrame5182.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5182.ViewUp = [0.4671466641157478, -0.866, -0.17797194117085563]
keyFrame5182.ViewAngle = 30.0
keyFrame5182.ParallelScale = 0.97681
keyFrame5182.PositionPathPoints = [41.02057555795507, 11.34, 62.05161212516468]
keyFrame5182.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5182.PositionMode = 'Path'
keyFrame5182.FocalPointMode = 'Path'
keyFrame5182.ClosedFocalPath = 0
keyFrame5182.ClosedPositionPath = 0

# ====================================================================
keyFrame5183 = CameraKeyFrame()
keyFrame5183.KeyTime = 0.4575
keyFrame5183.KeyValues = [0.0]
keyFrame5183.Position = [41.10464668428807, 11.34, 62.019486692257225]
keyFrame5183.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5183.ViewUp = [0.46678978591847275, -0.866, -0.17890587863107643]
keyFrame5183.ViewAngle = 30.0
keyFrame5183.ParallelScale = 0.97681
keyFrame5183.PositionPathPoints = [41.10464668428807, 11.34, 62.019486692257225]
keyFrame5183.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5183.PositionMode = 'Path'
keyFrame5183.FocalPointMode = 'Path'
keyFrame5183.ClosedFocalPath = 0
keyFrame5183.ClosedPositionPath = 0

# ====================================================================
keyFrame5184 = CameraKeyFrame()
keyFrame5184.KeyTime = 0.46
keyFrame5184.KeyValues = [0.0]
keyFrame5184.Position = [41.18865339052357, 11.34, 61.987193181597256]
keyFrame5184.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5184.ViewUp = [0.46643104055342716, -0.866, -0.17983910048471125]
keyFrame5184.ViewAngle = 30.0
keyFrame5184.ParallelScale = 0.97681
keyFrame5184.PositionPathPoints = [41.18865339052357, 11.34, 61.987193181597256]
keyFrame5184.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5184.PositionMode = 'Path'
keyFrame5184.FocalPointMode = 'Path'
keyFrame5184.ClosedFocalPath = 0
keyFrame5184.ClosedPositionPath = 0

# ====================================================================
keyFrame5185 = CameraKeyFrame()
keyFrame5185.KeyTime = 0.4625
keyFrame5185.KeyValues = [0.0]
keyFrame5185.Position = [41.27259534060116, 11.34, 61.95473172236309]
keyFrame5185.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5185.ViewUp = [0.4660704294566113, -0.866, -0.18077160299574185]
keyFrame5185.ViewAngle = 30.0
keyFrame5185.ParallelScale = 0.97681
keyFrame5185.PositionPathPoints = [41.27259534060116, 11.34, 61.95473172236309]
keyFrame5185.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5185.PositionMode = 'Path'
keyFrame5185.FocalPointMode = 'Path'
keyFrame5185.ClosedFocalPath = 0
keyFrame5185.ClosedPositionPath = 0

# ====================================================================
keyFrame5186 = CameraKeyFrame()
keyFrame5186.KeyTime = 0.465
keyFrame5186.KeyValues = [0.0]
keyFrame5186.Position = [41.356472198727914, 11.34, 61.92210244440372]
keyFrame5186.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5186.ViewUp = [0.4657079540715603, -0.866, -0.1817033824309014]
keyFrame5186.ViewAngle = 30.0
keyFrame5186.ParallelScale = 0.97681
keyFrame5186.PositionPathPoints = [41.356472198727914, 11.34, 61.92210244440372]
keyFrame5186.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5186.PositionMode = 'Path'
keyFrame5186.FocalPointMode = 'Path'
keyFrame5186.ClosedFocalPath = 0
keyFrame5186.ClosedPositionPath = 0

# ====================================================================
keyFrame5187 = CameraKeyFrame()
keyFrame5187.KeyTime = 0.4675
keyFrame5187.KeyValues = [0.0]
keyFrame5187.Position = [41.4402836293804, 11.34, 61.889305478238235]
keyFrame5187.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5187.ViewUp = [0.46534361584933864, -0.866, -0.18263443505969473]
keyFrame5187.ViewAngle = 30.0
keyFrame5187.ParallelScale = 0.97681
keyFrame5187.PositionPathPoints = [41.4402836293804, 11.34, 61.889305478238235]
keyFrame5187.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5187.PositionMode = 'Path'
keyFrame5187.FocalPointMode = 'Path'
keyFrame5187.ClosedFocalPath = 0
keyFrame5187.ClosedPositionPath = 0

# ====================================================================
keyFrame5188 = CameraKeyFrame()
keyFrame5188.KeyTime = 0.47
keyFrame5188.KeyValues = [0.0]
keyFrame5188.Position = [41.52402929730668, 11.34, 61.85634095505523]
keyFrame5188.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5188.ViewUp = [0.46497741624853517, -0.866, -0.18356475715441856]
keyFrame5188.ViewAngle = 30.0
keyFrame5188.ParallelScale = 0.97681
keyFrame5188.PositionPathPoints = [41.52402929730668, 11.34, 61.85634095505523]
keyFrame5188.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5188.PositionMode = 'Path'
keyFrame5188.FocalPointMode = 'Path'
keyFrame5188.ClosedFocalPath = 0
keyFrame5188.ClosedPositionPath = 0

# ====================================================================
keyFrame5189 = CameraKeyFrame()
keyFrame5189.KeyTime = 0.4725
keyFrame5189.KeyValues = [0.0]
keyFrame5189.Position = [41.607708867528174, 11.34, 61.823209006712254]
keyFrame5189.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5189.ViewUp = [0.46460935673525783, -0.866, -0.18449434499018155]
keyFrame5189.ViewAngle = 30.0
keyFrame5189.ParallelScale = 0.97681
keyFrame5189.PositionPathPoints = [41.607708867528174, 11.34, 61.823209006712254]
keyFrame5189.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5189.PositionMode = 'Path'
keyFrame5189.FocalPointMode = 'Path'
keyFrame5189.ClosedFocalPath = 0
keyFrame5189.ClosedPositionPath = 0

# ====================================================================
keyFrame5190 = CameraKeyFrame()
keyFrame5190.KeyTime = 0.475
keyFrame5190.KeyValues = [0.0]
keyFrame5190.Position = [41.69132200534173, 11.34, 61.78990976573523]
keyFrame5190.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5190.ViewUp = [0.4642394387831286, -0.866, -0.18542319484492475]
keyFrame5190.ViewAngle = 30.0
keyFrame5190.ParallelScale = 0.97681
keyFrame5190.PositionPathPoints = [41.69132200534173, 11.34, 61.78990976573523]
keyFrame5190.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5190.PositionMode = 'Path'
keyFrame5190.FocalPointMode = 'Path'
keyFrame5190.ClosedFocalPath = 0
keyFrame5190.ClosedPositionPath = 0

# ====================================================================
keyFrame5191 = CameraKeyFrame()
keyFrame5191.KeyTime = 0.4775
keyFrame5191.KeyValues = [0.0]
keyFrame5191.Position = [41.77486837632152, 11.34, 61.75644336531788]
keyFrame5191.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5191.ViewUp = [0.4638676638732786, -0.866, -0.1863513029994416]
keyFrame5191.ViewAngle = 30.0
keyFrame5191.ParallelScale = 0.97681
keyFrame5191.PositionPathPoints = [41.77486837632152, 11.34, 61.75644336531788]
keyFrame5191.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5191.PositionMode = 'Path'
keyFrame5191.FocalPointMode = 'Path'
keyFrame5191.ClosedFocalPath = 0
keyFrame5191.ClosedPositionPath = 0

# ====================================================================
keyFrame5192 = CameraKeyFrame()
keyFrame5192.KeyTime = 0.48
keyFrame5192.KeyValues = [0.0]
keyFrame5192.Position = [41.85834764632101, 11.34, 61.722809939321145]
keyFrame5192.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5192.ViewUp = [0.4634940334943424, -0.866, -0.18727866573739832]
keyFrame5192.ViewAngle = 30.0
keyFrame5192.ParallelScale = 0.97681
keyFrame5192.PositionPathPoints = [41.85834764632101, 11.34, 61.722809939321145]
keyFrame5192.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5192.PositionMode = 'Path'
keyFrame5192.FocalPointMode = 'Path'
keyFrame5192.ClosedFocalPath = 0
keyFrame5192.ClosedPositionPath = 0

# ====================================================================
keyFrame5193 = CameraKeyFrame()
keyFrame5193.KeyTime = 0.4825
keyFrame5193.KeyValues = [0.0]
keyFrame5193.Position = [41.94175948147493, 11.34, 61.68900962227263]
keyFrame5193.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5193.ViewUp = [0.46311854914245326, -0.866, -0.18820527934535394]
keyFrame5193.ViewAngle = 30.0
keyFrame5193.ParallelScale = 0.97681
keyFrame5193.PositionPathPoints = [41.94175948147493, 11.34, 61.68900962227263]
keyFrame5193.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5193.PositionMode = 'Path'
keyFrame5193.FocalPointMode = 'Path'
keyFrame5193.ClosedFocalPath = 0
keyFrame5193.ClosedPositionPath = 0

# ====================================================================
keyFrame5194 = CameraKeyFrame()
keyFrame5194.KeyTime = 0.485
keyFrame5194.KeyValues = [0.0]
keyFrame5194.Position = [42.02510354820127, 11.34, 61.655042549366]
keyFrame5194.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5194.ViewUp = [0.46274121232123805, -0.866, -0.18913114011278068]
keyFrame5194.ViewAngle = 30.0
keyFrame5194.ParallelScale = 0.97681
keyFrame5194.PositionPathPoints = [42.02510354820127, 11.34, 61.655042549366]
keyFrame5194.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5194.PositionMode = 'Path'
keyFrame5194.FocalPointMode = 'Path'
keyFrame5194.ClosedFocalPath = 0
keyFrame5194.ClosedPositionPath = 0

# ====================================================================
keyFrame5195 = CameraKeyFrame()
keyFrame5195.KeyTime = 0.4875
keyFrame5195.KeyValues = [0.0]
keyFrame5195.Position = [42.10837951320315, 11.34, 61.62090885646046]
keyFrame5195.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5195.ViewUp = [0.4623620245418119, -0.866, -0.19005624433208396]
keyFrame5195.ViewAngle = 30.0
keyFrame5195.ParallelScale = 0.97681
keyFrame5195.PositionPathPoints = [42.10837951320315, 11.34, 61.62090885646046]
keyFrame5195.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5195.PositionMode = 'Path'
keyFrame5195.FocalPointMode = 'Path'
keyFrame5195.ClosedFocalPath = 0
keyFrame5195.ClosedPositionPath = 0

# ====================================================================
keyFrame5196 = CameraKeyFrame()
keyFrame5196.KeyTime = 0.49
keyFrame5196.KeyValues = [0.0]
keyFrame5196.Position = [42.191587043470875, 11.34, 61.586608680080104]
keyFrame5196.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5196.ViewUp = [0.4619809873227732, -0.866, -0.19098058829862286]
keyFrame5196.ViewAngle = 30.0
keyFrame5196.ParallelScale = 0.97681
keyFrame5196.PositionPathPoints = [42.191587043470875, 11.34, 61.586608680080104]
keyFrame5196.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5196.PositionMode = 'Path'
keyFrame5196.FocalPointMode = 'Path'
keyFrame5196.ClosedFocalPath = 0
keyFrame5196.ClosedPositionPath = 0

# ====================================================================
keyFrame5197 = CameraKeyFrame()
keyFrame5197.KeyTime = 0.4925
keyFrame5197.KeyValues = [0.0]
keyFrame5197.Position = [42.27472580628388, 11.34, 61.55214215741342]
keyFrame5197.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5197.ViewUp = [0.4615981021901982, -0.866, -0.19190416831073015]
keyFrame5197.ViewAngle = 30.0
keyFrame5197.ParallelScale = 0.97681
keyFrame5197.PositionPathPoints = [42.27472580628388, 11.34, 61.55214215741342]
keyFrame5197.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5197.PositionMode = 'Path'
keyFrame5197.FocalPointMode = 'Path'
keyFrame5197.ClosedFocalPath = 0
keyFrame5197.ClosedPositionPath = 0

# ====================================================================
keyFrame5198 = CameraKeyFrame()
keyFrame5198.KeyTime = 0.495
keyFrame5198.KeyValues = [0.0]
keyFrame5198.Position = [42.35779546921265, 11.34, 61.51750942631266]
keyFrame5198.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5198.ViewUp = [0.4612133706776364, -0.866, -0.1928269806697325]
keyFrame5198.ViewAngle = 30.0
keyFrame5198.ParallelScale = 0.97681
keyFrame5198.PositionPathPoints = [42.35779546921265, 11.34, 61.51750942631266]
keyFrame5198.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5198.PositionMode = 'Path'
keyFrame5198.FocalPointMode = 'Path'
keyFrame5198.ClosedFocalPath = 0
keyFrame5198.ClosedPositionPath = 0

# ====================================================================
keyFrame5199 = CameraKeyFrame()
keyFrame5199.KeyTime = 0.4975
keyFrame5199.KeyValues = [0.0]
keyFrame5199.Position = [42.440795700120674, 11.34, 61.482710625293294]
keyFrame5199.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5199.ViewUp = [0.4608267943261048, -0.866, -0.19374902167997082]
keyFrame5199.ViewAngle = 30.0
keyFrame5199.ParallelScale = 0.97681
keyFrame5199.PositionPathPoints = [42.440795700120674, 11.34, 61.482710625293294]
keyFrame5199.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5199.PositionMode = 'Path'
keyFrame5199.FocalPointMode = 'Path'
keyFrame5199.ClosedFocalPath = 0
keyFrame5199.ClosedPositionPath = 0

# ====================================================================
keyFrame5200 = CameraKeyFrame()
keyFrame5200.KeyTime = 0.5
keyFrame5200.KeyValues = [0.0]
keyFrame5200.Position = [42.523726167166515, 11.34, 61.44774589353343]
keyFrame5200.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5200.ViewUp = [0.4604383746840831, -0.866, -0.19467028764882033]
keyFrame5200.ViewAngle = 30.0
keyFrame5200.ParallelScale = 0.97681
keyFrame5200.PositionPathPoints = [42.523726167166515, 11.34, 61.44774589353343]
keyFrame5200.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5200.PositionMode = 'Path'
keyFrame5200.FocalPointMode = 'Path'
keyFrame5200.ClosedFocalPath = 0
keyFrame5200.ClosedPositionPath = 0

# ====================================================================
keyFrame5201 = CameraKeyFrame()
keyFrame5201.KeyTime = 0.5025
keyFrame5201.KeyValues = [0.0]
keyFrame5201.Position = [42.60658653880563, 11.34, 61.41261537087324]
keyFrame5201.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5201.ViewUp = [0.4600481133075087, -0.866, -0.19559077488671084]
keyFrame5201.ViewAngle = 30.0
keyFrame5201.ParallelScale = 0.97681
keyFrame5201.PositionPathPoints = [42.60658653880563, 11.34, 61.41261537087324]
keyFrame5201.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5201.PositionMode = 'Path'
keyFrame5201.FocalPointMode = 'Path'
keyFrame5201.ClosedFocalPath = 0
keyFrame5201.ClosedPositionPath = 0

# ====================================================================
keyFrame5202 = CameraKeyFrame()
keyFrame5202.KeyTime = 0.505
keyFrame5202.KeyValues = [0.0]
keyFrame5202.Position = [42.689376483792415, 11.34, 61.377319197814394]
keyFrame5202.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5202.ViewUp = [0.4596560117597712, -0.866, -0.196510479707147]
keyFrame5202.ViewAngle = 30.0
keyFrame5202.ParallelScale = 0.97681
keyFrame5202.PositionPathPoints = [42.689376483792415, 11.34, 61.377319197814394]
keyFrame5202.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5202.PositionMode = 'Path'
keyFrame5202.FocalPointMode = 'Path'
keyFrame5202.ClosedFocalPath = 0
keyFrame5202.ClosedPositionPath = 0

# ====================================================================
keyFrame5203 = CameraKeyFrame()
keyFrame5203.KeyTime = 0.5075
keyFrame5203.KeyValues = [0.0]
keyFrame5203.Position = [42.77209567118217, 11.34, 61.34185751551948]
keyFrame5203.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5203.ViewUp = [0.4592620716117074, -0.866, -0.19742939842672838]
keyFrame5203.ViewAngle = 30.0
keyFrame5203.ParallelScale = 0.97681
keyFrame5203.PositionPathPoints = [42.77209567118217, 11.34, 61.34185751551948]
keyFrame5203.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5203.PositionMode = 'Path'
keyFrame5203.FocalPointMode = 'Path'
keyFrame5203.ClosedFocalPath = 0
keyFrame5203.ClosedPositionPath = 0

# ====================================================================
keyFrame5204 = CameraKeyFrame()
keyFrame5204.KeyTime = 0.51
keyFrame5204.KeyValues = [0.0]
keyFrame5204.Position = [42.854743770333016, 11.34, 61.3062304658114]
keyFrame5204.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5204.ViewUp = [0.4588662944415962, -0.866, -0.1983475273651698]
keyFrame5204.ViewAngle = 30.0
keyFrame5204.ParallelScale = 0.97681
keyFrame5204.PositionPathPoints = [42.854743770333016, 11.34, 61.3062304658114]
keyFrame5204.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5204.PositionMode = 'Path'
keyFrame5204.FocalPointMode = 'Path'
keyFrame5204.ClosedFocalPath = 0
keyFrame5204.ClosedPositionPath = 0

# ====================================================================
keyFrame5205 = CameraKeyFrame()
keyFrame5205.KeyTime = 0.5125
keyFrame5205.KeyValues = [0.0]
keyFrame5205.Position = [42.93732045090789, 11.34, 61.27043819117288]
keyFrame5205.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5205.ViewUp = [0.4584686818351536, -0.866, -0.19926486284532155]
keyFrame5205.ViewAngle = 30.0
keyFrame5205.ParallelScale = 0.97681
keyFrame5205.PositionPathPoints = [42.93732045090789, 11.34, 61.27043819117288]
keyFrame5205.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5205.PositionMode = 'Path'
keyFrame5205.FocalPointMode = 'Path'
keyFrame5205.ClosedFocalPath = 0
keyFrame5205.ClosedPositionPath = 0

# ====================================================================
keyFrame5206 = CameraKeyFrame()
keyFrame5206.KeyTime = 0.515
keyFrame5206.KeyValues = [0.0]
keyFrame5206.Position = [43.019825382876505, 11.34, 61.2344808347458]
keyFrame5206.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5206.ViewUp = [0.4580692353855272, -0.866, -0.20018140119318945]
keyFrame5206.ViewAngle = 30.0
keyFrame5206.ParallelScale = 0.97681
keyFrame5206.PositionPathPoints = [43.019825382876505, 11.34, 61.2344808347458]
keyFrame5206.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5206.PositionMode = 'Path'
keyFrame5206.FocalPointMode = 'Path'
keyFrame5206.ClosedFocalPath = 0
keyFrame5206.ClosedPositionPath = 0

# ====================================================================
keyFrame5207 = CameraKeyFrame()
keyFrame5207.KeyTime = 0.5175
keyFrame5207.KeyValues = [0.0]
keyFrame5207.Position = [43.10225823651727, 11.34, 61.19835854033068]
keyFrame5207.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5207.ViewUp = [0.45766795669316107, -0.866, -0.20109713873811724]
keyFrame5207.ViewAngle = 30.0
keyFrame5207.ParallelScale = 0.97681
keyFrame5207.PositionPathPoints = [43.10225823651727, 11.34, 61.19835854033068]
keyFrame5207.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5207.PositionMode = 'Path'
keyFrame5207.FocalPointMode = 'Path'
keyFrame5207.ClosedFocalPath = 0
keyFrame5207.ClosedPositionPath = 0

# ====================================================================
keyFrame5208 = CameraKeyFrame()
keyFrame5208.KeyTime = 0.52
keyFrame5208.KeyValues = [0.0]
keyFrame5208.Position = [43.184618682419355, 11.34, 61.1620714523861]
keyFrame5208.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5208.ViewUp = [0.45726484734623607, -0.866, -0.2020120718370998]
keyFrame5208.ViewAngle = 30.0
keyFrame5208.ParallelScale = 0.97681
keyFrame5208.PositionPathPoints = [43.184618682419355, 11.34, 61.1620714523861]
keyFrame5208.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5208.PositionMode = 'Path'
keyFrame5208.FocalPointMode = 'Path'
keyFrame5208.ClosedFocalPath = 0
keyFrame5208.ClosedPositionPath = 0

# ====================================================================
keyFrame5209 = CameraKeyFrame()
keyFrame5209.KeyTime = 0.5225
keyFrame5209.KeyValues = [0.0]
keyFrame5209.Position = [43.2669063914845, 11.34, 61.12561971602809]
keyFrame5209.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5209.ViewUp = [0.4568599089439105, -0.866, -0.20292619684592444]
keyFrame5209.ViewAngle = 30.0
keyFrame5209.ParallelScale = 0.97681
keyFrame5209.PositionPathPoints = [43.2669063914845, 11.34, 61.12561971602809]
keyFrame5209.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5209.PositionMode = 'Path'
keyFrame5209.FocalPointMode = 'Path'
keyFrame5209.ClosedFocalPath = 0
keyFrame5209.ClosedPositionPath = 0

# ====================================================================
keyFrame5210 = CameraKeyFrame()
keyFrame5210.KeyTime = 0.525
keyFrame5210.KeyValues = [0.0]
keyFrame5210.Position = [43.34912103492914, 11.34, 61.089003477029614]
keyFrame5210.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5210.ViewUp = [0.456453143106023, -0.866, -0.20383951010713008]
keyFrame5210.ViewAngle = 30.0
keyFrame5210.ParallelScale = 0.97681
keyFrame5210.PositionPathPoints = [43.34912103492914, 11.34, 61.089003477029614]
keyFrame5210.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5210.PositionMode = 'Path'
keyFrame5210.FocalPointMode = 'Path'
keyFrame5210.ClosedFocalPath = 0
keyFrame5210.ClosedPositionPath = 0

# ====================================================================
keyFrame5211 = CameraKeyFrame()
keyFrame5211.KeyTime = 0.5275
keyFrame5211.KeyValues = [0.0]
keyFrame5211.Position = [43.43126228428622, 11.34, 61.05222288181995]
keyFrame5211.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5211.ViewUp = [0.4560445514597079, -0.866, -0.2047520079666491]
keyFrame5211.ViewAngle = 30.0
keyFrame5211.ParallelScale = 0.97681
keyFrame5211.PositionPathPoints = [43.43126228428622, 11.34, 61.05222288181995]
keyFrame5211.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5211.PositionMode = 'Path'
keyFrame5211.FocalPointMode = 'Path'
keyFrame5211.ClosedFocalPath = 0
keyFrame5211.ClosedPositionPath = 0

# ====================================================================
keyFrame5212 = CameraKeyFrame()
keyFrame5212.KeyTime = 0.53
keyFrame5212.KeyValues = [0.0]
keyFrame5212.Position = [43.513329811375456, 11.34, 61.01527807748653]
keyFrame5212.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5212.ViewUp = [0.45563413563938887, -0.866, -0.20566368677382996]
keyFrame5212.ViewAngle = 30.0
keyFrame5212.ParallelScale = 0.97681
keyFrame5212.PositionPathPoints = [43.513329811375456, 11.34, 61.01527807748653]
keyFrame5212.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5212.PositionMode = 'Path'
keyFrame5212.FocalPointMode = 'Path'
keyFrame5212.ClosedFocalPath = 0
keyFrame5212.ClosedPositionPath = 0

# ====================================================================
keyFrame5213 = CameraKeyFrame()
keyFrame5213.KeyTime = 0.5325
keyFrame5213.KeyValues = [0.0]
keyFrame5213.Position = [43.59532328596096, 11.34, 60.978169211950636]
keyFrame5213.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5213.ViewUp = [0.4552218972867717, -0.866, -0.20657454288145918]
keyFrame5213.ViewAngle = 30.0
keyFrame5213.ParallelScale = 0.97681
keyFrame5213.PositionPathPoints = [43.59532328596096, 11.34, 60.978169211950636]
keyFrame5213.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5213.PositionMode = 'Path'
keyFrame5213.FocalPointMode = 'Path'
keyFrame5213.ClosedFocalPath = 0
keyFrame5213.ClosedPositionPath = 0

# ====================================================================
keyFrame5214 = CameraKeyFrame()
keyFrame5214.KeyTime = 0.535
keyFrame5214.KeyValues = [0.0]
keyFrame5214.Position = [43.67724237869486, 11.34, 60.94089643374565]
keyFrame5214.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5214.ViewUp = [0.4548078380508377, -0.866, -0.2074845726457838]
keyFrame5214.ViewAngle = 30.0
keyFrame5214.ParallelScale = 0.97681
keyFrame5214.PositionPathPoints = [43.67724237869486, 11.34, 60.94089643374565]
keyFrame5214.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5214.PositionMode = 'Path'
keyFrame5214.FocalPointMode = 'Path'
keyFrame5214.ClosedFocalPath = 0
keyFrame5214.ClosedPositionPath = 0

# ====================================================================
keyFrame5215 = CameraKeyFrame()
keyFrame5215.KeyTime = 0.5375
keyFrame5215.KeyValues = [0.0]
keyFrame5215.Position = [43.759086761895645, 11.34, 60.903459891958065]
keyFrame5215.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5215.ViewUp = [0.4543919595878368, -0.866, -0.2083937724265335]
keyFrame5215.ViewAngle = 30.0
keyFrame5215.ParallelScale = 0.97681
keyFrame5215.PositionPathPoints = [43.759086761895645, 11.34, 60.903459891958065]
keyFrame5215.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5215.PositionMode = 'Path'
keyFrame5215.FocalPointMode = 'Path'
keyFrame5215.ClosedFocalPath = 0
keyFrame5215.ClosedPositionPath = 0

# ====================================================================
keyFrame5216 = CameraKeyFrame()
keyFrame5216.KeyTime = 0.54
keyFrame5216.KeyValues = [0.0]
keyFrame5216.Position = [43.84085610818194, 11.34, 60.86585973632981]
keyFrame5216.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5216.ViewUp = [0.453974263561281, -0.866, -0.20930213858694297]
keyFrame5216.ViewAngle = 30.0
keyFrame5216.ParallelScale = 0.97681
keyFrame5216.PositionPathPoints = [43.84085610818194, 11.34, 60.86585973632981]
keyFrame5216.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5216.PositionMode = 'Path'
keyFrame5216.FocalPointMode = 'Path'
keyFrame5216.ClosedFocalPath = 0
keyFrame5216.ClosedPositionPath = 0

# ====================================================================
keyFrame5217 = CameraKeyFrame()
keyFrame5217.KeyTime = 0.5425
keyFrame5217.KeyValues = [0.0]
keyFrame5217.Position = [43.92255009047389, 11.34, 60.828096117257736]
keyFrame5217.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5217.ViewUp = [0.45355475164193726, -0.866, -0.21020966749377412]
keyFrame5217.ViewAngle = 30.0
keyFrame5217.ParallelScale = 0.97681
keyFrame5217.PositionPathPoints = [43.92255009047389, 11.34, 60.828096117257736]
keyFrame5217.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5217.PositionMode = 'Path'
keyFrame5217.FocalPointMode = 'Path'
keyFrame5217.ClosedFocalPath = 0
keyFrame5217.ClosedPositionPath = 0

# ====================================================================
keyFrame5218 = CameraKeyFrame()
keyFrame5218.KeyTime = 0.545
keyFrame5218.KeyValues = [0.0]
keyFrame5218.Position = [44.0041683819946, 11.34, 60.790169185793054]
keyFrame5218.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5218.ViewUp = [0.45313342550782093, -0.866, -0.21111635551733832]
keyFrame5218.ViewAngle = 30.0
keyFrame5218.ParallelScale = 0.97681
keyFrame5218.PositionPathPoints = [44.0041683819946, 11.34, 60.790169185793054]
keyFrame5218.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5218.PositionMode = 'Path'
keyFrame5218.FocalPointMode = 'Path'
keyFrame5218.ClosedFocalPath = 0
keyFrame5218.ClosedPositionPath = 0

# ====================================================================
keyFrame5219 = CameraKeyFrame()
keyFrame5219.KeyTime = 0.5475
keyFrame5219.KeyValues = [0.0]
keyFrame5219.Position = [44.08571065627146, 11.34, 60.75207909364083]
keyFrame5219.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5219.ViewUp = [0.45271028684418885, -0.866, -0.2120221990315187]
keyFrame5219.ViewAngle = 30.0
keyFrame5219.ParallelScale = 0.97681
keyFrame5219.PositionPathPoints = [44.08571065627146, 11.34, 60.75207909364083]
keyFrame5219.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5219.PositionMode = 'Path'
keyFrame5219.FocalPointMode = 'Path'
keyFrame5219.ClosedFocalPath = 0
keyFrame5219.ClosedPositionPath = 0

# ====================================================================
keyFrame5220 = CameraKeyFrame()
keyFrame5220.KeyTime = 0.55
keyFrame5220.KeyValues = [0.0]
keyFrame5220.Position = [44.16717658713763, 11.34, 60.71382599315943]
keyFrame5220.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5220.ViewUp = [0.4522853373435326, -0.866, -0.21292719441379246]
keyFrame5220.ViewAngle = 30.0
keyFrame5220.ParallelScale = 0.97681
keyFrame5220.PositionPathPoints = [44.16717658713763, 11.34, 60.71382599315943]
keyFrame5220.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5220.PositionMode = 'Path'
keyFrame5220.FocalPointMode = 'Path'
keyFrame5220.ClosedFocalPath = 0
keyFrame5220.ClosedPositionPath = 0

# ====================================================================
keyFrame5221 = CameraKeyFrame()
keyFrame5221.KeyTime = 0.5525
keyFrame5221.KeyValues = [0.0]
keyFrame5221.Position = [44.24856584873342, 11.34, 60.67541003736001]
keyFrame5221.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5221.ViewUp = [0.4518585787055718, -0.866, -0.21383133804525298]
keyFrame5221.ViewAngle = 30.0
keyFrame5221.ParallelScale = 0.97681
keyFrame5221.PositionPathPoints = [44.24856584873342, 11.34, 60.67541003736001]
keyFrame5221.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5221.PositionMode = 'Path'
keyFrame5221.FocalPointMode = 'Path'
keyFrame5221.ClosedFocalPath = 0
keyFrame5221.ClosedPositionPath = 0

# ====================================================================
keyFrame5222 = CameraKeyFrame()
keyFrame5222.KeyTime = 0.555
keyFrame5222.KeyValues = [0.0]
keyFrame5222.Position = [44.32987811550767, 11.34, 60.63683137990597]
keyFrame5222.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5222.ViewUp = [0.451430012637247, -0.866, -0.21473462631063228]
keyFrame5222.ViewAngle = 30.0
keyFrame5222.ParallelScale = 0.97681
keyFrame5222.PositionPathPoints = [44.32987811550767, 11.34, 60.63683137990597]
keyFrame5222.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5222.PositionMode = 'Path'
keyFrame5222.FocalPointMode = 'Path'
keyFrame5222.ClosedFocalPath = 0
keyFrame5222.ClosedPositionPath = 0

# ====================================================================
keyFrame5223 = CameraKeyFrame()
keyFrame5223.KeyTime = 0.5575
keyFrame5223.KeyValues = [0.0]
keyFrame5223.Position = [44.411113062219144, 11.34, 60.598090175112425]
keyFrame5223.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5223.ViewUp = [0.45099964085271343, -0.866, -0.21563705559832314]
keyFrame5223.ViewAngle = 30.0
keyFrame5223.ParallelScale = 0.97681
keyFrame5223.PositionPathPoints = [44.411113062219144, 11.34, 60.598090175112425]
keyFrame5223.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5223.PositionMode = 'Path'
keyFrame5223.FocalPointMode = 'Path'
keyFrame5223.ClosedFocalPath = 0
keyFrame5223.ClosedPositionPath = 0

# ====================================================================
keyFrame5224 = CameraKeyFrame()
keyFrame5224.KeyTime = 0.56
keyFrame5224.KeyValues = [0.0]
keyFrame5224.Position = [44.49227036393802, 11.34, 60.55918657794569]
keyFrame5224.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5224.ViewUp = [0.4505674650733336, -0.866, -0.21653862230040133]
keyFrame5224.ViewAngle = 30.0
keyFrame5224.ParallelScale = 0.97681
keyFrame5224.PositionPathPoints = [44.49227036393802, 11.34, 60.55918657794569]
keyFrame5224.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5224.PositionMode = 'Path'
keyFrame5224.FocalPointMode = 'Path'
keyFrame5224.ClosedFocalPath = 0
keyFrame5224.ClosedPositionPath = 0

# ====================================================================
keyFrame5225 = CameraKeyFrame()
keyFrame5225.KeyTime = 0.5625
keyFrame5225.KeyValues = [0.0]
keyFrame5225.Position = [44.573349696047174, 11.34, 60.52012074402272]
keyFrame5225.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5225.ViewUp = [0.450133487027671, -0.866, -0.2174393228126481]
keyFrame5225.ViewAngle = 30.0
keyFrame5225.ParallelScale = 0.97681
keyFrame5225.PositionPathPoints = [44.573349696047174, 11.34, 60.52012074402272]
keyFrame5225.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5225.PositionMode = 'Path'
keyFrame5225.FocalPointMode = 'Path'
keyFrame5225.ClosedFocalPath = 0
keyFrame5225.ClosedPositionPath = 0

# ====================================================================
keyFrame5226 = CameraKeyFrame()
keyFrame5226.KeyTime = 0.565
keyFrame5226.KeyValues = [0.0]
keyFrame5226.Position = [44.65435073424369, 11.34, 60.480892829610596]
keyFrame5226.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5226.ViewUp = [0.44969770845148294, -0.866, -0.21833915353457214]
keyFrame5226.ViewAngle = 30.0
keyFrame5226.ParallelScale = 0.97681
keyFrame5226.PositionPathPoints = [44.65435073424369, 11.34, 60.480892829610596]
keyFrame5226.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5226.PositionMode = 'Path'
keyFrame5226.FocalPointMode = 'Path'
keyFrame5226.ClosedFocalPath = 0
keyFrame5226.ClosedPositionPath = 0

# ====================================================================
keyFrame5227 = CameraKeyFrame()
keyFrame5227.KeyTime = 0.5675
keyFrame5227.KeyValues = [0.0]
keyFrame5227.Position = [44.73527315454017, 11.34, 60.441502991625995]
keyFrame5227.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5227.ViewUp = [0.4492601310877141, -0.866, -0.21923811086943212]
keyFrame5227.ViewAngle = 30.0
keyFrame5227.ParallelScale = 0.97681
keyFrame5227.PositionPathPoints = [44.73527315454017, 11.34, 60.441502991625995]
keyFrame5227.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5227.PositionMode = 'Path'
keyFrame5227.FocalPointMode = 'Path'
keyFrame5227.ClosedFocalPath = 0
keyFrame5227.ClosedPositionPath = 0

# ====================================================================
keyFrame5228 = CameraKeyFrame()
keyFrame5228.KeyTime = 0.57
keyFrame5228.KeyValues = [0.0]
keyFrame5228.Position = [44.81611663326622, 11.34, 60.401951387634654]
keyFrame5228.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5228.ViewUp = [0.44882075668648946, -0.866, -0.2201361912242587]
keyFrame5228.ViewAngle = 30.0
keyFrame5228.ParallelScale = 0.97681
keyFrame5228.PositionPathPoints = [44.81611663326622, 11.34, 60.401951387634654]
keyFrame5228.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5228.PositionMode = 'Path'
keyFrame5228.FocalPointMode = 'Path'
keyFrame5228.ClosedFocalPath = 0
keyFrame5228.ClosedPositionPath = 0

# ====================================================================
keyFrame5229 = CameraKeyFrame()
keyFrame5229.KeyTime = 0.5725
keyFrame5229.KeyValues = [0.0]
keyFrame5229.Position = [44.89688084706978, 11.34, 60.36223817585084]
keyFrame5229.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5229.ViewUp = [0.4483795870051076, -0.866, -0.22103339100987704]
keyFrame5229.ViewAngle = 30.0
keyFrame5229.ParallelScale = 0.97681
keyFrame5229.PositionPathPoints = [44.89688084706978, 11.34, 60.36223817585084]
keyFrame5229.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5229.PositionMode = 'Path'
keyFrame5229.FocalPointMode = 'Path'
keyFrame5229.ClosedFocalPath = 0
keyFrame5229.ClosedPositionPath = 0

# ====================================================================
keyFrame5230 = CameraKeyFrame()
keyFrame5230.KeyTime = 0.575
keyFrame5230.KeyValues = [0.0]
keyFrame5230.Position = [44.9775654729186, 11.34, 60.32236351513681]
keyFrame5230.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5230.ViewUp = [0.447936623808034, -0.866, -0.22192970664092884]
keyFrame5230.ViewAngle = 30.0
keyFrame5230.ParallelScale = 0.97681
keyFrame5230.PositionPathPoints = [44.9775654729186, 11.34, 60.32236351513681]
keyFrame5230.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5230.PositionMode = 'Path'
keyFrame5230.FocalPointMode = 'Path'
keyFrame5230.ClosedFocalPath = 0
keyFrame5230.ClosedPositionPath = 0

# ====================================================================
keyFrame5231 = CameraKeyFrame()
keyFrame5231.KeyTime = 0.5775
keyFrame5231.KeyValues = [0.0]
keyFrame5231.Position = [45.058170188101585, 11.34, 60.28232756500229]
keyFrame5231.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5231.ViewUp = [0.44749186886689407, -0.866, -0.22282513453589475]
keyFrame5231.ViewAngle = 30.0
keyFrame5231.ParallelScale = 0.97681
keyFrame5231.PositionPathPoints = [45.058170188101585, 11.34, 60.28232756500229]
keyFrame5231.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5231.PositionMode = 'Path'
keyFrame5231.FocalPointMode = 'Path'
keyFrame5231.ClosedFocalPath = 0
keyFrame5231.ClosedPositionPath = 0

# ====================================================================
keyFrame5232 = CameraKeyFrame()
keyFrame5232.KeyTime = 0.58
keyFrame5232.KeyValues = [0.0]
keyFrame5232.Position = [45.13869467023024, 11.34, 60.24213048560395]
keyFrame5232.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5232.ViewUp = [0.4470453239604666, -0.866, -0.22371967111711658]
keyFrame5232.ViewAngle = 30.0
keyFrame5232.ParallelScale = 0.97681
keyFrame5232.PositionPathPoints = [45.13869467023024, 11.34, 60.24213048560395]
keyFrame5232.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5232.PositionMode = 'Path'
keyFrame5232.FocalPointMode = 'Path'
keyFrame5232.ClosedFocalPath = 0
keyFrame5232.ClosedPositionPath = 0

# ====================================================================
keyFrame5233 = CameraKeyFrame()
keyFrame5233.KeyTime = 0.5825
keyFrame5233.KeyValues = [0.0]
keyFrame5233.Position = [45.21913859724002, 11.34, 60.20177243774485]
keyFrame5233.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5233.ViewUp = [0.4465969908746767, -0.866, -0.22461331281081956]
keyFrame5233.ViewAngle = 30.0
keyFrame5233.ParallelScale = 0.97681
keyFrame5233.PositionPathPoints = [45.21913859724002, 11.34, 60.20177243774485]
keyFrame5233.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5233.PositionMode = 'Path'
keyFrame5233.FocalPointMode = 'Path'
keyFrame5233.ClosedFocalPath = 0
keyFrame5233.ClosedPositionPath = 0

# ====================================================================
keyFrame5234 = CameraKeyFrame()
keyFrame5234.KeyTime = 0.585
keyFrame5234.KeyValues = [0.0]
keyFrame5234.Position = [45.29950164739179, 11.34, 60.161253582873925]
keyFrame5234.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5234.ViewUp = [0.4461468714025892, -0.866, -0.2255060560471346]
keyFrame5234.ViewAngle = 30.0
keyFrame5234.ParallelScale = 0.97681
keyFrame5234.PositionPathPoints = [45.29950164739179, 11.34, 60.161253582873925]
keyFrame5234.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5234.PositionMode = 'Path'
keyFrame5234.FocalPointMode = 'Path'
keyFrame5234.ClosedFocalPath = 0
keyFrame5234.ClosedPositionPath = 0

# ====================================================================
keyFrame5235 = CameraKeyFrame()
keyFrame5235.KeyTime = 0.5875
keyFrame5235.KeyValues = [0.0]
keyFrame5235.Position = [45.37978349927323, 11.34, 60.12057408308545]
keyFrame5235.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5235.ViewUp = [0.4456949673444018, -0.866, -0.2263978972601206]
keyFrame5235.ViewAngle = 30.0
keyFrame5235.ParallelScale = 0.97681
keyFrame5235.PositionPathPoints = [45.37978349927323, 11.34, 60.12057408308545]
keyFrame5235.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5235.PositionMode = 'Path'
keyFrame5235.FocalPointMode = 'Path'
keyFrame5235.ClosedFocalPath = 0
keyFrame5235.ClosedPositionPath = 0

# ====================================================================
keyFrame5236 = CameraKeyFrame()
keyFrame5236.KeyTime = 0.59
keyFrame5236.KeyValues = [0.0]
keyFrame5236.Position = [45.45998383180019, 11.34, 60.079734101118525]
keyFrame5236.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5236.ViewUp = [0.44524128050743816, -0.866, -0.22728883288778665]
keyFrame5236.ViewAngle = 30.0
keyFrame5236.ParallelScale = 0.97681
keyFrame5236.PositionPathPoints = [45.45998383180019, 11.34, 60.079734101118525]
keyFrame5236.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5236.PositionMode = 'Path'
keyFrame5236.FocalPointMode = 'Path'
keyFrame5236.ClosedFocalPath = 0
keyFrame5236.ClosedPositionPath = 0

# ====================================================================
keyFrame5237 = CameraKeyFrame()
keyFrame5237.KeyTime = 0.5925
keyFrame5237.KeyValues = [0.0]
keyFrame5237.Position = [45.54010232421808, 11.34, 60.038733800356496]
keyFrame5237.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5237.ViewUp = [0.4447858127061414, -0.866, -0.2281788593721143]
keyFrame5237.ViewAngle = 30.0
keyFrame5237.ParallelScale = 0.97681
keyFrame5237.PositionPathPoints = [45.54010232421808, 11.34, 60.038733800356496]
keyFrame5237.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5237.PositionMode = 'Path'
keyFrame5237.FocalPointMode = 'Path'
keyFrame5237.ClosedFocalPath = 0
keyFrame5237.ClosedPositionPath = 0

# ====================================================================
keyFrame5238 = CameraKeyFrame()
keyFrame5238.KeyTime = 0.595
keyFrame5238.KeyValues = [0.0]
keyFrame5238.Position = [45.62013865610339, 11.34, 59.99757334482648]
keyFrame5238.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5238.ViewUp = [0.4443285657620671, -0.866, -0.2290679731590798]
keyFrame5238.ViewAngle = 30.0
keyFrame5238.ParallelScale = 0.97681
keyFrame5238.PositionPathPoints = [45.62013865610339, 11.34, 59.99757334482648]
keyFrame5238.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5238.PositionMode = 'Path'
keyFrame5238.FocalPointMode = 'Path'
keyFrame5238.ClosedFocalPath = 0
keyFrame5238.ClosedPositionPath = 0

# ====================================================================
keyFrame5239 = CameraKeyFrame()
keyFrame5239.KeyTime = 0.5975
keyFrame5239.KeyValues = [0.0]
keyFrame5239.Position = [45.70009250736497, 11.34, 59.95625289919879]
keyFrame5239.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5239.ViewUp = [0.44386954150387636, -0.866, -0.22995617069867658]
keyFrame5239.ViewAngle = 30.0
keyFrame5239.ParallelScale = 0.97681
keyFrame5239.PositionPathPoints = [45.70009250736497, 11.34, 59.95625289919879]
keyFrame5239.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5239.PositionMode = 'Path'
keyFrame5239.FocalPointMode = 'Path'
keyFrame5239.ClosedFocalPath = 0
keyFrame5239.ClosedPositionPath = 0

# ====================================================================
keyFrame5240 = CameraKeyFrame()
keyFrame5240.KeyTime = 0.6
keyFrame5240.KeyValues = [0.0]
keyFrame5240.Position = [45.77996355824547, 11.34, 59.91477262878644]
keyFrame5240.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5240.ViewUp = [0.4434087417673295, -0.866, -0.2308434484449371]
keyFrame5240.ViewAngle = 30.0
keyFrame5240.ParallelScale = 0.97681
keyFrame5240.PositionPathPoints = [45.77996355824547, 11.34, 59.91477262878644]
keyFrame5240.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5240.PositionMode = 'Path'
keyFrame5240.FocalPointMode = 'Path'
keyFrame5240.ClosedFocalPath = 0
keyFrame5240.ClosedPositionPath = 0

# ====================================================================
keyFrame5241 = CameraKeyFrame()
keyFrame5241.KeyTime = 0.6025
keyFrame5241.KeyValues = [0.0]
keyFrame5241.Position = [45.859751489322775, 11.34, 59.873132699544584]
keyFrame5241.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5241.ViewUp = [0.44294616839527856, -0.866, -0.23172980285595549]
keyFrame5241.ViewAngle = 30.0
keyFrame5241.ParallelScale = 0.97681
keyFrame5241.PositionPathPoints = [45.859751489322775, 11.34, 59.873132699544584]
keyFrame5241.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5241.PositionMode = 'Path'
keyFrame5241.FocalPointMode = 'Path'
keyFrame5241.ClosedFocalPath = 0
keyFrame5241.ClosedPositionPath = 0

# ====================================================================
keyFrame5242 = CameraKeyFrame()
keyFrame5242.KeyTime = 0.605
keyFrame5242.KeyValues = [0.0]
keyFrame5242.Position = [45.939455981500075, 11.34, 59.83133327806277]
keyFrame5242.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5242.ViewUp = [0.4424818232376612, -0.866, -0.2326152303939097]
keyFrame5242.ViewAngle = 30.0
keyFrame5242.ParallelScale = 0.97681
keyFrame5242.PositionPathPoints = [45.939455981500075, 11.34, 59.83133327806277]
keyFrame5242.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5242.PositionMode = 'Path'
keyFrame5242.FocalPointMode = 'Path'
keyFrame5242.ClosedFocalPath = 0
keyFrame5242.ClosedPositionPath = 0

# ====================================================================
keyFrame5243 = CameraKeyFrame()
keyFrame5243.KeyTime = 0.6075
keyFrame5243.KeyValues = [0.0]
keyFrame5243.Position = [46.01907671561219, 11.34, 59.78937453131197]
keyFrame5243.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5243.ViewUp = [0.44201570815149366, -0.866, -0.23349972752508358]
keyFrame5243.ViewAngle = 30.0
keyFrame5243.ParallelScale = 0.97681
keyFrame5243.PositionPathPoints = [46.01907671561219, 11.34, 59.78937453131197]
keyFrame5243.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5243.PositionMode = 'Path'
keyFrame5243.FocalPointMode = 'Path'
keyFrame5243.ClosedFocalPath = 0
keyFrame5243.ClosedPositionPath = 0

# ====================================================================
keyFrame5244 = CameraKeyFrame()
keyFrame5244.KeyTime = 0.61
keyFrame5244.KeyValues = [0.0]
keyFrame5244.Position = [46.09861337298321, 11.34, 59.747256626999466]
keyFrame5244.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5244.ViewUp = [0.4415478250008636, -0.866, -0.23438329071988942]
keyFrame5244.ViewAngle = 30.0
keyFrame5244.ParallelScale = 0.97681
keyFrame5244.PositionPathPoints = [46.09861337298321, 11.34, 59.747256626999466]
keyFrame5244.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5244.PositionMode = 'Path'
keyFrame5244.FocalPointMode = 'Path'
keyFrame5244.ClosedFocalPath = 0
keyFrame5244.ClosedPositionPath = 0

# ====================================================================
keyFrame5245 = CameraKeyFrame()
keyFrame5245.KeyTime = 0.6125
keyFrame5245.KeyValues = [0.0]
keyFrame5245.Position = [46.17806563546476, 11.34, 59.70497973359187]
keyFrame5245.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5245.ViewUp = [0.441078175656924, -0.866, -0.23526591645289005]
keyFrame5245.ViewAngle = 30.0
keyFrame5245.ParallelScale = 0.97681
keyFrame5245.PositionPathPoints = [46.17806563546476, 11.34, 59.70497973359187]
keyFrame5245.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5245.PositionMode = 'Path'
keyFrame5245.FocalPointMode = 'Path'
keyFrame5245.ClosedFocalPath = 0
keyFrame5245.ClosedPositionPath = 0

# ====================================================================
keyFrame5246 = CameraKeyFrame()
keyFrame5246.KeyTime = 0.615
keyFrame5246.KeyValues = [0.0]
keyFrame5246.Position = [46.2574331852465, 11.34, 59.66254402019258]
keyFrame5246.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5246.ViewUp = [0.44060676199788573, -0.866, -0.23614760120282116]
keyFrame5246.ViewAngle = 30.0
keyFrame5246.ParallelScale = 0.97681
keyFrame5246.PositionPathPoints = [46.2574331852465, 11.34, 59.66254402019258]
keyFrame5246.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5246.PositionMode = 'Path'
keyFrame5246.FocalPointMode = 'Path'
keyFrame5246.ClosedFocalPath = 0
keyFrame5246.ClosedPositionPath = 0

# ====================================================================
keyFrame5247 = CameraKeyFrame()
keyFrame5247.KeyTime = 0.6175
keyFrame5247.KeyValues = [0.0]
keyFrame5247.Position = [46.336715704857326, 11.34, 59.619949656541166]
keyFrame5247.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5247.ViewUp = [0.44013358590901114, -0.866, -0.23702834145261348]
keyFrame5247.ViewAngle = 30.0
keyFrame5247.ParallelScale = 0.97681
keyFrame5247.PositionPathPoints = [46.336715704857326, 11.34, 59.619949656541166]
keyFrame5247.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5247.PositionMode = 'Path'
keyFrame5247.FocalPointMode = 'Path'
keyFrame5247.ClosedFocalPath = 0
keyFrame5247.ClosedPositionPath = 0

# ====================================================================
keyFrame5248 = CameraKeyFrame()
keyFrame5248.KeyTime = 0.62
keyFrame5248.KeyValues = [0.0]
keyFrame5248.Position = [46.41591287716676, 11.34, 59.577196813012826]
keyFrame5248.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5248.ViewUp = [0.4396586492826072, -0.866, -0.23790813368941519]
keyFrame5248.ViewAngle = 30.0
keyFrame5248.ParallelScale = 0.97681
keyFrame5248.PositionPathPoints = [46.41591287716676, 11.34, 59.577196813012826]
keyFrame5248.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5248.PositionMode = 'Path'
keyFrame5248.FocalPointMode = 'Path'
keyFrame5248.ClosedFocalPath = 0
keyFrame5248.ClosedPositionPath = 0

# ====================================================================
keyFrame5249 = CameraKeyFrame()
keyFrame5249.KeyTime = 0.6225
keyFrame5249.KeyValues = [0.0]
keyFrame5249.Position = [46.49502438538627, 11.34, 59.53428566061774]
keyFrame5249.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5249.ViewUp = [0.4391819540180185, -0.866, -0.238786974404614]
keyFrame5249.ViewAngle = 30.0
keyFrame5249.ParallelScale = 0.97681
keyFrame5249.PositionPathPoints = [46.49502438538627, 11.34, 59.53428566061774]
keyFrame5249.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5249.PositionMode = 'Path'
keyFrame5249.FocalPointMode = 'Path'
keyFrame5249.ClosedFocalPath = 0
keyFrame5249.ClosedPositionPath = 0

# ====================================================================
keyFrame5250 = CameraKeyFrame()
keyFrame5250.KeyTime = 0.625
keyFrame5250.KeyValues = [0.0]
keyFrame5250.Position = [46.57404991307051, 11.34, 59.49121637100054]
keyFrame5250.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5250.ViewUp = [0.4387035020216209, -0.866, -0.23966486009385962]
keyFrame5250.ViewAngle = 30.0
keyFrame5250.ParallelScale = 0.97681
keyFrame5250.PositionPathPoints = [46.57404991307051, 11.34, 59.49121637100054]
keyFrame5250.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5250.PositionMode = 'Path'
keyFrame5250.FocalPointMode = 'Path'
keyFrame5250.ClosedFocalPath = 0
keyFrame5250.ClosedPositionPath = 0

# ====================================================================
keyFrame5251 = CameraKeyFrame()
keyFrame5251.KeyTime = 0.6275
keyFrame5251.KeyValues = [0.0]
keyFrame5251.Position = [46.65298914411872, 11.34, 59.44798911643966]
keyFrame5251.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5251.ViewUp = [0.43822329520813413, -0.866, -0.2405417871991468]
keyFrame5251.ViewAngle = 30.0
keyFrame5251.ParallelScale = 0.97681
keyFrame5251.PositionPathPoints = [46.65298914411872, 11.34, 59.44798911643966]
keyFrame5251.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5251.PositionMode = 'Path'
keyFrame5251.FocalPointMode = 'Path'
keyFrame5251.ClosedFocalPath = 0
keyFrame5251.ClosedPositionPath = 0

# ====================================================================
keyFrame5252 = CameraKeyFrame()
keyFrame5252.KeyTime = 0.63
keyFrame5252.KeyValues = [0.0]
keyFrame5252.Position = [46.731841762775986, 11.34, 59.4046040698468]
keyFrame5252.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5252.ViewUp = [0.4377413354995338, -0.866, -0.24141775215632771]
keyFrame5252.ViewAngle = 30.0
keyFrame5252.ParallelScale = 0.97681
keyFrame5252.PositionPathPoints = [46.731841762775986, 11.34, 59.4046040698468]
keyFrame5252.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5252.PositionMode = 'Path'
keyFrame5252.FocalPointMode = 'Path'
keyFrame5252.ClosedFocalPath = 0
keyFrame5252.ClosedPositionPath = 0

# ====================================================================
keyFrame5253 = CameraKeyFrame()
keyFrame5253.KeyTime = 0.6325
keyFrame5253.KeyValues = [0.0]
keyFrame5253.Position = [46.81060745363456, 11.34, 59.3610614047663]
keyFrame5253.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5253.ViewUp = [0.437257624823535, -0.866, -0.24229275146136334]
keyFrame5253.ViewAngle = 30.0
keyFrame5253.ParallelScale = 0.97681
keyFrame5253.PositionPathPoints = [46.81060745363456, 11.34, 59.3610614047663]
keyFrame5253.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5253.PositionMode = 'Path'
keyFrame5253.FocalPointMode = 'Path'
keyFrame5253.ClosedFocalPath = 0
keyFrame5253.ClosedPositionPath = 0

# ====================================================================
keyFrame5254 = CameraKeyFrame()
keyFrame5254.KeyTime = 0.635
keyFrame5254.KeyValues = [0.0]
keyFrame5254.Position = [46.889285901635205, 11.34, 59.31736129537459]
keyFrame5254.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5254.ViewUp = [0.4367721651148694, -0.866, -0.24316678161400954]
keyFrame5254.ViewAngle = 30.0
keyFrame5254.ParallelScale = 0.97681
keyFrame5254.PositionPathPoints = [46.889285901635205, 11.34, 59.31736129537459]
keyFrame5254.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5254.PositionMode = 'Path'
keyFrame5254.FocalPointMode = 'Path'
keyFrame5254.ClosedFocalPath = 0
keyFrame5254.ClosedPositionPath = 0

# ====================================================================
keyFrame5255 = CameraKeyFrame()
keyFrame5255.KeyTime = 0.6375
keyFrame5255.KeyValues = [0.0]
keyFrame5255.Position = [46.967876792068466, 11.34, 59.273503916479555]
keyFrame5255.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5255.ViewUp = [0.4362849583152787, -0.866, -0.2440398391178234]
keyFrame5255.ViewAngle = 30.0
keyFrame5255.ParallelScale = 0.97681
keyFrame5255.PositionPathPoints = [46.967876792068466, 11.34, 59.273503916479555]
keyFrame5255.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5255.PositionMode = 'Path'
keyFrame5255.FocalPointMode = 'Path'
keyFrame5255.ClosedFocalPath = 0
keyFrame5255.ClosedPositionPath = 0

# ====================================================================
keyFrame5256 = CameraKeyFrame()
keyFrame5256.KeyTime = 0.64
keyFrame5256.KeyValues = [0.0]
keyFrame5256.Position = [47.046379810576, 11.34, 59.22948944351997]
keyFrame5256.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5256.ViewUp = [0.4357960063735082, -0.866, -0.24491192048017513]
keyFrame5256.ViewAngle = 30.0
keyFrame5256.ParallelScale = 0.97681
keyFrame5256.PositionPathPoints = [47.046379810576, 11.34, 59.22948944351997]
keyFrame5256.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5256.PositionMode = 'Path'
keyFrame5256.FocalPointMode = 'Path'
keyFrame5256.ClosedFocalPath = 0
keyFrame5256.ClosedPositionPath = 0

# ====================================================================
keyFrame5257 = CameraKeyFrame()
keyFrame5257.KeyTime = 0.6425
keyFrame5257.KeyValues = [0.0]
keyFrame5257.Position = [47.124794643151915, 11.34, 59.18531805256491]
keyFrame5257.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5257.ViewUp = [0.43530531124530014, -0.866, -0.2457830222122604]
keyFrame5257.ViewAngle = 30.0
keyFrame5257.ParallelScale = 0.97681
keyFrame5257.PositionPathPoints = [47.124794643151915, 11.34, 59.18531805256491]
keyFrame5257.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5257.PositionMode = 'Path'
keyFrame5257.FocalPointMode = 'Path'
keyFrame5257.ClosedFocalPath = 0
keyFrame5257.ClosedPositionPath = 0

# ====================================================================
keyFrame5258 = CameraKeyFrame()
keyFrame5258.KeyTime = 0.645
keyFrame5258.KeyValues = [0.0]
keyFrame5258.Position = [47.20312097614401, 11.34, 59.14098992031317]
keyFrame5258.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5258.ViewUp = [0.4348128748933871, -0.866, -0.24665314082911213]
keyFrame5258.ViewAngle = 30.0
keyFrame5258.ParallelScale = 0.97681
keyFrame5258.PositionPathPoints = [47.20312097614401, 11.34, 59.14098992031317]
keyFrame5258.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5258.PositionMode = 'Path'
keyFrame5258.FocalPointMode = 'Path'
keyFrame5258.ClosedFocalPath = 0
keyFrame5258.ClosedPositionPath = 0

# ====================================================================
keyFrame5259 = CameraKeyFrame()
keyFrame5259.KeyTime = 0.6475
keyFrame5259.KeyValues = [0.0]
keyFrame5259.Position = [47.281358496255194, 11.34, 59.096505224092645]
keyFrame5259.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5259.ViewUp = [0.4343186992874855, -0.866, -0.24752227284961303]
keyFrame5259.ViewAngle = 30.0
keyFrame5259.ParallelScale = 0.97681
keyFrame5259.PositionPathPoints = [47.281358496255194, 11.34, 59.096505224092645]
keyFrame5259.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5259.PositionMode = 'Path'
keyFrame5259.FocalPointMode = 'Path'
keyFrame5259.ClosedFocalPath = 0
keyFrame5259.ClosedPositionPath = 0

# ====================================================================
keyFrame5260 = CameraKeyFrame()
keyFrame5260.KeyTime = 0.65
keyFrame5260.KeyValues = [0.0]
keyFrame5260.Position = [47.35950689054472, 11.34, 59.05186414185979]
keyFrame5260.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5260.ViewUp = [0.43382278640428906, -0.866, -0.24839041479650728]
keyFrame5260.ViewAngle = 30.0
keyFrame5260.ParallelScale = 0.97681
keyFrame5260.PositionPathPoints = [47.35950689054472, 11.34, 59.05186414185979]
keyFrame5260.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5260.PositionMode = 'Path'
keyFrame5260.FocalPointMode = 'Path'
keyFrame5260.ClosedFocalPath = 0
keyFrame5260.ClosedPositionPath = 0

# ====================================================================
keyFrame5261 = CameraKeyFrame()
keyFrame5261.KeyTime = 0.6525
keyFrame5261.KeyValues = [0.0]
keyFrame5261.Position = [47.43756584642951, 11.34, 59.00706685219897]
keyFrame5261.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5261.ViewUp = [0.43332513822746216, -0.866, -0.249257563196413]
keyFrame5261.ViewAngle = 30.0
keyFrame5261.ParallelScale = 0.97681
keyFrame5261.PositionPathPoints = [47.43756584642951, 11.34, 59.00706685219897]
keyFrame5261.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5261.PositionMode = 'Path'
keyFrame5261.FocalPointMode = 'Path'
keyFrame5261.ClosedFocalPath = 0
keyFrame5261.ClosedPositionPath = 0

# ====================================================================
keyFrame5262 = CameraKeyFrame()
keyFrame5262.KeyTime = 0.655
keyFrame5262.KeyValues = [0.0]
keyFrame5262.Position = [47.515535051685475, 11.34, 58.96211353432192]
keyFrame5262.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5262.ViewUp = [0.43282575674763335, -0.866, -0.2501237145798341]
keyFrame5262.ViewAngle = 30.0
keyFrame5262.ParallelScale = 0.97681
keyFrame5262.PositionPathPoints = [47.515535051685475, 11.34, 58.96211353432192]
keyFrame5262.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5262.PositionMode = 'Path'
keyFrame5262.FocalPointMode = 'Path'
keyFrame5262.ClosedFocalPath = 0
keyFrame5262.ClosedPositionPath = 0

# ====================================================================
keyFrame5263 = CameraKeyFrame()
keyFrame5263.KeyTime = 0.6575
keyFrame5263.KeyValues = [0.0]
keyFrame5263.Position = [47.59341419444888, 11.34, 58.91700436806715]
keyFrame5263.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5263.ViewUp = [0.43232464396238884, -0.866, -0.25098886548117266]
keyFrame5263.ViewAngle = 30.0
keyFrame5263.ParallelScale = 0.97681
keyFrame5263.PositionPathPoints = [47.59341419444888, 11.34, 58.91700436806715]
keyFrame5263.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5263.PositionMode = 'Path'
keyFrame5263.FocalPointMode = 'Path'
keyFrame5263.ClosedFocalPath = 0
keyFrame5263.ClosedPositionPath = 0

# ====================================================================
keyFrame5264 = CameraKeyFrame()
keyFrame5264.KeyTime = 0.66
keyFrame5264.KeyValues = [0.0]
keyFrame5264.Position = [47.67120296321755, 11.34, 58.87173953389932]
keyFrame5264.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5264.ViewUp = [0.4318218018762658, -0.866, -0.25185301243874064]
keyFrame5264.ViewAngle = 30.0
keyFrame5264.ParallelScale = 0.97681
keyFrame5264.PositionPathPoints = [47.67120296321755, 11.34, 58.87173953389932]
keyFrame5264.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5264.PositionMode = 'Path'
keyFrame5264.FocalPointMode = 'Path'
keyFrame5264.ClosedFocalPath = 0
keyFrame5264.ClosedPositionPath = 0

# ====================================================================
keyFrame5265 = CameraKeyFrame()
keyFrame5265.KeyTime = 0.6625
keyFrame5265.KeyValues = [0.0]
keyFrame5265.Position = [47.748901046852296, 11.34, 58.82631921290869]
keyFrame5265.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5265.ViewUp = [0.4313172325007458, -0.866, -0.2527161519947725]
keyFrame5265.ViewAngle = 30.0
keyFrame5265.ParallelScale = 0.97681
keyFrame5265.PositionPathPoints = [47.748901046852296, 11.34, 58.82631921290869]
keyFrame5265.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5265.PositionMode = 'Path'
keyFrame5265.FocalPointMode = 'Path'
keyFrame5265.ClosedFocalPath = 0
keyFrame5265.ClosedPositionPath = 0

# ====================================================================
keyFrame5266 = CameraKeyFrame()
keyFrame5266.KeyTime = 0.665
keyFrame5266.KeyValues = [0.0]
keyFrame5266.Position = [47.82650813457812, 11.34, 58.780743586810516]
keyFrame5266.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5266.ViewUp = [0.43081093785424845, -0.866, -0.2535782806954369]
keyFrame5266.ViewAngle = 30.0
keyFrame5266.ParallelScale = 0.97681
keyFrame5266.PositionPathPoints = [47.82650813457812, 11.34, 58.780743586810516]
keyFrame5266.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5266.PositionMode = 'Path'
keyFrame5266.FocalPointMode = 'Path'
keyFrame5266.ClosedFocalPath = 0
keyFrame5266.ClosedPositionPath = 0

# ====================================================================
keyFrame5267 = CameraKeyFrame()
keyFrame5267.KeyTime = 0.6675
keyFrame5267.KeyValues = [0.0]
keyFrame5267.Position = [47.90402391598565, 11.34, 58.73501283794445]
keyFrame5267.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5267.ViewUp = [0.4303029199621247, -0.866, -0.25443939509084906]
keyFrame5267.ViewAngle = 30.0
keyFrame5267.ParallelScale = 0.97681
keyFrame5267.PositionPathPoints = [47.90402391598565, 11.34, 58.73501283794445]
keyFrame5267.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5267.PositionMode = 'Path'
keyFrame5267.FocalPointMode = 'Path'
keyFrame5267.ClosedFocalPath = 0
keyFrame5267.ClosedPositionPath = 0

# ====================================================================
keyFrame5268 = CameraKeyFrame()
keyFrame5268.KeyTime = 0.67
keyFrame5268.KeyValues = [0.0]
keyFrame5268.Position = [47.981448081032326, 11.34, 58.689127149273986]
keyFrame5268.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5268.ViewUp = [0.4297931808566502, -0.866, -0.2552994917350827]
keyFrame5268.ViewAngle = 30.0
keyFrame5268.ParallelScale = 0.97681
keyFrame5268.PositionPathPoints = [47.981448081032326, 11.34, 58.689127149273986]
keyFrame5268.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5268.PositionMode = 'Path'
keyFrame5268.FocalPointMode = 'Path'
keyFrame5268.ClosedFocalPath = 0
keyFrame5268.ClosedPositionPath = 0

# ====================================================================
keyFrame5269 = CameraKeyFrame()
keyFrame5269.KeyTime = 0.6725
keyFrame5269.KeyValues = [0.0]
keyFrame5269.Position = [48.05878032004381, 11.34, 58.64308670438582]
keyFrame5269.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5269.ViewUp = [0.4292817225770189, -0.866, -0.25615856718618235]
keyFrame5269.ViewAngle = 30.0
keyFrame5269.ParallelScale = 0.97681
keyFrame5269.PositionPathPoints = [48.05878032004381, 11.34, 58.64308670438582]
keyFrame5269.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5269.PositionMode = 'Path'
keyFrame5269.FocalPointMode = 'Path'
keyFrame5269.ClosedFocalPath = 0
keyFrame5269.ClosedPositionPath = 0

# ====================================================================
keyFrame5270 = CameraKeyFrame()
keyFrame5270.KeyTime = 0.675
keyFrame5270.KeyValues = [0.0]
keyFrame5270.Position = [48.13602032371524, 11.34, 58.59689168748932]
keyFrame5270.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5270.ViewUp = [0.4287685471693364, -0.866, -0.25701661800617526]
keyFrame5270.ViewAngle = 30.0
keyFrame5270.ParallelScale = 0.97681
keyFrame5270.PositionPathPoints = [48.13602032371524, 11.34, 58.59689168748932]
keyFrame5270.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5270.PositionMode = 'Path'
keyFrame5270.FocalPointMode = 'Path'
keyFrame5270.ClosedFocalPath = 0
keyFrame5270.ClosedPositionPath = 0

# ====================================================================
keyFrame5271 = CameraKeyFrame()
keyFrame5271.KeyTime = 0.6775
keyFrame5271.KeyValues = [0.0]
keyFrame5271.Position = [48.21316778311261, 11.34, 58.55054228341586]
keyFrame5271.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5271.ViewUp = [0.42825365668661336, -0.866, -0.2578736407610836]
keyFrame5271.ViewAngle = 30.0
keyFrame5271.ParallelScale = 0.97681
keyFrame5271.PositionPathPoints = [48.21316778311261, 11.34, 58.55054228341586]
keyFrame5271.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5271.PositionMode = 'Path'
keyFrame5271.FocalPointMode = 'Path'
keyFrame5271.ClosedFocalPath = 0
keyFrame5271.ClosedPositionPath = 0

# ====================================================================
keyFrame5272 = CameraKeyFrame()
keyFrame5272.KeyTime = 0.68
keyFrame5272.KeyValues = [0.0]
keyFrame5272.Position = [48.29022238966502, 11.34, 58.50403867760062]
keyFrame5272.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5272.ViewUp = [0.42773705318875904, -0.866, -0.2587296320209367]
keyFrame5272.ViewAngle = 30.0
keyFrame5272.ParallelScale = 0.97681
keyFrame5272.PositionPathPoints = [48.29022238966502, 11.34, 58.50403867760062]
keyFrame5272.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5272.PositionMode = 'Path'
keyFrame5272.FocalPointMode = 'Path'
keyFrame5272.ClosedFocalPath = 0
keyFrame5272.ClosedPositionPath = 0

# ====================================================================
keyFrame5273 = CameraKeyFrame()
keyFrame5273.KeyTime = 0.6825
keyFrame5273.KeyValues = [0.0]
keyFrame5273.Position = [48.36718383498423, 11.34, 58.45738105572413]
keyFrame5273.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5273.ViewUp = [0.4272187387425747, -0.866, -0.25958458835978293]
keyFrame5273.ViewAngle = 30.0
keyFrame5273.ParallelScale = 0.97681
keyFrame5273.PositionPathPoints = [48.36718383498423, 11.34, 58.45738105572413]
keyFrame5273.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5273.PositionMode = 'Path'
keyFrame5273.FocalPointMode = 'Path'
keyFrame5273.ClosedFocalPath = 0
keyFrame5273.ClosedPositionPath = 0

# ====================================================================
keyFrame5274 = CameraKeyFrame()
keyFrame5274.KeyTime = 0.685
keyFrame5274.KeyValues = [0.0]
keyFrame5274.Position = [48.444051811148015, 11.34, 58.410569604266726]
keyFrame5274.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5274.ViewUp = [0.426698715421747, -0.866, -0.2604385063557019]
keyFrame5274.ViewAngle = 30.0
keyFrame5274.ParallelScale = 0.97681
keyFrame5274.PositionPathPoints = [48.444051811148015, 11.34, 58.410569604266726]
keyFrame5274.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5274.PositionMode = 'Path'
keyFrame5274.FocalPointMode = 'Path'
keyFrame5274.ClosedFocalPath = 0
keyFrame5274.ClosedPositionPath = 0

# ====================================================================
keyFrame5275 = CameraKeyFrame()
keyFrame5275.KeyTime = 0.6875
keyFrame5275.KeyValues = [0.0]
keyFrame5275.Position = [48.520826010681915, 11.34, 58.363604510469685]
keyFrame5275.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5275.ViewUp = [0.42617698530684145, -0.866, -0.26129138259081686]
keyFrame5275.ViewAngle = 30.0
keyFrame5275.ParallelScale = 0.97681
keyFrame5275.PositionPathPoints = [48.520826010681915, 11.34, 58.363604510469685]
keyFrame5275.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5275.PositionMode = 'Path'
keyFrame5275.FocalPointMode = 'Path'
keyFrame5275.ClosedFocalPath = 0
keyFrame5275.ClosedPositionPath = 0

# ====================================================================
keyFrame5276 = CameraKeyFrame()
keyFrame5276.KeyTime = 0.69
keyFrame5276.KeyValues = [0.0]
keyFrame5276.Position = [48.59750612648695, 11.34, 58.31648596218962]
keyFrame5276.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5276.ViewUp = [0.42565355048529596, -0.866, -0.26214321365130616]
keyFrame5276.ViewAngle = 30.0
keyFrame5276.ParallelScale = 0.97681
keyFrame5276.PositionPathPoints = [48.59750612648695, 11.34, 58.31648596218962]
keyFrame5276.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5276.PositionMode = 'Path'
keyFrame5276.FocalPointMode = 'Path'
keyFrame5276.ClosedFocalPath = 0
keyFrame5276.ClosedPositionPath = 0

# ====================================================================
keyFrame5277 = CameraKeyFrame()
keyFrame5277.KeyTime = 0.6925
keyFrame5277.KeyValues = [0.0]
keyFrame5277.Position = [48.674091851840856, 11.34, 58.26921414789776]
keyFrame5277.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5277.ViewUp = [0.425128413051414, -0.866, -0.2629939961274161]
keyFrame5277.ViewAngle = 30.0
keyFrame5277.ParallelScale = 0.97681
keyFrame5277.PositionPathPoints = [48.674091851840856, 11.34, 58.26921414789776]
keyFrame5277.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5277.PositionMode = 'Path'
keyFrame5277.FocalPointMode = 'Path'
keyFrame5277.ClosedFocalPath = 0
keyFrame5277.ClosedPositionPath = 0

# ====================================================================
keyFrame5278 = CameraKeyFrame()
keyFrame5278.KeyTime = 0.695
keyFrame5278.KeyValues = [0.0]
keyFrame5278.Position = [48.75058288039938, 11.34, 58.221789256679365]
keyFrame5278.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5278.ViewUp = [0.4246015751063585, -0.866, -0.26384372661347255]
keyFrame5278.ViewAngle = 30.0
keyFrame5278.ParallelScale = 0.97681
keyFrame5278.PositionPathPoints = [48.75058288039938, 11.34, 58.221789256679365]
keyFrame5278.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5278.PositionMode = 'Path'
keyFrame5278.FocalPointMode = 'Path'
keyFrame5278.ClosedFocalPath = 0
keyFrame5278.ClosedPositionPath = 0

# ====================================================================
keyFrame5279 = CameraKeyFrame()
keyFrame5279.KeyTime = 0.6975
keyFrame5279.KeyValues = [0.0]
keyFrame5279.Position = [48.82697890619755, 11.34, 58.17421147823295]
keyFrame5279.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5279.ViewUp = [0.4240730387581447, -0.866, -0.2646924017078932]
keyFrame5279.ViewAngle = 30.0
keyFrame5279.ParallelScale = 0.97681
keyFrame5279.PositionPathPoints = [48.82697890619755, 11.34, 58.17421147823295]
keyFrame5279.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5279.PositionMode = 'Path'
keyFrame5279.FocalPointMode = 'Path'
keyFrame5279.ClosedFocalPath = 0
keyFrame5279.ClosedPositionPath = 0

# ====================================================================
keyFrame5280 = CameraKeyFrame()
keyFrame5280.KeyTime = 0.7
keyFrame5280.KeyValues = [0.0]
keyFrame5280.Position = [48.90327962365093, 11.34, 58.1264810028697]
keyFrame5280.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5280.ViewUp = [0.42354280612163425, -0.866, -0.26554001801319976]
keyFrame5280.ViewAngle = 30.0
keyFrame5280.ParallelScale = 0.97681
keyFrame5280.PositionPathPoints = [48.90327962365093, 11.34, 58.1264810028697]
keyFrame5280.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5280.PositionMode = 'Path'
keyFrame5280.FocalPointMode = 'Path'
keyFrame5280.ClosedFocalPath = 0
keyFrame5280.ClosedPositionPath = 0

# ====================================================================
keyFrame5281 = CameraKeyFrame()
keyFrame5281.KeyTime = 0.7025
keyFrame5281.KeyValues = [0.0]
keyFrame5281.Position = [48.979484727556894, 11.34, 58.078598021512775]
keyFrame5281.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5281.ViewUp = [0.42301087931852793, -0.866, -0.26638657213603006]
keyFrame5281.ViewAngle = 30.0
keyFrame5281.ParallelScale = 0.97681
keyFrame5281.PositionPathPoints = [48.979484727556894, 11.34, 58.078598021512775]
keyFrame5281.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5281.PositionMode = 'Path'
keyFrame5281.FocalPointMode = 'Path'
keyFrame5281.ClosedFocalPath = 0
keyFrame5281.ClosedPositionPath = 0

# ====================================================================
keyFrame5282 = CameraKeyFrame()
keyFrame5282.KeyTime = 0.705
keyFrame5282.KeyValues = [0.0]
keyFrame5282.Position = [49.05559391309592, 11.34, 58.030562725696626]
keyFrame5282.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5282.ViewUp = [0.4224772604773598, -0.866, -0.26723206068714994]
keyFrame5282.ViewAngle = 30.0
keyFrame5282.ParallelScale = 0.97681
keyFrame5282.PositionPathPoints = [49.05559391309592, 11.34, 58.030562725696626]
keyFrame5282.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5282.PositionMode = 'Path'
keyFrame5282.FocalPointMode = 'Path'
keyFrame5282.ClosedFocalPath = 0
keyFrame5282.ClosedPositionPath = 0

# ====================================================================
keyFrame5283 = CameraKeyFrame()
keyFrame5283.KeyTime = 0.7075
keyFrame5283.KeyValues = [0.0]
keyFrame5283.Position = [49.13160687583286, 11.34, 57.98237530756634]
keyFrame5283.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5283.ViewUp = [0.42194195173349003, -0.866, -0.26807648028146575]
keyFrame5283.ViewAngle = 30.0
keyFrame5283.ParallelScale = 0.97681
keyFrame5283.PositionPathPoints = [49.13160687583286, 11.34, 57.98237530756634]
keyFrame5283.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5283.PositionMode = 'Path'
keyFrame5283.FocalPointMode = 'Path'
keyFrame5283.ClosedFocalPath = 0
keyFrame5283.ClosedPositionPath = 0

# ====================================================================
keyFrame5284 = CameraKeyFrame()
keyFrame5284.KeyTime = 0.71
keyFrame5284.KeyValues = [0.0]
keyFrame5284.Position = [49.20752331171816, 11.34, 57.93403595987697]
keyFrame5284.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5284.ViewUp = [0.4214049552290989, -0.866, -0.268919827538036]
keyFrame5284.ViewAngle = 30.0
keyFrame5284.ParallelScale = 0.97681
keyFrame5284.PositionPathPoints = [49.20752331171816, 11.34, 57.93403595987697]
keyFrame5284.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5284.PositionMode = 'Path'
keyFrame5284.FocalPointMode = 'Path'
keyFrame5284.ClosedFocalPath = 0
keyFrame5284.ClosedPositionPath = 0

# ====================================================================
keyFrame5285 = CameraKeyFrame()
keyFrame5285.KeyTime = 0.7125
keyFrame5285.KeyValues = [0.0]
keyFrame5285.Position = [49.28334291708924, 11.34, 57.885544875992856]
keyFrame5285.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5285.ViewUp = [0.4208662731131797, -0.866, -0.2697620990800839]
keyFrame5285.ViewAngle = 30.0
keyFrame5285.ParallelScale = 0.97681
keyFrame5285.PositionPathPoints = [49.28334291708924, 11.34, 57.885544875992856]
keyFrame5285.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5285.PositionMode = 'Path'
keyFrame5285.FocalPointMode = 'Path'
keyFrame5285.ClosedFocalPath = 0
keyFrame5285.ClosedPositionPath = 0

# ====================================================================
keyFrame5286 = CameraKeyFrame()
keyFrame5286.KeyTime = 0.715
keyFrame5286.KeyValues = [0.0]
keyFrame5286.Position = [49.35906538867164, 11.34, 57.83690224988697]
keyFrame5286.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5286.ViewUp = [0.4203259075405478, -0.866, -0.27060329153778473]
keyFrame5286.ViewAngle = 30.0
keyFrame5286.ParallelScale = 0.97681
keyFrame5286.PositionPathPoints = [49.35906538867164, 11.34, 57.83690224988697]
keyFrame5286.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5286.PositionMode = 'Path'
keyFrame5286.FocalPointMode = 'Path'
keyFrame5286.ClosedFocalPath = 0
keyFrame5286.ClosedPositionPath = 0

# ====================================================================
keyFrame5287 = CameraKeyFrame()
keyFrame5287.KeyTime = 0.7175
keyFrame5287.KeyValues = [0.0]
keyFrame5287.Position = [49.43469042358039, 11.34, 57.788108276140235]
keyFrame5287.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5287.ViewUp = [0.4197838606643379, -0.866, -0.27144340156940444]
keyFrame5287.ViewAngle = 30.0
keyFrame5287.ParallelScale = 0.97681
keyFrame5287.PositionPathPoints = [49.43469042358039, 11.34, 57.788108276140235]
keyFrame5287.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5287.PositionMode = 'Path'
keyFrame5287.FocalPointMode = 'Path'
keyFrame5287.ClosedFocalPath = 0
keyFrame5287.ClosedPositionPath = 0

# ====================================================================
keyFrame5288 = CameraKeyFrame()
keyFrame5288.KeyTime = 0.72
keyFrame5288.KeyValues = [0.0]
keyFrame5288.Position = [49.51021771932122, 11.34, 57.73916314994086]
keyFrame5288.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5288.ViewUp = [0.41924013465053284, -0.866, -0.27228242582034606]
keyFrame5288.ViewAngle = 30.0
keyFrame5288.ParallelScale = 0.97681
keyFrame5288.PositionPathPoints = [49.51021771932122, 11.34, 57.73916314994086]
keyFrame5288.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5288.PositionMode = 'Path'
keyFrame5288.FocalPointMode = 'Path'
keyFrame5288.ClosedFocalPath = 0
keyFrame5288.ClosedPositionPath = 0

# ====================================================================
keyFrame5289 = CameraKeyFrame()
keyFrame5289.KeyTime = 0.7225
keyFrame5289.KeyValues = [0.0]
keyFrame5289.Position = [49.585646973791896, 11.34, 57.69006706708367]
keyFrame5289.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5289.ViewUp = [0.4186947316739603, -0.866, -0.27312036093442543]
keyFrame5289.ViewAngle = 30.0
keyFrame5289.ParallelScale = 0.97681
keyFrame5289.PositionPathPoints = [49.585646973791896, 11.34, 57.69006706708367]
keyFrame5289.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5289.PositionMode = 'Path'
keyFrame5289.FocalPointMode = 'Path'
keyFrame5289.ClosedFocalPath = 0
keyFrame5289.ClosedPositionPath = 0

# ====================================================================
keyFrame5290 = CameraKeyFrame()
keyFrame5290.KeyTime = 0.725
keyFrame5290.KeyValues = [0.0]
keyFrame5290.Position = [49.660977885283415, 11.34, 57.640820223969435]
keyFrame5290.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5290.ViewUp = [0.41814765391616876, -0.866, -0.27395720355985204]
keyFrame5290.ViewAngle = 30.0
keyFrame5290.ParallelScale = 0.97681
keyFrame5290.PositionPathPoints = [49.660977885283415, 11.34, 57.640820223969435]
keyFrame5290.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5290.PositionMode = 'Path'
keyFrame5290.FocalPointMode = 'Path'
keyFrame5290.ClosedFocalPath = 0
keyFrame5290.ClosedPositionPath = 0

# ====================================================================
keyFrame5291 = CameraKeyFrame()
keyFrame5291.KeyTime = 0.7275
keyFrame5291.KeyValues = [0.0]
keyFrame5291.Position = [49.73621015248135, 11.34, 57.59142281760421]
keyFrame5291.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5291.ViewUp = [0.41759890356541995, -0.866, -0.27479295034924356]
keyFrame5291.ViewAngle = 30.0
keyFrame5291.ParallelScale = 0.97681
keyFrame5291.PositionPathPoints = [49.73621015248135, 11.34, 57.59142281760421]
keyFrame5291.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5291.PositionMode = 'Path'
keyFrame5291.FocalPointMode = 'Path'
keyFrame5291.ClosedFocalPath = 0
keyFrame5291.ClosedPositionPath = 0

# ====================================================================
keyFrame5292 = CameraKeyFrame()
keyFrame5292.KeyTime = 0.73
keyFrame5292.KeyValues = [0.0]
keyFrame5292.Position = [49.811343474467066, 11.34, 57.54187504559865]
keyFrame5292.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5292.ViewUp = [0.417048482816681, -0.866, -0.27562759795964126]
keyFrame5292.ViewAngle = 30.0
keyFrame5292.ParallelScale = 0.97681
keyFrame5292.PositionPathPoints = [49.811343474467066, 11.34, 57.54187504559865]
keyFrame5292.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5292.PositionMode = 'Path'
keyFrame5292.FocalPointMode = 'Path'
keyFrame5292.ClosedFocalPath = 0
keyFrame5292.ClosedPositionPath = 0

# ====================================================================
keyFrame5293 = CameraKeyFrame()
keyFrame5293.KeyTime = 0.7325
keyFrame5293.KeyValues = [0.0]
keyFrame5293.Position = [49.88637755071903, 11.34, 57.492177106167354]
keyFrame5293.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5293.ViewUp = [0.4164963938716169, -0.866, -0.27646114305252534]
keyFrame5293.ViewAngle = 30.0
keyFrame5293.ParallelScale = 0.97681
keyFrame5293.PositionPathPoints = [49.88637755071903, 11.34, 57.492177106167354]
keyFrame5293.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5293.PositionMode = 'Path'
keyFrame5293.FocalPointMode = 'Path'
keyFrame5293.ClosedFocalPath = 0
keyFrame5293.ClosedPositionPath = 0

# ====================================================================
keyFrame5294 = CameraKeyFrame()
keyFrame5294.KeyTime = 0.735
keyFrame5294.KeyValues = [0.0]
keyFrame5294.Position = [49.96131208111407, 11.34, 57.442329198128185]
keyFrame5294.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5294.ViewUp = [0.4159426389385831, -0.866, -0.2772935822938297]
keyFrame5294.ViewAngle = 30.0
keyFrame5294.ParallelScale = 0.97681
keyFrame5294.PositionPathPoints = [49.96131208111407, 11.34, 57.442329198128185]
keyFrame5294.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5294.PositionMode = 'Path'
keyFrame5294.FocalPointMode = 'Path'
keyFrame5294.ClosedFocalPath = 0
keyFrame5294.ClosedPositionPath = 0

# ====================================================================
keyFrame5295 = CameraKeyFrame()
keyFrame5295.KeyTime = 0.7375
keyFrame5295.KeyValues = [0.0]
keyFrame5295.Position = [50.03614676592865, 11.34, 57.39233152090161]
keyFrame5295.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5295.ViewUp = [0.4153872202326173, -0.866, -0.2781249123539573]
keyFrame5295.ViewAngle = 30.0
keyFrame5295.ParallelScale = 0.97681
keyFrame5295.PositionPathPoints = [50.03614676592865, 11.34, 57.39233152090161]
keyFrame5295.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5295.PositionMode = 'Path'
keyFrame5295.FocalPointMode = 'Path'
keyFrame5295.ClosedFocalPath = 0
keyFrame5295.ClosedPositionPath = 0

# ====================================================================
keyFrame5296 = CameraKeyFrame()
keyFrame5296.KeyTime = 0.74
keyFrame5296.KeyValues = [0.0]
keyFrame5296.Position = [50.11088130584011, 11.34, 57.34218427451002]
keyFrame5296.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5296.ViewUp = [0.4148301399754325, -0.866, -0.2789551299077952]
keyFrame5296.ViewAngle = 30.0
keyFrame5296.ParallelScale = 0.97681
keyFrame5296.PositionPathPoints = [50.11088130584011, 11.34, 57.34218427451002]
keyFrame5296.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5296.PositionMode = 'Path'
keyFrame5296.FocalPointMode = 'Path'
keyFrame5296.ClosedFocalPath = 0
keyFrame5296.ClosedPositionPath = 0

# ====================================================================
keyFrame5297 = CameraKeyFrame()
keyFrame5297.KeyTime = 0.7425
keyFrame5297.KeyValues = [0.0]
keyFrame5297.Position = [50.18551540192803, 11.34, 57.29188765957708]
keyFrame5297.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5297.ViewUp = [0.41427140039540894, -0.866, -0.2797842316347297]
keyFrame5297.ViewAngle = 30.0
keyFrame5297.ParallelScale = 0.97681
keyFrame5297.PositionPathPoints = [50.18551540192803, 11.34, 57.29188765957708]
keyFrame5297.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5297.PositionMode = 'Path'
keyFrame5297.FocalPointMode = 'Path'
keyFrame5297.ClosedFocalPath = 0
keyFrame5297.ClosedPositionPath = 0

# ====================================================================
keyFrame5298 = CameraKeyFrame()
keyFrame5298.KeyTime = 0.745
keyFrame5298.KeyValues = [0.0]
keyFrame5298.Position = [50.2600487556754, 11.34, 57.241441877327034]
keyFrame5298.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5298.ViewUp = [0.41371100372758657, -0.866, -0.28061221421866145]
keyFrame5298.ViewAngle = 30.0
keyFrame5298.ParallelScale = 0.97681
keyFrame5298.PositionPathPoints = [50.2600487556754, 11.34, 57.241441877327034]
keyFrame5298.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5298.PositionMode = 'Path'
keyFrame5298.FocalPointMode = 'Path'
keyFrame5298.ClosedFocalPath = 0
keyFrame5298.ClosedPositionPath = 0

# ====================================================================
keyFrame5299 = CameraKeyFrame()
keyFrame5299.KeyTime = 0.7475
keyFrame5299.KeyValues = [0.0]
keyFrame5299.Position = [50.33448106896992, 11.34, 57.19084712958405]
keyFrame5299.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5299.ViewUp = [0.41314895221365744, -0.866, -0.2814390743480207]
keyFrame5299.ViewAngle = 30.0
keyFrame5299.ParallelScale = 0.97681
keyFrame5299.PositionPathPoints = [50.33448106896992, 11.34, 57.19084712958405]
keyFrame5299.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5299.PositionMode = 'Path'
keyFrame5299.FocalPointMode = 'Path'
keyFrame5299.ClosedFocalPath = 0
keyFrame5299.ClosedPositionPath = 0

# ====================================================================
keyFrame5300 = CameraKeyFrame()
keyFrame5300.KeyTime = 0.75
keyFrame5300.KeyValues = [0.0]
keyFrame5300.Position = [50.40881204410532, 11.34, 57.14010361877155]
keyFrame5300.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5300.ViewUp = [0.4125852481019581, -0.866, -0.2822648087157822]
keyFrame5300.ViewAngle = 30.0
keyFrame5300.ParallelScale = 0.97681
keyFrame5300.PositionPathPoints = [50.40881204410532, 11.34, 57.14010361877155]
keyFrame5300.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5300.PositionMode = 'Path'
keyFrame5300.FocalPointMode = 'Path'
keyFrame5300.ClosedFocalPath = 0
keyFrame5300.ClosedPositionPath = 0

# ====================================================================
keyFrame5301 = CameraKeyFrame()
keyFrame5301.KeyTime = 0.7525
keyFrame5301.KeyValues = [0.0]
keyFrame5301.Position = [50.48304138378258, 11.34, 57.089211547911546]
keyFrame5301.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5301.ViewUp = [0.41201989364746194, -0.866, -0.2830894140194807]
keyFrame5301.ViewAngle = 30.0
keyFrame5301.ParallelScale = 0.97681
keyFrame5301.PositionPathPoints = [50.48304138378258, 11.34, 57.089211547911546]
keyFrame5301.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5301.PositionMode = 'Path'
keyFrame5301.FocalPointMode = 'Path'
keyFrame5301.ClosedFocalPath = 0
keyFrame5301.ClosedPositionPath = 0

# ====================================================================
keyFrame5302 = CameraKeyFrame()
keyFrame5302.KeyTime = 0.755
keyFrame5302.KeyValues = [0.0]
keyFrame5302.Position = [50.55716878984768, 11.34, 57.03817111824867]
keyFrame5302.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5302.ViewUp = [0.4114528911117715, -0.866, -0.2839128869612255]
keyFrame5302.ViewAngle = 30.0
keyFrame5302.ParallelScale = 0.97681
keyFrame5302.PositionPathPoints = [50.55716878984768, 11.34, 57.03817111824867]
keyFrame5302.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5302.PositionMode = 'Path'
keyFrame5302.FocalPointMode = 'Path'
keyFrame5302.ClosedFocalPath = 0
keyFrame5302.ClosedPositionPath = 0

# ====================================================================
keyFrame5303 = CameraKeyFrame()
keyFrame5303.KeyTime = 0.7575
keyFrame5303.KeyValues = [0.0]
keyFrame5303.Position = [50.6311939683485, 11.34, 56.98698253875335]
keyFrame5303.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5303.ViewUp = [0.4108842427631109, -0.866, -0.28473522424771636]
keyFrame5303.ViewAngle = 30.0
keyFrame5303.ParallelScale = 0.97681
keyFrame5303.PositionPathPoints = [50.6311939683485, 11.34, 56.98698253875335]
keyFrame5303.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5303.PositionMode = 'Path'
keyFrame5303.FocalPointMode = 'Path'
keyFrame5303.ClosedFocalPath = 0
keyFrame5303.ClosedPositionPath = 0

# ====================================================================
keyFrame5304 = CameraKeyFrame()
keyFrame5304.KeyTime = 0.76
keyFrame5304.KeyValues = [0.0]
keyFrame5304.Position = [50.70511662160065, 11.34, 56.93564601120376]
keyFrame5304.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5304.ViewUp = [0.4103139508763182, -0.866, -0.2855564225902579]
keyFrame5304.ViewAngle = 30.0
keyFrame5304.ParallelScale = 0.97681
keyFrame5304.PositionPathPoints = [50.70511662160065, 11.34, 56.93564601120376]
keyFrame5304.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5304.PositionMode = 'Path'
keyFrame5304.FocalPointMode = 'Path'
keyFrame5304.ClosedFocalPath = 0
keyFrame5304.ClosedPositionPath = 0

# ====================================================================
keyFrame5305 = CameraKeyFrame()
keyFrame5305.KeyTime = 0.7625
keyFrame5305.KeyValues = [0.0]
keyFrame5305.Position = [50.77893645391579, 11.34, 56.88416174095096]
keyFrame5305.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5305.ViewUp = [0.4097420177328379, -0.866, -0.28637647870477495]
keyFrame5305.ViewAngle = 30.0
keyFrame5305.ParallelScale = 0.97681
keyFrame5305.PositionPathPoints = [50.77893645391579, 11.34, 56.88416174095096]
keyFrame5305.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5305.PositionMode = 'Path'
keyFrame5305.FocalPointMode = 'Path'
keyFrame5305.ClosedFocalPath = 0
keyFrame5305.ClosedPositionPath = 0

# ====================================================================
keyFrame5306 = CameraKeyFrame()
keyFrame5306.KeyTime = 0.765
keyFrame5306.KeyValues = [0.0]
keyFrame5306.Position = [50.85265317001675, 11.34, 56.832529933936755]
keyFrame5306.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5306.ViewUp = [0.409168445620713, -0.866, -0.28719538931182814]
keyFrame5306.ViewAngle = 30.0
keyFrame5306.ParallelScale = 0.97681
keyFrame5306.PositionPathPoints = [50.85265317001675, 11.34, 56.832529933936755]
keyFrame5306.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5306.PositionMode = 'Path'
keyFrame5306.FocalPointMode = 'Path'
keyFrame5306.ClosedFocalPath = 0
keyFrame5306.ClosedPositionPath = 0

# ====================================================================
keyFrame5307 = CameraKeyFrame()
keyFrame5307.KeyTime = 0.7675
keyFrame5307.KeyValues = [0.0]
keyFrame5307.Position = [50.92626647503894, 11.34, 56.78075079669303]
keyFrame5307.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5307.ViewUp = [0.4085932368345776, -0.866, -0.2880131511366283]
keyFrame5307.ViewAngle = 30.0
keyFrame5307.ParallelScale = 0.97681
keyFrame5307.PositionPathPoints = [50.92626647503894, 11.34, 56.78075079669303]
keyFrame5307.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5307.PositionMode = 'Path'
keyFrame5307.FocalPointMode = 'Path'
keyFrame5307.ClosedFocalPath = 0
keyFrame5307.ClosedPositionPath = 0

# ====================================================================
keyFrame5308 = CameraKeyFrame()
keyFrame5308.KeyTime = 0.77
keyFrame5308.KeyValues = [0.0]
keyFrame5308.Position = [50.99977607453148, 11.34, 56.72882453634102]
keyFrame5308.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5308.ViewUp = [0.4080163936756493, -0.866, -0.28882976090905205]
keyFrame5308.ViewAngle = 30.0
keyFrame5308.ParallelScale = 0.97681
keyFrame5308.PositionPathPoints = [50.99977607453148, 11.34, 56.72882453634102]
keyFrame5308.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5308.PositionMode = 'Path'
keyFrame5308.FocalPointMode = 'Path'
keyFrame5308.ClosedFocalPath = 0
keyFrame5308.ClosedPositionPath = 0

# ====================================================================
keyFrame5309 = CameraKeyFrame()
keyFrame5309.KeyTime = 0.7725
keyFrame5309.KeyValues = [0.0]
keyFrame5309.Position = [51.07318167445858, 11.34, 56.67675136059071]
keyFrame5309.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5309.ViewUp = [0.40743791845172145, -0.866, -0.2896452153636569]
keyFrame5309.ViewAngle = 30.0
keyFrame5309.ParallelScale = 0.97681
keyFrame5309.PositionPathPoints = [51.07318167445858, 11.34, 56.67675136059071]
keyFrame5309.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5309.PositionMode = 'Path'
keyFrame5309.FocalPointMode = 'Path'
keyFrame5309.ClosedFocalPath = 0
keyFrame5309.ClosedPositionPath = 0

# ====================================================================
keyFrame5310 = CameraKeyFrame()
keyFrame5310.KeyTime = 0.775
keyFrame5310.KeyValues = [0.0]
keyFrame5310.Position = [51.14648298120072, 11.34, 56.62453147774005]
keyFrame5310.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5310.ViewUp = [0.40685781347715555, -0.866, -0.2904595112396962]
keyFrame5310.ViewAngle = 30.0
keyFrame5310.ParallelScale = 0.97681
keyFrame5310.PositionPathPoints = [51.14648298120072, 11.34, 56.62453147774005]
keyFrame5310.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5310.PositionMode = 'Path'
keyFrame5310.FocalPointMode = 'Path'
keyFrame5310.ClosedFocalPath = 0
keyFrame5310.ClosedPositionPath = 0

# ====================================================================
keyFrame5311 = CameraKeyFrame()
keyFrame5311.KeyTime = 0.7775
keyFrame5311.KeyValues = [0.0]
keyFrame5311.Position = [51.219679701555975, 11.34, 56.572165096674354]
keyFrame5311.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5311.ViewUp = [0.4062760810728736, -0.866, -0.2912726452811344]
keyFrame5311.ViewAngle = 30.0
keyFrame5311.ParallelScale = 0.97681
keyFrame5311.PositionPathPoints = [51.219679701555975, 11.34, 56.572165096674354]
keyFrame5311.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5311.PositionMode = 'Path'
keyFrame5311.FocalPointMode = 'Path'
keyFrame5311.ClosedFocalPath = 0
keyFrame5311.ClosedPositionPath = 0

# ====================================================================
keyFrame5312 = CameraKeyFrame()
keyFrame5312.KeyTime = 0.78
keyFrame5312.KeyValues = [0.0]
keyFrame5312.Position = [51.29277154274125, 11.34, 56.51965242686556]
keyFrame5312.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5312.ViewUp = [0.40569272356635055, -0.866, -0.29208461423666215]
keyFrame5312.ViewAngle = 30.0
keyFrame5312.ParallelScale = 0.97681
keyFrame5312.PositionPathPoints = [51.29277154274125, 11.34, 56.51965242686556]
keyFrame5312.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5312.PositionMode = 'Path'
keyFrame5312.FocalPointMode = 'Path'
keyFrame5312.ClosedFocalPath = 0
keyFrame5312.ClosedPositionPath = 0

# ====================================================================
keyFrame5313 = CameraKeyFrame()
keyFrame5313.KeyTime = 0.7825
keyFrame5313.KeyValues = [0.0]
keyFrame5313.Position = [51.365758212393516, 11.34, 56.46699367837159]
keyFrame5313.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5313.ViewUp = [0.4051077432916066, -0.866, -0.2928954148597115]
keyFrame5313.ViewAngle = 30.0
keyFrame5313.ParallelScale = 0.97681
keyFrame5313.PositionPathPoints = [51.365758212393516, 11.34, 56.46699367837159]
keyFrame5313.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5313.PositionMode = 'Path'
keyFrame5313.FocalPointMode = 'Path'
keyFrame5313.ClosedFocalPath = 0
keyFrame5313.ClosedPositionPath = 0

# ====================================================================
keyFrame5314 = CameraKeyFrame()
keyFrame5314.KeyTime = 0.785
keyFrame5314.KeyValues = [0.0]
keyFrame5314.Position = [51.438639418571114, 11.34, 56.41418906183557]
keyFrame5314.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5314.ViewUp = [0.40452114258919963, -0.866, -0.29370504390847074]
keyFrame5314.ViewAngle = 30.0
keyFrame5314.ParallelScale = 0.97681
keyFrame5314.PositionPathPoints = [51.438639418571114, 11.34, 56.41418906183557]
keyFrame5314.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5314.PositionMode = 'Path'
keyFrame5314.FocalPointMode = 'Path'
keyFrame5314.ClosedFocalPath = 0
keyFrame5314.ClosedPositionPath = 0

# ====================================================================
keyFrame5315 = CameraKeyFrame()
keyFrame5315.KeyTime = 0.7875
keyFrame5315.KeyValues = [0.0]
keyFrame5315.Position = [51.511414869755015, 11.34, 56.361238788485245]
keyFrame5315.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5315.ViewUp = [0.4039329238062175, -0.866, -0.29451349814590005]
keyFrame5315.ViewAngle = 30.0
keyFrame5315.ParallelScale = 0.97681
keyFrame5315.PositionPathPoints = [51.511414869755015, 11.34, 56.361238788485245]
keyFrame5315.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5315.PositionMode = 'Path'
keyFrame5315.FocalPointMode = 'Path'
keyFrame5315.ClosedFocalPath = 0
keyFrame5315.ClosedPositionPath = 0

# ====================================================================
keyFrame5316 = CameraKeyFrame()
keyFrame5316.KeyTime = 0.79
keyFrame5316.KeyValues = [0.0]
keyFrame5316.Position = [51.584084274850014, 11.34, 56.30814307013217]
keyFrame5316.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5316.ViewUp = [0.4033430892962704, -0.866, -0.29532077433974613]
keyFrame5316.ViewAngle = 30.0
keyFrame5316.ParallelScale = 0.97681
keyFrame5316.PositionPathPoints = [51.584084274850014, 11.34, 56.30814307013217]
keyFrame5316.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5316.PositionMode = 'Path'
keyFrame5316.FocalPointMode = 'Path'
keyFrame5316.ClosedFocalPath = 0
keyFrame5316.ClosedPositionPath = 0

# ====================================================================
keyFrame5317 = CameraKeyFrame()
keyFrame5317.KeyTime = 0.7925
keyFrame5317.KeyValues = [0.0]
keyFrame5317.Position = [51.656647343186066, 11.34, 56.25490211917109]
keyFrame5317.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5317.ViewUp = [0.4027516414194833, -0.866, -0.29612686926255755]
keyFrame5317.ViewAngle = 30.0
keyFrame5317.ParallelScale = 0.97681
keyFrame5317.PositionPathPoints = [51.656647343186066, 11.34, 56.25490211917109]
keyFrame5317.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5317.PositionMode = 'Path'
keyFrame5317.FocalPointMode = 'Path'
keyFrame5317.ClosedFocalPath = 0
keyFrame5317.ClosedPositionPath = 0

# ====================================================================
keyFrame5318 = CameraKeyFrame()
keyFrame5318.KeyTime = 0.795
keyFrame5318.KeyValues = [0.0]
keyFrame5318.Position = [51.729103784519495, 11.34, 56.2015161485792]
keyFrame5318.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5318.ViewUp = [0.4021585825424883, -0.866, -0.29693177969169987]
keyFrame5318.ViewAngle = 30.0
keyFrame5318.ParallelScale = 0.97681
keyFrame5318.PositionPathPoints = [51.729103784519495, 11.34, 56.2015161485792]
keyFrame5318.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5318.PositionMode = 'Path'
keyFrame5318.FocalPointMode = 'Path'
keyFrame5318.ClosedFocalPath = 0
keyFrame5318.ClosedPositionPath = 0

# ====================================================================
keyFrame5319 = CameraKeyFrame()
keyFrame5319.KeyTime = 0.7975
keyFrame5319.KeyValues = [0.0]
keyFrame5319.Position = [51.801453309034216, 11.34, 56.147985371915446]
keyFrame5319.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5319.ViewUp = [0.40156391503841704, -0.866, -0.29773550240937086]
keyFrame5319.ViewAngle = 30.0
keyFrame5319.ParallelScale = 0.97681
keyFrame5319.PositionPathPoints = [51.801453309034216, 11.34, 56.147985371915446]
keyFrame5319.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5319.PositionMode = 'Path'
keyFrame5319.FocalPointMode = 'Path'
keyFrame5319.ClosedFocalPath = 0
keyFrame5319.ClosedPositionPath = 0

# ====================================================================
keyFrame5320 = CameraKeyFrame()
keyFrame5320.KeyTime = 0.8
keyFrame5320.KeyValues = [0.0]
keyFrame5320.Position = [51.87369562734308, 11.34, 56.094310003319805]
keyFrame5320.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5320.ViewUp = [0.40096764128689294, -0.866, -0.29853803420261543]
keyFrame5320.ViewAngle = 30.0
keyFrame5320.ParallelScale = 0.97681
keyFrame5320.PositionPathPoints = [51.87369562734308, 11.34, 56.094310003319805]
keyFrame5320.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5320.PositionMode = 'Path'
keyFrame5320.FocalPointMode = 'Path'
keyFrame5320.ClosedFocalPath = 0
keyFrame5320.ClosedPositionPath = 0

# ====================================================================
keyFrame5321 = CameraKeyFrame()
keyFrame5321.KeyTime = 0.8025
keyFrame5321.KeyValues = [0.0]
keyFrame5321.Position = [51.94583045048904, 11.34, 56.04049025751259]
keyFrame5321.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5321.ViewUp = [0.40036976367402366, -0.866, -0.2993393718633408]
keyFrame5321.ViewAngle = 30.0
keyFrame5321.ParallelScale = 0.97681
keyFrame5321.PositionPathPoints = [51.94583045048904, 11.34, 56.04049025751259]
keyFrame5321.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5321.PositionMode = 'Path'
keyFrame5321.FocalPointMode = 'Path'
keyFrame5321.ClosedFocalPath = 0
keyFrame5321.ClosedPositionPath = 0

# ====================================================================
keyFrame5322 = CameraKeyFrame()
keyFrame5322.KeyTime = 0.805
keyFrame5322.KeyValues = [0.0]
keyFrame5322.Position = [52.01785748994642, 11.34, 55.98652634979372]
keyFrame5322.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5322.ViewUp = [0.3997702845883811, -0.866, -0.3001395121808841]
keyFrame5322.ViewAngle = 30.0
keyFrame5322.ParallelScale = 0.97681
keyFrame5322.PositionPathPoints = [52.01785748994642, 11.34, 55.98652634979372]
keyFrame5322.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5322.PositionMode = 'Path'
keyFrame5322.FocalPointMode = 'Path'
keyFrame5322.ClosedFocalPath = 0
keyFrame5322.ClosedPositionPath = 0

# ====================================================================
keyFrame5323 = CameraKeyFrame()
keyFrame5323.KeyTime = 0.8075
keyFrame5323.KeyValues = [0.0]
keyFrame5323.Position = [52.08977645762219, 11.34, 55.93241849604203]
keyFrame5323.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5323.ViewUp = [0.3991692064204149, -0.866, -0.3009384519409532]
keyFrame5323.ViewAngle = 30.0
keyFrame5323.ParallelScale = 0.97681
keyFrame5323.PositionPathPoints = [52.08977645762219, 11.34, 55.93241849604203]
keyFrame5323.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5323.PositionMode = 'Path'
keyFrame5323.FocalPointMode = 'Path'
keyFrame5323.ClosedFocalPath = 0
keyFrame5323.ClosedPositionPath = 0

# ====================================================================
keyFrame5324 = CameraKeyFrame()
keyFrame5324.KeyTime = 0.81
keyFrame5324.KeyValues = [0.0]
keyFrame5324.Position = [52.16158706585719, 11.34, 55.87816691271452]
keyFrame5324.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5324.ViewUp = [0.3985665315741434, -0.866, -0.3017361879473559]
keyFrame5324.ViewAngle = 30.0
keyFrame5324.ParallelScale = 0.97681
keyFrame5324.PositionPathPoints = [52.16158706585719, 11.34, 55.87816691271452]
keyFrame5324.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5324.PositionMode = 'Path'
keyFrame5324.FocalPointMode = 'Path'
keyFrame5324.ClosedFocalPath = 0
keyFrame5324.ClosedPositionPath = 0

# ====================================================================
keyFrame5325 = CameraKeyFrame()
keyFrame5325.KeyTime = 0.8125
keyFrame5325.KeyValues = [0.0]
keyFrame5325.Position = [52.23328902742736, 11.34, 55.82377181684565]
keyFrame5325.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5325.ViewUp = [0.3979622624601859, -0.866, -0.3025327170090964]
keyFrame5325.ViewAngle = 30.0
keyFrame5325.ParallelScale = 0.97681
keyFrame5325.PositionPathPoints = [52.23328902742736, 11.34, 55.82377181684565]
keyFrame5325.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5325.PositionMode = 'Path'
keyFrame5325.FocalPointMode = 'Path'
keyFrame5325.ClosedFocalPath = 0
keyFrame5325.ClosedPositionPath = 0

# ====================================================================
keyFrame5326 = CameraKeyFrame()
keyFrame5326.KeyTime = 0.815
keyFrame5326.KeyValues = [0.0]
keyFrame5326.Position = [52.30488205554501, 11.34, 55.76923342604662]
keyFrame5326.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5326.ViewUp = [0.3973564014955489, -0.866, -0.30332803594000746]
keyFrame5326.ViewAngle = 30.0
keyFrame5326.ParallelScale = 0.97681
keyFrame5326.PositionPathPoints = [52.30488205554501, 11.34, 55.76923342604662]
keyFrame5326.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5326.PositionMode = 'Path'
keyFrame5326.FocalPointMode = 'Path'
keyFrame5326.ClosedFocalPath = 0
keyFrame5326.ClosedPositionPath = 0

# ====================================================================
keyFrame5327 = CameraKeyFrame()
keyFrame5327.KeyTime = 0.8175
keyFrame5327.KeyValues = [0.0]
keyFrame5327.Position = [52.37636586386007, 11.34, 55.714551958504615]
keyFrame5327.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5327.ViewUp = [0.39674895110361735, -0.866, -0.3041221415587639]
keyFrame5327.ViewAngle = 30.0
keyFrame5327.ParallelScale = 0.97681
keyFrame5327.PositionPathPoints = [52.37636586386007, 11.34, 55.714551958504615]
keyFrame5327.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5327.PositionMode = 'Path'
keyFrame5327.FocalPointMode = 'Path'
keyFrame5327.ClosedFocalPath = 0
keyFrame5327.ClosedPositionPath = 0

# ====================================================================
keyFrame5328 = CameraKeyFrame()
keyFrame5328.KeyTime = 0.82
keyFrame5328.KeyValues = [0.0]
keyFrame5328.Position = [52.44774016646129, 11.34, 55.659727632982126]
keyFrame5328.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5328.ViewUp = [0.39613991371414614, -0.866, -0.3049150306888956]
keyFrame5328.ViewAngle = 30.0
keyFrame5328.ParallelScale = 0.97681
keyFrame5328.PositionPathPoints = [52.44774016646129, 11.34, 55.659727632982126]
keyFrame5328.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5328.PositionMode = 'Path'
keyFrame5328.FocalPointMode = 'Path'
keyFrame5328.ClosedFocalPath = 0
keyFrame5328.ClosedPositionPath = 0

# ====================================================================
keyFrame5329 = CameraKeyFrame()
keyFrame5329.KeyTime = 0.8225
keyFrame5329.KeyValues = [0.0]
keyFrame5329.Position = [52.51900467787752, 11.34, 55.60476066881618]
keyFrame5329.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5329.ViewUp = [0.39552929176325125, -0.866, -0.3057067001588006]
keyFrame5329.ViewAngle = 30.0
keyFrame5329.ParallelScale = 0.97681
keyFrame5329.PositionPathPoints = [52.51900467787752, 11.34, 55.60476066881618]
keyFrame5329.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5329.PositionMode = 'Path'
keyFrame5329.FocalPointMode = 'Path'
keyFrame5329.ClosedFocalPath = 0
keyFrame5329.ClosedPositionPath = 0

# ====================================================================
keyFrame5330 = CameraKeyFrame()
keyFrame5330.KeyTime = 0.825
keyFrame5330.KeyValues = [0.0]
keyFrame5330.Position = [52.59015911307891, 11.34, 55.54965128591761]
keyFrame5330.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5330.ViewUp = [0.39491708769340106, -0.866, -0.30649714680175844]
keyFrame5330.ViewAngle = 30.0
keyFrame5330.ParallelScale = 0.97681
keyFrame5330.PositionPathPoints = [52.59015911307891, 11.34, 55.54965128591761]
keyFrame5330.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5330.PositionMode = 'Path'
keyFrame5330.FocalPointMode = 'Path'
keyFrame5330.ClosedFocalPath = 0
keyFrame5330.ClosedPositionPath = 0

# ====================================================================
keyFrame5331 = CameraKeyFrame()
keyFrame5331.KeyTime = 0.8275
keyFrame5331.KeyValues = [0.0]
keyFrame5331.Position = [52.66120318747821, 11.34, 55.49439970477034]
keyFrame5331.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5331.ViewUp = [0.39430330395340785, -0.866, -0.3072863674559434]
keyFrame5331.ViewAngle = 30.0
keyFrame5331.ParallelScale = 0.97681
keyFrame5331.PositionPathPoints = [52.66120318747821, 11.34, 55.49439970477034]
keyFrame5331.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5331.PositionMode = 'Path'
keyFrame5331.FocalPointMode = 'Path'
keyFrame5331.ClosedFocalPath = 0
keyFrame5331.ClosedPositionPath = 0

# ====================================================================
keyFrame5332 = CameraKeyFrame()
keyFrame5332.KeyTime = 0.83
keyFrame5332.KeyValues = [0.0]
keyFrame5332.Position = [52.73213661689391, 11.34, 55.4390061463744]
keyFrame5332.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5332.ViewUp = [0.3936879429984191, -0.866, -0.30807435896443747]
keyFrame5332.ViewAngle = 30.0
keyFrame5332.ParallelScale = 0.97681
keyFrame5332.PositionPathPoints = [52.73213661689391, 11.34, 55.4390061463744]
keyFrame5332.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5332.PositionMode = 'Path'
keyFrame5332.FocalPointMode = 'Path'
keyFrame5332.ClosedFocalPath = 0
keyFrame5332.ClosedPositionPath = 0

# ====================================================================
keyFrame5333 = CameraKeyFrame()
keyFrame5333.KeyTime = 0.8325
keyFrame5333.KeyValues = [0.0]
keyFrame5333.Position = [52.80295911722598, 11.34, 55.38347083176383]
keyFrame5333.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5333.ViewUp = [0.3930710072899084, -0.866, -0.3088611181752436]
keyFrame5333.ViewAngle = 30.0
keyFrame5333.ParallelScale = 0.97681
keyFrame5333.PositionPathPoints = [52.80295911722598, 11.34, 55.38347083176383]
keyFrame5333.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5333.PositionMode = 'Path'
keyFrame5333.FocalPointMode = 'Path'
keyFrame5333.ClosedFocalPath = 0
keyFrame5333.ClosedPositionPath = 0

# ====================================================================
keyFrame5334 = CameraKeyFrame()
keyFrame5334.KeyTime = 0.835
keyFrame5334.KeyValues = [0.0]
keyFrame5334.Position = [52.87367040507755, 11.34, 55.327793982923396]
keyFrame5334.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5334.ViewUp = [0.3924524992956675, -0.866, -0.3096466419412991]
keyFrame5334.ViewAngle = 30.0
keyFrame5334.ParallelScale = 0.97681
keyFrame5334.PositionPathPoints = [52.87367040507755, 11.34, 55.327793982923396]
keyFrame5334.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5334.PositionMode = 'Path'
keyFrame5334.FocalPointMode = 'Path'
keyFrame5334.ClosedFocalPath = 0
keyFrame5334.ClosedPositionPath = 0

# ====================================================================
keyFrame5335 = CameraKeyFrame()
keyFrame5335.KeyTime = 0.8375
keyFrame5335.KeyValues = [0.0]
keyFrame5335.Position = [52.94427019759554, 11.34, 55.27197582255035]
keyFrame5335.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5335.ViewUp = [0.39183242148979697, -0.866, -0.3104309271204884]
keyFrame5335.ViewAngle = 30.0
keyFrame5335.ParallelScale = 0.97681
keyFrame5335.PositionPathPoints = [52.94427019759554, 11.34, 55.27197582255035]
keyFrame5335.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5335.PositionMode = 'Path'
keyFrame5335.FocalPointMode = 'Path'
keyFrame5335.ClosedFocalPath = 0
keyFrame5335.ClosedPositionPath = 0

# ====================================================================
keyFrame5336 = CameraKeyFrame()
keyFrame5336.KeyTime = 0.84
keyFrame5336.KeyValues = [0.0]
keyFrame5336.Position = [53.014758212373565, 11.34, 55.2160165739083]
keyFrame5336.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5336.ViewUp = [0.39121077635269785, -0.866, -0.3112139705756568]
keyFrame5336.ViewAngle = 30.0
keyFrame5336.ParallelScale = 0.97681
keyFrame5336.PositionPathPoints = [53.014758212373565, 11.34, 55.2160165739083]
keyFrame5336.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5336.PositionMode = 'Path'
keyFrame5336.FocalPointMode = 'Path'
keyFrame5336.ClosedFocalPath = 0
keyFrame5336.ClosedPositionPath = 0

# ====================================================================
keyFrame5337 = CameraKeyFrame()
keyFrame5337.KeyTime = 0.8425
keyFrame5337.KeyValues = [0.0]
keyFrame5337.Position = [53.08513416745306, 11.34, 55.15991646082636]
keyFrame5337.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5337.ViewUp = [0.39058756637106296, -0.866, -0.3119957691746231]
keyFrame5337.ViewAngle = 30.0
keyFrame5337.ParallelScale = 0.97681
keyFrame5337.PositionPathPoints = [53.08513416745306, 11.34, 55.15991646082636]
keyFrame5337.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5337.PositionMode = 'Path'
keyFrame5337.FocalPointMode = 'Path'
keyFrame5337.ClosedFocalPath = 0
keyFrame5337.ClosedPositionPath = 0

# ====================================================================
keyFrame5338 = CameraKeyFrame()
keyFrame5338.KeyTime = 0.845
keyFrame5338.KeyValues = [0.0]
keyFrame5338.Position = [53.15539778132457, 11.34, 55.10367570769833]
keyFrame5338.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5338.ViewUp = [0.38996279403786804, -0.866, -0.31277631979019316]
keyFrame5338.ViewAngle = 30.0
keyFrame5338.ParallelScale = 0.97681
keyFrame5338.PositionPathPoints = [53.15539778132457, 11.34, 55.10367570769833]
keyFrame5338.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5338.PositionMode = 'Path'
keyFrame5338.FocalPointMode = 'Path'
keyFrame5338.ClosedFocalPath = 0
keyFrame5338.ClosedPositionPath = 0

# ====================================================================
keyFrame5339 = CameraKeyFrame()
keyFrame5339.KeyTime = 0.8475
keyFrame5339.KeyValues = [0.0]
keyFrame5339.Position = [53.225548772928775, 11.34, 55.04729453948189]
keyFrame5339.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5339.ViewUp = [0.3893364618523633, -0.866, -0.31355561930017284]
keyFrame5339.ViewAngle = 30.0
keyFrame5339.ParallelScale = 0.97681
keyFrame5339.PositionPathPoints = [53.225548772928775, 11.34, 55.04729453948189]
keyFrame5339.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5339.PositionMode = 'Path'
keyFrame5339.FocalPointMode = 'Path'
keyFrame5339.ClosedFocalPath = 0
keyFrame5339.ClosedPositionPath = 0

# ====================================================================
keyFrame5340 = CameraKeyFrame()
keyFrame5340.KeyTime = 0.85
keyFrame5340.KeyValues = [0.0]
keyFrame5340.Position = [53.29558686165784, 11.34, 54.99077318169775]
keyFrame5340.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5340.ViewUp = [0.38870857232006467, -0.866, -0.3143336645873814]
keyFrame5340.ViewAngle = 30.0
keyFrame5340.ParallelScale = 0.97681
keyFrame5340.PositionPathPoints = [53.29558686165784, 11.34, 54.99077318169775]
keyFrame5340.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5340.PositionMode = 'Path'
keyFrame5340.FocalPointMode = 'Path'
keyFrame5340.ClosedFocalPath = 0
keyFrame5340.ClosedPositionPath = 0

# ====================================================================
keyFrame5341 = CameraKeyFrame()
keyFrame5341.KeyTime = 0.8525
keyFrame5341.KeyValues = [0.0]
keyFrame5341.Position = [53.36551176735645, 11.34, 54.934111860428814]
keyFrame5341.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5341.ViewUp = [0.388079127952745, -0.866, -0.3151104525396645]
keyFrame5341.ViewAngle = 30.0
keyFrame5341.ParallelScale = 0.97681
keyFrame5341.PositionPathPoints = [53.36551176735645, 11.34, 54.934111860428814]
keyFrame5341.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5341.PositionMode = 'Path'
keyFrame5341.FocalPointMode = 'Path'
keyFrame5341.ClosedFocalPath = 0
keyFrame5341.ClosedPositionPath = 0

# ====================================================================
keyFrame5342 = CameraKeyFrame()
keyFrame5342.KeyTime = 0.855
keyFrame5342.KeyValues = [0.0]
keyFrame5342.Position = [53.43532321032305, 11.34, 54.877310802319364]
keyFrame5342.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5342.ViewUp = [0.3874481312684256, -0.866, -0.31588598004990764]
keyFrame5342.ViewAngle = 30.0
keyFrame5342.ParallelScale = 0.97681
keyFrame5342.PositionPathPoints = [53.43532321032305, 11.34, 54.877310802319364]
keyFrame5342.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5342.PositionMode = 'Path'
keyFrame5342.FocalPointMode = 'Path'
keyFrame5342.ClosedFocalPath = 0
keyFrame5342.ClosedPositionPath = 0

# ====================================================================
keyFrame5343 = CameraKeyFrame()
keyFrame5343.KeyTime = 0.8575
keyFrame5343.KeyValues = [0.0]
keyFrame5343.Position = [53.50502091131101, 11.34, 54.82037023457419]
keyFrame5343.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5343.ViewUp = [0.3868155847913672, -0.866, -0.3166602440160489]
keyFrame5343.ViewAngle = 30.0
keyFrame5343.ParallelScale = 0.97681
keyFrame5343.PositionPathPoints = [53.50502091131101, 11.34, 54.82037023457419]
keyFrame5343.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5343.PositionMode = 'Path'
keyFrame5343.FocalPointMode = 'Path'
keyFrame5343.ClosedFocalPath = 0
keyFrame5343.ClosedPositionPath = 0

# ====================================================================
keyFrame5344 = CameraKeyFrame()
keyFrame5344.KeyTime = 0.86
keyFrame5344.KeyValues = [0.0]
keyFrame5344.Position = [53.57460459152978, 11.34, 54.763290384957784]
keyFrame5344.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5344.ViewUp = [0.38618149105206173, -0.866, -0.31743324134109263]
keyFrame5344.ViewAngle = 30.0
keyFrame5344.ParallelScale = 0.97681
keyFrame5344.PositionPathPoints = [53.57460459152978, 11.34, 54.763290384957784]
keyFrame5344.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5344.PositionMode = 'Path'
keyFrame5344.FocalPointMode = 'Path'
keyFrame5344.ClosedFocalPath = 0
keyFrame5344.ClosedPositionPath = 0

# ====================================================================
keyFrame5345 = CameraKeyFrame()
keyFrame5345.KeyTime = 0.8625
keyFrame5345.KeyValues = [0.0]
keyFrame5345.Position = [53.644073972646055, 11.34, 54.70607148179345]
keyFrame5345.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5345.ViewUp = [0.38554585258722335, -0.866, -0.3182049689331223]
keyFrame5345.ViewAngle = 30.0
keyFrame5345.ParallelScale = 0.97681
keyFrame5345.PositionPathPoints = [53.644073972646055, 11.34, 54.70607148179345]
keyFrame5345.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5345.PositionMode = 'Path'
keyFrame5345.FocalPointMode = 'Path'
keyFrame5345.ClosedFocalPath = 0
keyFrame5345.ClosedPositionPath = 0

# ====================================================================
keyFrame5346 = CameraKeyFrame()
keyFrame5346.KeyTime = 0.865
keyFrame5346.KeyValues = [0.0]
keyFrame5346.Position = [53.71342877678498, 11.34, 54.648713753962504]
keyFrame5346.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5346.ViewUp = [0.38490867193977985, -0.866, -0.3189754237053138]
keyFrame5346.ViewAngle = 30.0
keyFrame5346.ParallelScale = 0.97681
keyFrame5346.PositionPathPoints = [53.71342877678498, 11.34, 54.648713753962504]
keyFrame5346.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5346.PositionMode = 'Path'
keyFrame5346.FocalPointMode = 'Path'
keyFrame5346.ClosedFocalPath = 0
keyFrame5346.ClosedPositionPath = 0

# ====================================================================
keyFrame5347 = CameraKeyFrame()
keyFrame5347.KeyTime = 0.8675
keyFrame5347.KeyValues = [0.0]
keyFrame5347.Position = [53.78266872653124, 11.34, 54.59121743090336]
keyFrame5347.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5347.ViewUp = [0.38426995165886385, -0.866, -0.31974460257594856]
keyFrame5347.ViewAngle = 30.0
keyFrame5347.ParallelScale = 0.97681
keyFrame5347.PositionPathPoints = [53.78266872653124, 11.34, 54.59121743090336]
keyFrame5347.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5347.PositionMode = 'Path'
keyFrame5347.FocalPointMode = 'Path'
keyFrame5347.ClosedFocalPath = 0
keyFrame5347.ClosedPositionPath = 0

# ====================================================================
keyFrame5348 = CameraKeyFrame()
keyFrame5348.KeyTime = 0.87
keyFrame5348.KeyValues = [0.0]
keyFrame5348.Position = [53.85179354493032, 11.34, 54.53358274261076]
keyFrame5348.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5348.ViewUp = [0.3836296942998045, -0.866, -0.32051250246842694]
keyFrame5348.ViewAngle = 30.0
keyFrame5348.ParallelScale = 0.97681
keyFrame5348.PositionPathPoints = [53.85179354493032, 11.34, 54.53358274261076]
keyFrame5348.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5348.PositionMode = 'Path'
keyFrame5348.FocalPointMode = 'Path'
keyFrame5348.ClosedFocalPath = 0
keyFrame5348.ClosedPositionPath = 0

# ====================================================================
keyFrame5349 = CameraKeyFrame()
keyFrame5349.KeyTime = 0.8725
keyFrame5349.KeyValues = [0.0]
keyFrame5349.Position = [53.92080295548956, 11.34, 54.475809919634806]
keyFrame5349.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5349.ViewUp = [0.38298790242411823, -0.866, -0.32127912031128114]
keyFrame5349.ViewAngle = 30.0
keyFrame5349.ParallelScale = 0.97681
keyFrame5349.PositionPathPoints = [53.92080295548956, 11.34, 54.475809919634806]
keyFrame5349.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5349.PositionMode = 'Path'
keyFrame5349.FocalPointMode = 'Path'
keyFrame5349.ClosedFocalPath = 0
keyFrame5349.ClosedPositionPath = 0

# ====================================================================
keyFrame5350 = CameraKeyFrame()
keyFrame5350.KeyTime = 0.875
keyFrame5350.KeyValues = [0.0]
keyFrame5350.Position = [53.989696682179414, 11.34, 54.417899193080196]
keyFrame5350.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5350.ViewUp = [0.38234457859950055, -0.866, -0.3220444530381885]
keyFrame5350.ViewAngle = 30.0
keyFrame5350.ParallelScale = 0.97681
keyFrame5350.PositionPathPoints = [53.989696682179414, 11.34, 54.417899193080196]
keyFrame5350.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5350.PositionMode = 'Path'
keyFrame5350.FocalPointMode = 'Path'
keyFrame5350.ClosedFocalPath = 0
keyFrame5350.ClosedPositionPath = 0

# ====================================================================
keyFrame5351 = CameraKeyFrame()
keyFrame5351.KeyTime = 0.8775
keyFrame5351.KeyValues = [0.0]
keyFrame5351.Position = [54.0584744494345, 11.34, 54.35985079460529]
keyFrame5351.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5351.ViewUp = [0.38169972539981717, -0.866, -0.3228084975879848]
keyFrame5351.ViewAngle = 30.0
keyFrame5351.ParallelScale = 0.97681
keyFrame5351.PositionPathPoints = [54.0584744494345, 11.34, 54.35985079460529]
keyFrame5351.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5351.PositionMode = 'Path'
keyFrame5351.FocalPointMode = 'Path'
keyFrame5351.ClosedFocalPath = 0
keyFrame5351.ClosedPositionPath = 0

# ====================================================================
keyFrame5352 = CameraKeyFrame()
keyFrame5352.KeyTime = 0.88
keyFrame5352.KeyValues = [0.0]
keyFrame5352.Position = [54.12713598215488, 11.34, 54.30166495642131]
keyFrame5352.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5352.ViewUp = [0.38105334540509533, -0.866, -0.3235712509046771]
keyFrame5352.ViewAngle = 30.0
keyFrame5352.ParallelScale = 0.97681
keyFrame5352.PositionPathPoints = [54.12713598215488, 11.34, 54.30166495642131]
keyFrame5352.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5352.PositionMode = 'Path'
keyFrame5352.FocalPointMode = 'Path'
keyFrame5352.ClosedFocalPath = 0
keyFrame5352.ClosedPositionPath = 0

# ====================================================================
keyFrame5353 = CameraKeyFrame()
keyFrame5353.KeyTime = 0.8825
keyFrame5353.KeyValues = [0.0]
keyFrame5353.Position = [54.19568100570709, 11.34, 54.24334191129138]
keyFrame5353.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5353.ViewUp = [0.3804054412015152, -0.866, -0.3243327099374575]
keyFrame5353.ViewAngle = 30.0
keyFrame5353.ParallelScale = 0.97681
keyFrame5353.PositionPathPoints = [54.19568100570709, 11.34, 54.24334191129138]
keyFrame5353.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5353.PositionMode = 'Path'
keyFrame5353.FocalPointMode = 'Path'
keyFrame5353.ClosedFocalPath = 0
keyFrame5353.ClosedPositionPath = 0

# ====================================================================
keyFrame5354 = CameraKeyFrame()
keyFrame5354.KeyTime = 0.885
keyFrame5354.KeyValues = [0.0]
keyFrame5354.Position = [54.26410924592538, 11.34, 54.184881892529724]
keyFrame5354.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5354.ViewUp = [0.3797560153814011, -0.866, -0.3250928716407157]
keyFrame5354.ViewAngle = 30.0
keyFrame5354.ParallelScale = 0.97681
keyFrame5354.PositionPathPoints = [54.26410924592538, 11.34, 54.184881892529724]
keyFrame5354.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5354.PositionMode = 'Path'
keyFrame5354.FocalPointMode = 'Path'
keyFrame5354.ClosedFocalPath = 0
keyFrame5354.ClosedPositionPath = 0

# ====================================================================
keyFrame5355 = CameraKeyFrame()
keyFrame5355.KeyTime = 0.8875
keyFrame5355.KeyValues = [0.0]
keyFrame5355.Position = [54.332420429112815, 11.34, 54.12628513400076]
keyFrame5355.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5355.ViewUp = [0.37910507054321274, -0.866, -0.3258517329740527]
keyFrame5355.ViewAngle = 30.0
keyFrame5355.ParallelScale = 0.97681
keyFrame5355.PositionPathPoints = [54.332420429112815, 11.34, 54.12628513400076]
keyFrame5355.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5355.PositionMode = 'Path'
keyFrame5355.FocalPointMode = 'Path'
keyFrame5355.ClosedFocalPath = 0
keyFrame5355.ClosedPositionPath = 0

# ====================================================================
keyFrame5356 = CameraKeyFrame()
keyFrame5356.KeyTime = 0.89
keyFrame5356.KeyValues = [0.0]
keyFrame5356.Position = [54.40061428204247, 11.34, 54.0675518701182]
keyFrame5356.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5356.ViewUp = [0.37845260929153696, -0.866, -0.32660929090229346]
keyFrame5356.ViewAngle = 30.0
keyFrame5356.ParallelScale = 0.97681
keyFrame5356.PositionPathPoints = [54.40061428204247, 11.34, 54.0675518701182]
keyFrame5356.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5356.PositionMode = 'Path'
keyFrame5356.FocalPointMode = 'Path'
keyFrame5356.ClosedFocalPath = 0
keyFrame5356.ClosedPositionPath = 0

# ====================================================================
keyFrame5357 = CameraKeyFrame()
keyFrame5357.KeyTime = 0.8925
keyFrame5357.KeyValues = [0.0]
keyFrame5357.Position = [54.46869053195849, 11.34, 54.00868233584423]
keyFrame5357.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5357.ViewUp = [0.3777986342368258, -0.866, -0.3273655423954022]
keyFrame5357.ViewAngle = 30.0
keyFrame5357.ParallelScale = 0.97681
keyFrame5357.PositionPathPoints = [54.46869053195849, 11.34, 54.00868233584423]
keyFrame5357.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5357.PositionMode = 'Path'
keyFrame5357.FocalPointMode = 'Path'
keyFrame5357.ClosedFocalPath = 0
keyFrame5357.ClosedPositionPath = 0

# ====================================================================
keyFrame5358 = CameraKeyFrame()
keyFrame5358.KeyTime = 0.895
keyFrame5358.KeyValues = [0.0]
keyFrame5358.Position = [54.53664890657734, 11.34, 53.94967676668852]
keyFrame5358.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5358.ViewUp = [0.3771431479888792, -0.866, -0.32812048442595926]
keyFrame5358.ViewAngle = 30.0
keyFrame5358.ParallelScale = 0.97681
keyFrame5358.PositionPathPoints = [54.53664890657734, 11.34, 53.94967676668852]
keyFrame5358.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5358.PositionMode = 'Path'
keyFrame5358.FocalPointMode = 'Path'
keyFrame5358.ClosedFocalPath = 0
keyFrame5358.ClosedPositionPath = 0

# ====================================================================
keyFrame5359 = CameraKeyFrame()
keyFrame5359.KeyTime = 0.8975
keyFrame5359.KeyValues = [0.0]
keyFrame5359.Position = [54.604489134088865, 11.34, 53.89053539870743]
keyFrame5359.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5359.ViewUp = [0.37648615316664386, -0.866, -0.3288741139729954]
keyFrame5359.ViewAngle = 30.0
keyFrame5359.ParallelScale = 0.97681
keyFrame5359.PositionPathPoints = [54.604489134088865, 11.34, 53.89053539870743]
keyFrame5359.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5359.PositionMode = 'Path'
keyFrame5359.FocalPointMode = 'Path'
keyFrame5359.ClosedFocalPath = 0
keyFrame5359.ClosedPositionPath = 0

# ====================================================================
keyFrame5360 = CameraKeyFrame()
keyFrame5360.KeyTime = 0.9
keyFrame5360.KeyValues = [0.0]
keyFrame5360.Position = [54.67221094315748, 11.34, 53.83125846850307]
keyFrame5360.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5360.ViewUp = [0.37582765239801996, -0.866, -0.32962642802193326]
keyFrame5360.ViewAngle = 30.0
keyFrame5360.ParallelScale = 0.97681
keyFrame5360.PositionPathPoints = [54.67221094315748, 11.34, 53.83125846850307]
keyFrame5360.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5360.PositionMode = 'Path'
keyFrame5360.FocalPointMode = 'Path'
keyFrame5360.ClosedFocalPath = 0
keyFrame5360.ClosedPositionPath = 0

# ====================================================================
keyFrame5361 = CameraKeyFrame()
keyFrame5361.KeyTime = 0.9025
keyFrame5361.KeyValues = [0.0]
keyFrame5361.Position = [54.7398140629233, 11.34, 53.7718462132224]
keyFrame5361.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5361.ViewUp = [0.37516764831694227, -0.866, -0.3303774235634668]
keyFrame5361.ViewAngle = 30.0
keyFrame5361.ParallelScale = 0.97681
keyFrame5361.PositionPathPoints = [54.7398140629233, 11.34, 53.7718462132224]
keyFrame5361.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5361.PositionMode = 'Path'
keyFrame5361.FocalPointMode = 'Path'
keyFrame5361.ClosedFocalPath = 0
keyFrame5361.ClosedPositionPath = 0

# ====================================================================
keyFrame5362 = CameraKeyFrame()
keyFrame5362.KeyTime = 0.905
keyFrame5362.KeyValues = [0.0]
keyFrame5362.Position = [54.807298223003244, 11.34, 53.712298870556346]
keyFrame5362.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5362.ViewUp = [0.3745061435633703, -0.866, -0.3311270975935735]
keyFrame5362.ViewAngle = 30.0
keyFrame5362.ParallelScale = 0.97681
keyFrame5362.PositionPathPoints = [54.807298223003244, 11.34, 53.712298870556346]
keyFrame5362.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5362.PositionMode = 'Path'
keyFrame5362.FocalPointMode = 'Path'
keyFrame5362.ClosedFocalPath = 0
keyFrame5362.ClosedPositionPath = 0

# ====================================================================
keyFrame5363 = CameraKeyFrame()
keyFrame5363.KeyTime = 0.9075
keyFrame5363.KeyValues = [0.0]
keyFrame5363.Position = [54.87466315349219, 11.34, 53.65261667873887]
keyFrame5363.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5363.ViewUp = [0.37384314078327885, -0.866, -0.33187544711352807]
keyFrame5363.ViewAngle = 30.0
keyFrame5363.ParallelScale = 0.97681
keyFrame5363.PositionPathPoints = [54.87466315349219, 11.34, 53.65261667873887]
keyFrame5363.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5363.PositionMode = 'Path'
keyFrame5363.FocalPointMode = 'Path'
keyFrame5363.ClosedFocalPath = 0
keyFrame5363.ClosedPositionPath = 0

# ====================================================================
keyFrame5364 = CameraKeyFrame()
keyFrame5364.KeyTime = 0.91
keyFrame5364.KeyValues = [0.0]
keyFrame5364.Position = [54.94190858496415, 11.34, 53.5927998765461]
keyFrame5364.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5364.ViewUp = [0.37317864262864836, -0.866, -0.33262246912991433]
keyFrame5364.ViewAngle = 30.0
keyFrame5364.ParallelScale = 0.97681
keyFrame5364.PositionPathPoints = [54.94190858496415, 11.34, 53.5927998765461]
keyFrame5364.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5364.PositionMode = 'Path'
keyFrame5364.FocalPointMode = 'Path'
keyFrame5364.ClosedFocalPath = 0
keyFrame5364.ClosedPositionPath = 0

# ====================================================================
keyFrame5365 = CameraKeyFrame()
keyFrame5365.KeyTime = 0.9125
keyFrame5365.KeyValues = [0.0]
keyFrame5365.Position = [55.00903424847333, 11.34, 53.5328487032954]
keyFrame5365.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5365.ViewUp = [0.3725126517574555, -0.866, -0.33336816065463887]
keyFrame5365.ViewAngle = 30.0
keyFrame5365.ParallelScale = 0.97681
keyFrame5365.PositionPathPoints = [55.00903424847333, 11.34, 53.5328487032954]
keyFrame5365.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5365.PositionMode = 'Path'
keyFrame5365.FocalPointMode = 'Path'
keyFrame5365.ClosedFocalPath = 0
keyFrame5365.ClosedPositionPath = 0

# ====================================================================
keyFrame5366 = CameraKeyFrame()
keyFrame5366.KeyTime = 0.915
keyFrame5366.KeyValues = [0.0]
keyFrame5366.Position = [55.076039875555296, 11.34, 53.47276339884444]
keyFrame5366.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5366.ViewUp = [0.37184517083366353, -0.866, -0.33411251870494335]
keyFrame5366.ViewAngle = 30.0
keyFrame5366.ParallelScale = 0.97681
keyFrame5366.PositionPathPoints = [55.076039875555296, 11.34, 53.47276339884444]
keyFrame5366.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5366.PositionMode = 'Path'
keyFrame5366.FocalPointMode = 'Path'
keyFrame5366.ClosedFocalPath = 0
keyFrame5366.ClosedPositionPath = 0

# ====================================================================
keyFrame5367 = CameraKeyFrame()
keyFrame5367.KeyTime = 0.9175
keyFrame5367.KeyValues = [0.0]
keyFrame5367.Position = [55.14292519822813, 11.34, 53.412544203590315]
keyFrame5367.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5367.ViewUp = [0.3711762025272127, -0.866, -0.3348555403034177]
keyFrame5367.ViewAngle = 30.0
keyFrame5367.ParallelScale = 0.97681
keyFrame5367.PositionPathPoints = [55.14292519822813, 11.34, 53.412544203590315]
keyFrame5367.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5367.PositionMode = 'Path'
keyFrame5367.FocalPointMode = 'Path'
keyFrame5367.ClosedFocalPath = 0
keyFrame5367.ClosedPositionPath = 0

# ====================================================================
keyFrame5368 = CameraKeyFrame()
keyFrame5368.KeyTime = 0.92
keyFrame5368.KeyValues = [0.0]
keyFrame5368.Position = [55.209689948993486, 11.34, 53.352191358468595]
keyFrame5368.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5368.ViewUp = [0.3705057495140106, -0.866, -0.33559722247801266]
keyFrame5368.ViewAngle = 30.0
keyFrame5368.ParallelScale = 0.97681
keyFrame5368.PositionPathPoints = [55.209689948993486, 11.34, 53.352191358468595]
keyFrame5368.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5368.PositionMode = 'Path'
keyFrame5368.FocalPointMode = 'Path'
keyFrame5368.ClosedFocalPath = 0
keyFrame5368.ClosedPositionPath = 0

# ====================================================================
keyFrame5369 = CameraKeyFrame()
keyFrame5369.KeyTime = 0.9225
keyFrame5369.KeyValues = [0.0]
keyFrame5369.Position = [55.276333860837795, 11.34, 53.291705104952406]
keyFrame5369.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5369.ViewUp = [0.36983381447592295, -0.866, -0.33633756226205286]
keyFrame5369.ViewAngle = 30.0
keyFrame5369.ParallelScale = 0.97681
keyFrame5369.PositionPathPoints = [55.276333860837795, 11.34, 53.291705104952406]
keyFrame5369.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5369.PositionMode = 'Path'
keyFrame5369.FocalPointMode = 'Path'
keyFrame5369.ClosedFocalPath = 0
keyFrame5369.ClosedPositionPath = 0

# ====================================================================
keyFrame5370 = CameraKeyFrame()
keyFrame5370.KeyTime = 0.925
keyFrame5370.KeyValues = [0.0]
keyFrame5370.Position = [55.342856667233306, 11.34, 53.23108568505154]
keyFrame5370.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5370.ViewUp = [0.3691604001007637, -0.866, -0.3370765566942495]
keyFrame5370.ViewAngle = 30.0
keyFrame5370.ParallelScale = 0.97681
keyFrame5370.PositionPathPoints = [55.342856667233306, 11.34, 53.23108568505154]
keyFrame5370.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5370.PositionMode = 'Path'
keyFrame5370.FocalPointMode = 'Path'
keyFrame5370.ClosedFocalPath = 0
keyFrame5370.ClosedPositionPath = 0

# ====================================================================
keyFrame5371 = CameraKeyFrame()
keyFrame5371.KeyTime = 0.9275
keyFrame5371.KeyValues = [0.0]
keyFrame5371.Position = [55.409258102139276, 11.34, 53.170333341311455]
keyFrame5371.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5371.ViewUp = [0.3684855090822855, -0.866, -0.3378142028187133]
keyFrame5371.ViewAngle = 30.0
keyFrame5371.ParallelScale = 0.97681
keyFrame5371.PositionPathPoints = [55.409258102139276, 11.34, 53.170333341311455]
keyFrame5371.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5371.PositionMode = 'Path'
keyFrame5371.FocalPointMode = 'Path'
keyFrame5371.ClosedFocalPath = 0
keyFrame5371.ClosedPositionPath = 0

# ====================================================================
keyFrame5372 = CameraKeyFrame()
keyFrame5372.KeyTime = 0.93
keyFrame5372.KeyValues = [0.0]
keyFrame5372.Position = [55.47553790000305, 11.34, 53.10944831681242]
keyFrame5372.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5372.ViewUp = [0.36780914412017035, -0.866, -0.3385504976849673]
keyFrame5372.ViewAngle = 30.0
keyFrame5372.ParallelScale = 0.97681
keyFrame5372.PositionPathPoints = [55.47553790000305, 11.34, 53.10944831681242]
keyFrame5372.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5372.PositionMode = 'Path'
keyFrame5372.FocalPointMode = 'Path'
keyFrame5372.ClosedFocalPath = 0
keyFrame5372.ClosedPositionPath = 0

# ====================================================================
keyFrame5373 = CameraKeyFrame()
keyFrame5373.KeyTime = 0.9325
keyFrame5373.KeyValues = [0.0]
keyFrame5373.Position = [55.5416957957612, 11.34, 53.048430855168526]
keyFrame5373.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5373.ViewUp = [0.3671313079200199, -0.866, -0.3392854383479597]
keyFrame5373.ViewAngle = 30.0
keyFrame5373.ParallelScale = 0.97681
keyFrame5373.PositionPathPoints = [55.5416957957612, 11.34, 53.048430855168526]
keyFrame5373.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5373.PositionMode = 'Path'
keyFrame5373.FocalPointMode = 'Path'
keyFrame5373.ClosedFocalPath = 0
keyFrame5373.ClosedPositionPath = 0

# ====================================================================
keyFrame5374 = CameraKeyFrame()
keyFrame5374.KeyTime = 0.935
keyFrame5374.KeyValues = [0.0]
keyFrame5374.Position = [55.60773152484062, 11.34, 52.98728120052676]
keyFrame5374.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5374.ViewUp = [0.3664520031933458, -0.866, -0.34001902186807664]
keyFrame5374.ViewAngle = 30.0
keyFrame5374.ParallelScale = 0.97681
keyFrame5374.PositionPathPoints = [55.60773152484062, 11.34, 52.98728120052676]
keyFrame5374.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5374.PositionMode = 'Path'
keyFrame5374.FocalPointMode = 'Path'
keyFrame5374.ClosedFocalPath = 0
keyFrame5374.ClosedPositionPath = 0

# ====================================================================
keyFrame5375 = CameraKeyFrame()
keyFrame5375.KeyTime = 0.9375
keyFrame5375.KeyValues = [0.0]
keyFrame5375.Position = [55.673644823159634, 11.34, 52.925999597566076]
keyFrame5375.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5375.ViewUp = [0.3657712326575604, -0.866, -0.3407512453111552]
keyFrame5375.ViewAngle = 30.0
keyFrame5375.ParallelScale = 0.97681
keyFrame5375.PositionPathPoints = [55.673644823159634, 11.34, 52.925999597566076]
keyFrame5375.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5375.PositionMode = 'Path'
keyFrame5375.FocalPointMode = 'Path'
keyFrame5375.ClosedFocalPath = 0
keyFrame5375.ClosedPositionPath = 0

# ====================================================================
keyFrame5376 = CameraKeyFrame()
keyFrame5376.KeyTime = 0.94
keyFrame5376.KeyValues = [0.0]
keyFrame5376.Position = [55.73943542712915, 11.34, 52.86458629149644]
keyFrame5376.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5376.ViewUp = [0.3650889990359668, -0.866, -0.341482105748496]
keyFrame5376.ViewAngle = 30.0
keyFrame5376.ParallelScale = 0.97681
keyFrame5376.PositionPathPoints = [55.73943542712915, 11.34, 52.86458629149644]
keyFrame5376.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5376.PositionMode = 'Path'
keyFrame5376.FocalPointMode = 'Path'
keyFrame5376.ClosedFocalPath = 0
keyFrame5376.ClosedPositionPath = 0

# ====================================================================
keyFrame5377 = CameraKeyFrame()
keyFrame5377.KeyTime = 0.9425
keyFrame5377.KeyValues = [0.0]
keyFrame5377.Position = [55.805103073653754, 11.34, 52.80304152805786]
keyFrame5377.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5377.ViewUp = [0.36440530505774976, -0.866, -0.3422116002568764]
keyFrame5377.ViewAngle = 30.0
keyFrame5377.ParallelScale = 0.97681
keyFrame5377.PositionPathPoints = [55.805103073653754, 11.34, 52.80304152805786]
keyFrame5377.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5377.PositionMode = 'Path'
keyFrame5377.FocalPointMode = 'Path'
keyFrame5377.ClosedFocalPath = 0
keyFrame5377.ClosedPositionPath = 0

# ====================================================================
keyFrame5378 = CameraKeyFrame()
keyFrame5378.KeyTime = 0.945
keyFrame5378.KeyValues = [0.0]
keyFrame5378.Position = [55.87064750013275, 11.34, 52.74136555351949]
keyFrame5378.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5378.ViewUp = [0.36372015345796577, -0.866, -0.3429397259185629]
keyFrame5378.ViewAngle = 30.0
keyFrame5378.ParallelScale = 0.97681
keyFrame5378.PositionPathPoints = [55.87064750013275, 11.34, 52.74136555351949]
keyFrame5378.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5378.PositionMode = 'Path'
keyFrame5378.FocalPointMode = 'Path'
keyFrame5378.ClosedFocalPath = 0
keyFrame5378.ClosedPositionPath = 0

# ====================================================================
keyFrame5379 = CameraKeyFrame()
keyFrame5379.KeyTime = 0.9475
keyFrame5379.KeyValues = [0.0]
keyFrame5379.Position = [55.93606844446137, 11.34, 52.67955861467862]
keyFrame5379.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5379.ViewUp = [0.36303354697753354, -0.866, -0.3436664798213243]
keyFrame5379.ViewAngle = 30.0
keyFrame5379.ParallelScale = 0.97681
keyFrame5379.PositionPathPoints = [55.93606844446137, 11.34, 52.67955861467862]
keyFrame5379.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5379.PositionMode = 'Path'
keyFrame5379.FocalPointMode = 'Path'
keyFrame5379.ClosedFocalPath = 0
keyFrame5379.ClosedPositionPath = 0

# ====================================================================
keyFrame5380 = CameraKeyFrame()
keyFrame5380.KeyTime = 0.95
keyFrame5380.KeyValues = [0.0]
keyFrame5380.Position = [56.001365645031825, 11.34, 52.61762095885973]
keyFrame5380.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5380.ViewUp = [0.3623454883632247, -0.866, -0.3443918590584445]
keyFrame5380.ViewAngle = 30.0
keyFrame5380.ParallelScale = 0.97681
keyFrame5380.PositionPathPoints = [56.001365645031825, 11.34, 52.61762095885973]
keyFrame5380.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5380.PositionMode = 'Path'
keyFrame5380.FocalPointMode = 'Path'
keyFrame5380.ClosedFocalPath = 0
keyFrame5380.ClosedPositionPath = 0

# ====================================================================
keyFrame5381 = CameraKeyFrame()
keyFrame5381.KeyTime = 0.9525
keyFrame5381.KeyValues = [0.0]
keyFrame5381.Position = [56.066538840433736, 11.34, 52.555552833560824]
keyFrame5381.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5381.ViewUp = [0.361655980367654, -0.866, -0.34511586072873524]
keyFrame5381.ViewAngle = 30.0
keyFrame5381.ParallelScale = 0.97681
keyFrame5381.PositionPathPoints = [56.066538840433736, 11.34, 52.555552833560824]
keyFrame5381.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5381.PositionMode = 'Path'
keyFrame5381.FocalPointMode = 'Path'
keyFrame5381.ClosedFocalPath = 0
keyFrame5381.ClosedPositionPath = 0

# ====================================================================
keyFrame5382 = CameraKeyFrame()
keyFrame5382.KeyTime = 0.955
keyFrame5382.KeyValues = [0.0]
keyFrame5382.Position = [56.131587769417806, 11.34, 52.49335448640849]
keyFrame5382.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5382.ViewUp = [0.3609650257492697, -0.866, -0.34583848193654887]
keyFrame5382.ViewAngle = 30.0
keyFrame5382.ParallelScale = 0.97681
keyFrame5382.PositionPathPoints = [56.131587769417806, 11.34, 52.49335448640849]
keyFrame5382.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5382.PositionMode = 'Path'
keyFrame5382.FocalPointMode = 'Path'
keyFrame5382.ClosedFocalPath = 0
keyFrame5382.ClosedPositionPath = 0

# ====================================================================
keyFrame5383 = CameraKeyFrame()
keyFrame5383.KeyTime = 0.9575
keyFrame5383.KeyValues = [0.0]
keyFrame5383.Position = [56.19651217177719, 11.34, 52.431026166189696]
keyFrame5383.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5383.ViewUp = [0.3602726272723442, -0.866, -0.34655971979179157]
keyFrame5383.ViewAngle = 30.0
keyFrame5383.ParallelScale = 0.97681
keyFrame5383.PositionPathPoints = [56.19651217177719, 11.34, 52.431026166189696]
keyFrame5383.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5383.PositionMode = 'Path'
keyFrame5383.FocalPointMode = 'Path'
keyFrame5383.ClosedFocalPath = 0
keyFrame5383.ClosedPositionPath = 0

# ====================================================================
keyFrame5384 = CameraKeyFrame()
keyFrame5384.KeyTime = 0.96
keyFrame5384.KeyValues = [0.0]
keyFrame5384.Position = [56.26131178781867, 11.34, 52.368568122229085]
keyFrame5384.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5384.ViewUp = [0.3595787877069644, -0.866, -0.3472795714099357]
keyFrame5384.ViewAngle = 30.0
keyFrame5384.ParallelScale = 0.97681
keyFrame5384.PositionPathPoints = [56.26131178781867, 11.34, 52.368568122229085]
keyFrame5384.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5384.PositionMode = 'Path'
keyFrame5384.FocalPointMode = 'Path'
keyFrame5384.ClosedFocalPath = 0
keyFrame5384.ClosedPositionPath = 0

# ====================================================================
keyFrame5385 = CameraKeyFrame()
keyFrame5385.KeyTime = 0.9625
keyFrame5385.KeyValues = [0.0]
keyFrame5385.Position = [56.325986358348004, 11.34, 52.305980604369545]
keyFrame5385.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5385.ViewUp = [0.35888350982902206, -0.866, -0.347998033912033]
keyFrame5385.ViewAngle = 30.0
keyFrame5385.ParallelScale = 0.97681
keyFrame5385.PositionPathPoints = [56.325986358348004, 11.34, 52.305980604369545]
keyFrame5385.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5385.PositionMode = 'Path'
keyFrame5385.FocalPointMode = 'Path'
keyFrame5385.ClosedFocalPath = 0
keyFrame5385.ClosedPositionPath = 0

# ====================================================================
keyFrame5386 = CameraKeyFrame()
keyFrame5386.KeyTime = 0.965
keyFrame5386.KeyValues = [0.0]
keyFrame5386.Position = [56.3905356246709, 11.34, 52.243263862971105]
keyFrame5386.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5386.ViewUp = [0.35818679642020446, -0.866, -0.3487151044247272]
keyFrame5386.ViewAngle = 30.0
keyFrame5386.ParallelScale = 0.97681
keyFrame5386.PositionPathPoints = [56.3905356246709, 11.34, 52.243263862971105]
keyFrame5386.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5386.PositionMode = 'Path'
keyFrame5386.FocalPointMode = 'Path'
keyFrame5386.ClosedFocalPath = 0
keyFrame5386.ClosedPositionPath = 0

# ====================================================================
keyFrame5387 = CameraKeyFrame()
keyFrame5387.KeyTime = 0.9675
keyFrame5387.KeyValues = [0.0]
keyFrame5387.Position = [56.45495932859404, 11.34, 52.18041814890986]
keyFrame5387.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5387.ViewUp = [0.3574886502679845, -0.866, -0.349430780080267]
keyFrame5387.ViewAngle = 30.0
keyFrame5387.ParallelScale = 0.97681
keyFrame5387.PositionPathPoints = [56.45495932859404, 11.34, 52.18041814890986]
keyFrame5387.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5387.PositionMode = 'Path'
keyFrame5387.FocalPointMode = 'Path'
keyFrame5387.ClosedFocalPath = 0
keyFrame5387.ClosedPositionPath = 0

# ====================================================================
keyFrame5388 = CameraKeyFrame()
keyFrame5388.KeyTime = 0.97
keyFrame5388.KeyValues = [0.0]
keyFrame5388.Position = [56.519257212426126, 11.34, 52.1174437135769]
keyFrame5388.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5388.ViewUp = [0.3567890741656115, -0.866, -0.350145058016519]
keyFrame5388.ViewAngle = 30.0
keyFrame5388.ParallelScale = 0.97681
keyFrame5388.PositionPathPoints = [56.519257212426126, 11.34, 52.1174437135769]
keyFrame5388.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5388.PositionMode = 'Path'
keyFrame5388.FocalPointMode = 'Path'
keyFrame5388.ClosedFocalPath = 0
keyFrame5388.ClosedPositionPath = 0

# ====================================================================
keyFrame5389 = CameraKeyFrame()
keyFrame5389.KeyTime = 0.9725
keyFrame5389.KeyValues = [0.0]
keyFrame5389.Position = [56.58342901897879, 11.34, 52.0543408088772]
keyFrame5389.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5389.ViewUp = [0.35608807091210143, -0.866, -0.35085793537698035]
keyFrame5389.ViewAngle = 30.0
keyFrame5389.ParallelScale = 0.97681
keyFrame5389.PositionPathPoints = [56.58342901897879, 11.34, 52.0543408088772]
keyFrame5389.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5389.PositionMode = 'Path'
keyFrame5389.FocalPointMode = 'Path'
keyFrame5389.ClosedFocalPath = 0
keyFrame5389.ClosedPositionPath = 0

# ====================================================================
keyFrame5390 = CameraKeyFrame()
keyFrame5390.KeyTime = 0.975
keyFrame5390.KeyValues = [0.0]
keyFrame5390.Position = [56.64747449156769, 11.34, 51.99110968722859]
keyFrame5390.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5390.ViewUp = [0.3553856433122273, -0.866, -0.35156940931079145]
keyFrame5390.ViewAngle = 30.0
keyFrame5390.ParallelScale = 0.97681
keyFrame5390.PositionPathPoints = [56.64747449156769, 11.34, 51.99110968722859]
keyFrame5390.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5390.PositionMode = 'Path'
keyFrame5390.FocalPointMode = 'Path'
keyFrame5390.ClosedFocalPath = 0
keyFrame5390.ClosedPositionPath = 0

# ====================================================================
keyFrame5391 = CameraKeyFrame()
keyFrame5391.KeyTime = 0.9775
keyFrame5391.KeyValues = [0.0]
keyFrame5391.Position = [56.71139337401348, 11.34, 51.92775060156058]
keyFrame5391.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5391.ViewUp = [0.35468179417650975, -0.866, -0.35227947697274925]
keyFrame5391.ViewAngle = 30.0
keyFrame5391.ParallelScale = 0.97681
keyFrame5391.PositionPathPoints = [56.71139337401348, 11.34, 51.92775060156058]
keyFrame5391.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5391.PositionMode = 'Path'
keyFrame5391.FocalPointMode = 'Path'
keyFrame5391.ClosedFocalPath = 0
keyFrame5391.ClosedPositionPath = 0

# ====================================================================
keyFrame5392 = CameraKeyFrame()
keyFrame5392.KeyTime = 0.98
keyFrame5392.KeyValues = [0.0]
keyFrame5392.Position = [56.775185410642806, 11.34, 51.86426380531336]
keyFrame5392.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5392.ViewUp = [0.3539765263212075, -0.866, -0.3529881355233198]
keyFrame5392.ViewAngle = 30.0
keyFrame5392.ParallelScale = 0.97681
keyFrame5392.PositionPathPoints = [56.775185410642806, 11.34, 51.86426380531336]
keyFrame5392.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5392.PositionMode = 'Path'
keyFrame5392.FocalPointMode = 'Path'
keyFrame5392.ClosedFocalPath = 0
keyFrame5392.ClosedPositionPath = 0

# ====================================================================
keyFrame5393 = CameraKeyFrame()
keyFrame5393.KeyTime = 0.9825
keyFrame5393.KeyValues = [0.0]
keyFrame5393.Position = [56.83885034628928, 11.34, 51.80064955243658]
keyFrame5393.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5393.ViewUp = [0.3532698425661947, -0.866, -0.35369538212684065]
keyFrame5393.ViewAngle = 30.0
keyFrame5393.ParallelScale = 0.97681
keyFrame5393.PositionPathPoints = [56.83885034628928, 11.34, 51.80064955243658]
keyFrame5393.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5393.PositionMode = 'Path'
keyFrame5393.FocalPointMode = 'Path'
keyFrame5393.ClosedFocalPath = 0
keyFrame5393.ClosedPositionPath = 0

# ====================================================================
keyFrame5394 = CameraKeyFrame()
keyFrame5394.KeyTime = 0.985
keyFrame5394.KeyValues = [0.0]
keyFrame5394.Position = [56.90238792629451, 11.34, 51.73690809738838]
keyFrame5394.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5394.ViewUp = [0.35256174573105914, -0.866, -0.3544012139481987]
keyFrame5394.ViewAngle = 30.0
keyFrame5394.ParallelScale = 0.97681
keyFrame5394.PositionPathPoints = [56.90238792629451, 11.34, 51.73690809738838]
keyFrame5394.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5394.PositionMode = 'Path'
keyFrame5394.FocalPointMode = 'Path'
keyFrame5394.ClosedFocalPath = 0
keyFrame5394.ClosedPositionPath = 0

# ====================================================================
keyFrame5395 = CameraKeyFrame()
keyFrame5395.KeyTime = 0.9875
keyFrame5395.KeyValues = [0.0]
keyFrame5395.Position = [56.96579789650906, 11.34, 51.67303969513417]
keyFrame5395.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5395.ViewUp = [0.35185223864744053, -0.866, -0.35510562816342284]
keyFrame5395.ViewAngle = 30.0
keyFrame5395.ParallelScale = 0.97681
keyFrame5395.PositionPathPoints = [56.96579789650906, 11.34, 51.67303969513417]
keyFrame5395.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5395.PositionMode = 'Path'
keyFrame5395.FocalPointMode = 'Path'
keyFrame5395.ClosedFocalPath = 0
keyFrame5395.ClosedPositionPath = 0

# ====================================================================
keyFrame5396 = CameraKeyFrame()
keyFrame5396.KeyTime = 0.99
keyFrame5396.KeyValues = [0.0]
keyFrame5396.Position = [57.02908000329346, 11.34, 51.60904460114558]
keyFrame5396.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5396.ViewUp = [0.3511413241532959, -0.866, -0.35580862195479196]
keyFrame5396.ViewAngle = 30.0
keyFrame5396.ParallelScale = 0.97681
keyFrame5396.PositionPathPoints = [57.02908000329346, 11.34, 51.60904460114558]
keyFrame5396.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5396.PositionMode = 'Path'
keyFrame5396.FocalPointMode = 'Path'
keyFrame5396.ClosedFocalPath = 0
keyFrame5396.ClosedPositionPath = 0

# ====================================================================
keyFrame5397 = CameraKeyFrame()
keyFrame5397.KeyTime = 0.9925
keyFrame5397.KeyValues = [0.0]
keyFrame5397.Position = [57.09223399351916, 11.34, 51.544923071399296]
keyFrame5397.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5397.ViewUp = [0.35042900509222186, -0.866, -0.3565101925102746]
keyFrame5397.ViewAngle = 30.0
keyFrame5397.ParallelScale = 0.97681
keyFrame5397.PositionPathPoints = [57.09223399351916, 11.34, 51.544923071399296]
keyFrame5397.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5397.PositionMode = 'Path'
keyFrame5397.FocalPointMode = 'Path'
keyFrame5397.ClosedFocalPath = 0
keyFrame5397.ClosedPositionPath = 0

# ====================================================================
keyFrame5398 = CameraKeyFrame()
keyFrame5398.KeyTime = 0.995
keyFrame5398.KeyValues = [0.0]
keyFrame5398.Position = [57.15525961456956, 11.34, 51.48067536237599]
keyFrame5398.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5398.ViewUp = [0.3497152843134437, -0.866, -0.35721033702354127]
keyFrame5398.ViewAngle = 30.0
keyFrame5398.ParallelScale = 0.97681
keyFrame5398.PositionPathPoints = [57.15525961456956, 11.34, 51.48067536237599]
keyFrame5398.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5398.PositionMode = 'Path'
keyFrame5398.FocalPointMode = 'Path'
keyFrame5398.ClosedFocalPath = 0
keyFrame5398.ClosedPositionPath = 0

# ====================================================================
keyFrame5399 = CameraKeyFrame()
keyFrame5399.KeyTime = 0.9975
keyFrame5399.KeyValues = [0.0]
keyFrame5399.Position = [57.21815661434094, 11.34, 51.41630173105918]
keyFrame5399.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5399.ViewUp = [0.34900016467180545, -0.866, -0.3579090526939764]
keyFrame5399.ViewAngle = 30.0
keyFrame5399.ParallelScale = 0.97681
keyFrame5399.PositionPathPoints = [57.21815661434094, 11.34, 51.41630173105918]
keyFrame5399.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5399.PositionMode = 'Path'
keyFrame5399.FocalPointMode = 'Path'
keyFrame5399.ClosedFocalPath = 0
keyFrame5399.ClosedPositionPath = 0

# ====================================================================
keyFrame5400 = CameraKeyFrame()
keyFrame5400.KeyTime = 1.0
keyFrame5400.KeyValues = [0.0]
keyFrame5400.Position = [57.28092474124347, 11.34, 51.351802434934044]
keyFrame5400.FocalPoint = [24.9999, 11.34, 20.0]
keyFrame5400.ViewUp = [0.3482836490277591, -0.866, -0.3586063367266904]
keyFrame5400.ViewAngle = 30.0
keyFrame5400.ParallelScale = 0.97681
keyFrame5400.PositionPathPoints = [57.28092474124347, 11.34, 51.351802434934044]
keyFrame5400.FocalPathPoints = [24.9999, 11.34, 20.0]
keyFrame5400.PositionMode = 'Path'
keyFrame5400.FocalPointMode = 'Path'
keyFrame5400.ClosedFocalPath = 0
keyFrame5400.ClosedPositionPath = 0

# initialize the animation track
cameraAnimationCue1.TimeMode = 'Normalized'
cameraAnimationCue1.StartTime = 0.0
cameraAnimationCue1.EndTime = 1.0
cameraAnimationCue1.Enabled = 1
cameraAnimationCue1.Mode = 'Path-based'
cameraAnimationCue1.KeyFrames = [keyFrame5000, keyFrame5001, keyFrame5002, keyFrame5003, keyFrame5004, keyFrame5005, keyFrame5006, keyFrame5007, keyFrame5008, keyFrame5009, keyFrame5010, keyFrame5011, keyFrame5012, keyFrame5013, keyFrame5014, keyFrame5015, keyFrame5016, keyFrame5017, keyFrame5018, keyFrame5019, keyFrame5020, keyFrame5021, keyFrame5022, keyFrame5023, keyFrame5024, keyFrame5025, keyFrame5026, keyFrame5027, keyFrame5028, keyFrame5029, keyFrame5030, keyFrame5031, keyFrame5032, keyFrame5033, keyFrame5034, keyFrame5035, keyFrame5036, keyFrame5037, keyFrame5038, keyFrame5039, keyFrame5040, keyFrame5041, keyFrame5042, keyFrame5043, keyFrame5044, keyFrame5045, keyFrame5046, keyFrame5047, keyFrame5048, keyFrame5049, keyFrame5050, keyFrame5051, keyFrame5052, keyFrame5053, keyFrame5054, keyFrame5055, keyFrame5056, keyFrame5057, keyFrame5058, keyFrame5059, keyFrame5060, keyFrame5061, keyFrame5062, keyFrame5063, keyFrame5064, keyFrame5065, keyFrame5066, keyFrame5067, keyFrame5068, keyFrame5069, keyFrame5070, keyFrame5071, keyFrame5072, keyFrame5073, keyFrame5074, keyFrame5075, keyFrame5076, keyFrame5077, keyFrame5078, keyFrame5079, keyFrame5080, keyFrame5081, keyFrame5082, keyFrame5083, keyFrame5084, keyFrame5085, keyFrame5086, keyFrame5087, keyFrame5088, keyFrame5089, keyFrame5090, keyFrame5091, keyFrame5092, keyFrame5093, keyFrame5094, keyFrame5095, keyFrame5096, keyFrame5097, keyFrame5098, keyFrame5099, keyFrame5100, keyFrame5101, keyFrame5102, keyFrame5103, keyFrame5104, keyFrame5105, keyFrame5106, keyFrame5107, keyFrame5108, keyFrame5109, keyFrame5110, keyFrame5111, keyFrame5112, keyFrame5113, keyFrame5114, keyFrame5115, keyFrame5116, keyFrame5117, keyFrame5118, keyFrame5119, keyFrame5120, keyFrame5121, keyFrame5122, keyFrame5123, keyFrame5124, keyFrame5125, keyFrame5126, keyFrame5127, keyFrame5128, keyFrame5129, keyFrame5130, keyFrame5131, keyFrame5132, keyFrame5133, keyFrame5134, keyFrame5135, keyFrame5136, keyFrame5137, keyFrame5138, keyFrame5139, keyFrame5140, keyFrame5141, keyFrame5142, keyFrame5143, keyFrame5144, keyFrame5145, keyFrame5146, keyFrame5147, keyFrame5148, keyFrame5149, keyFrame5150, keyFrame5151, keyFrame5152, keyFrame5153, keyFrame5154, keyFrame5155, keyFrame5156, keyFrame5157, keyFrame5158, keyFrame5159, keyFrame5160, keyFrame5161, keyFrame5162, keyFrame5163, keyFrame5164, keyFrame5165, keyFrame5166, keyFrame5167, keyFrame5168, keyFrame5169, keyFrame5170, keyFrame5171, keyFrame5172, keyFrame5173, keyFrame5174, keyFrame5175, keyFrame5176, keyFrame5177, keyFrame5178, keyFrame5179, keyFrame5180, keyFrame5181, keyFrame5182, keyFrame5183, keyFrame5184, keyFrame5185, keyFrame5186, keyFrame5187, keyFrame5188, keyFrame5189, keyFrame5190, keyFrame5191, keyFrame5192, keyFrame5193, keyFrame5194, keyFrame5195, keyFrame5196, keyFrame5197, keyFrame5198, keyFrame5199, keyFrame5200, keyFrame5201, keyFrame5202, keyFrame5203, keyFrame5204, keyFrame5205, keyFrame5206, keyFrame5207, keyFrame5208, keyFrame5209, keyFrame5210, keyFrame5211, keyFrame5212, keyFrame5213, keyFrame5214, keyFrame5215, keyFrame5216, keyFrame5217, keyFrame5218, keyFrame5219, keyFrame5220, keyFrame5221, keyFrame5222, keyFrame5223, keyFrame5224, keyFrame5225, keyFrame5226, keyFrame5227, keyFrame5228, keyFrame5229, keyFrame5230, keyFrame5231, keyFrame5232, keyFrame5233, keyFrame5234, keyFrame5235, keyFrame5236, keyFrame5237, keyFrame5238, keyFrame5239, keyFrame5240, keyFrame5241, keyFrame5242, keyFrame5243, keyFrame5244, keyFrame5245, keyFrame5246, keyFrame5247, keyFrame5248, keyFrame5249, keyFrame5250, keyFrame5251, keyFrame5252, keyFrame5253, keyFrame5254, keyFrame5255, keyFrame5256, keyFrame5257, keyFrame5258, keyFrame5259, keyFrame5260, keyFrame5261, keyFrame5262, keyFrame5263, keyFrame5264, keyFrame5265, keyFrame5266, keyFrame5267, keyFrame5268, keyFrame5269, keyFrame5270, keyFrame5271, keyFrame5272, keyFrame5273, keyFrame5274, keyFrame5275, keyFrame5276, keyFrame5277, keyFrame5278, keyFrame5279, keyFrame5280, keyFrame5281, keyFrame5282, keyFrame5283, keyFrame5284, keyFrame5285, keyFrame5286, keyFrame5287, keyFrame5288, keyFrame5289, keyFrame5290, keyFrame5291, keyFrame5292, keyFrame5293, keyFrame5294, keyFrame5295, keyFrame5296, keyFrame5297, keyFrame5298, keyFrame5299, keyFrame5300, keyFrame5301, keyFrame5302, keyFrame5303, keyFrame5304, keyFrame5305, keyFrame5306, keyFrame5307, keyFrame5308, keyFrame5309, keyFrame5310, keyFrame5311, keyFrame5312, keyFrame5313, keyFrame5314, keyFrame5315, keyFrame5316, keyFrame5317, keyFrame5318, keyFrame5319, keyFrame5320, keyFrame5321, keyFrame5322, keyFrame5323, keyFrame5324, keyFrame5325, keyFrame5326, keyFrame5327, keyFrame5328, keyFrame5329, keyFrame5330, keyFrame5331, keyFrame5332, keyFrame5333, keyFrame5334, keyFrame5335, keyFrame5336, keyFrame5337, keyFrame5338, keyFrame5339, keyFrame5340, keyFrame5341, keyFrame5342, keyFrame5343, keyFrame5344, keyFrame5345, keyFrame5346, keyFrame5347, keyFrame5348, keyFrame5349, keyFrame5350, keyFrame5351, keyFrame5352, keyFrame5353, keyFrame5354, keyFrame5355, keyFrame5356, keyFrame5357, keyFrame5358, keyFrame5359, keyFrame5360, keyFrame5361, keyFrame5362, keyFrame5363, keyFrame5364, keyFrame5365, keyFrame5366, keyFrame5367, keyFrame5368, keyFrame5369, keyFrame5370, keyFrame5371, keyFrame5372, keyFrame5373, keyFrame5374, keyFrame5375, keyFrame5376, keyFrame5377, keyFrame5378, keyFrame5379, keyFrame5380, keyFrame5381, keyFrame5382, keyFrame5383, keyFrame5384, keyFrame5385, keyFrame5386, keyFrame5387, keyFrame5388, keyFrame5389, keyFrame5390, keyFrame5391, keyFrame5392, keyFrame5393, keyFrame5394, keyFrame5395, keyFrame5396, keyFrame5397, keyFrame5398, keyFrame5399, keyFrame5400]
cameraAnimationCue1.DataSource = None
