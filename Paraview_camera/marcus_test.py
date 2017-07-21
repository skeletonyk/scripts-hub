
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
keyFrame5000.Position = [20.0, 20.0, 24.5]
keyFrame5000.FocalPoint = [20, 20, 20]
keyFrame5000.ViewUp = [0.4999, -0.866, 0.0]
keyFrame5000.ViewAngle = 30.0
keyFrame5000.ParallelScale = 0.97681
keyFrame5000.PositionPathPoints = [20.0, 20.0, 24.5]
keyFrame5000.FocalPathPoints = [20, 20, 20]
keyFrame5000.PositionMode = 'Path'
keyFrame5000.FocalPointMode = 'Path'
keyFrame5000.ClosedFocalPath = 0
keyFrame5000.ClosedPositionPath = 0

# ====================================================================
keyFrame5001 = CameraKeyFrame()
keyFrame5001.KeyTime = 0.0025
keyFrame5001.KeyValues = [0.0]
keyFrame5001.Position = [20.008999989169727, 20.0, 24.499991000012766]
keyFrame5001.FocalPoint = [20, 20, 20]
keyFrame5001.ViewUp = [0.4998990002014599, -0.866, -0.000999798779647768]
keyFrame5001.ViewAngle = 30.0
keyFrame5001.ParallelScale = 0.97681
keyFrame5001.PositionPathPoints = [20.008999989169727, 20.0, 24.499991000012766]
keyFrame5001.FocalPathPoints = [20, 20, 20]
keyFrame5001.PositionMode = 'Path'
keyFrame5001.FocalPointMode = 'Path'
keyFrame5001.ClosedFocalPath = 0
keyFrame5001.ClosedPositionPath = 0

# ====================================================================
keyFrame5002 = CameraKeyFrame()
keyFrame5002.KeyTime = 0.005
keyFrame5002.KeyValues = [0.0]
keyFrame5002.Position = [20.01799994293269, 20.0, 24.499964000084947]
keyFrame5002.FocalPoint = [20, 20, 20]
keyFrame5002.ViewUp = [0.4998960008095479, -0.866, -0.0019995936359588225]
keyFrame5002.ViewAngle = 30.0
keyFrame5002.ParallelScale = 0.97681
keyFrame5002.PositionPathPoints = [20.01799994293269, 20.0, 24.499964000084947]
keyFrame5002.FocalPathPoints = [20, 20, 20]
keyFrame5002.PositionMode = 'Path'
keyFrame5002.FocalPointMode = 'Path'
keyFrame5002.ClosedFocalPath = 0
keyFrame5002.ClosedPositionPath = 0

# ====================================================================
keyFrame5003 = CameraKeyFrame()
keyFrame5003.KeyTime = 0.0075
keyFrame5003.KeyValues = [0.0]
keyFrame5003.Position = [20.026999826352007, 20.0, 24.49991900031542]
keyFrame5003.FocalPoint = [20, 20, 20]
keyFrame5003.ViewUp = [0.4998910018350169, -0.866, -0.002999380720447823]
keyFrame5003.ViewAngle = 30.0
keyFrame5003.ParallelScale = 0.97681
keyFrame5003.PositionPathPoints = [20.026999826352007, 20.0, 24.49991900031542]
keyFrame5003.FocalPathPoints = [20, 20, 20]
keyFrame5003.PositionMode = 'Path'
keyFrame5003.FocalPointMode = 'Path'
keyFrame5003.ClosedFocalPath = 0
keyFrame5003.ClosedPositionPath = 0

# ====================================================================
keyFrame5004 = CameraKeyFrame()
keyFrame5004.KeyTime = 0.01
keyFrame5004.KeyValues = [0.0]
keyFrame5004.Position = [20.035999600927905, 20.0, 24.49985600089115]
keyFrame5004.FocalPoint = [20, 20, 20]
keyFrame5004.ViewUp = [0.49988400330596444, -0.866, -0.003999155591701697]
keyFrame5004.ViewAngle = 30.0
keyFrame5004.ParallelScale = 0.97681
keyFrame5004.PositionPathPoints = [20.035999600927905, 20.0, 24.49985600089115]
keyFrame5004.FocalPathPoints = [20, 20, 20]
keyFrame5004.PositionMode = 'Path'
keyFrame5004.FocalPointMode = 'Path'
keyFrame5004.ClosedFocalPath = 0
keyFrame5004.ClosedPositionPath = 0

# ====================================================================
keyFrame5005 = CameraKeyFrame()
keyFrame5005.KeyTime = 0.0125
keyFrame5005.KeyValues = [0.0]
keyFrame5005.Position = [20.044999236219123, 20.0, 24.499775002023952]
keyFrame5005.FocalPoint = [20, 20, 20]
keyFrame5005.ViewUp = [0.49987500532502527, -0.866, -0.004998915873783566]
keyFrame5005.ViewAngle = 30.0
keyFrame5005.ParallelScale = 0.97681
keyFrame5005.PositionPathPoints = [20.044999236219123, 20.0, 24.499775002023952]
keyFrame5005.FocalPathPoints = [20, 20, 20]
keyFrame5005.PositionMode = 'Path'
keyFrame5005.FocalPointMode = 'Path'
keyFrame5005.ClosedFocalPath = 0
keyFrame5005.ClosedPositionPath = 0

# ====================================================================
keyFrame5006 = CameraKeyFrame()
keyFrame5006.KeyTime = 0.015
keyFrame5006.KeyValues = [0.0]
keyFrame5006.Position = [20.05399869022508, 20.0, 24.499676004067503]
keyFrame5006.FocalPoint = [20, 20, 20]
keyFrame5006.ViewUp = [0.49986400795839225, -0.866, -0.005998657098363074]
keyFrame5006.ViewAngle = 30.0
keyFrame5006.ParallelScale = 0.97681
keyFrame5006.PositionPathPoints = [20.05399869022508, 20.0, 24.499676004067503]
keyFrame5006.FocalPathPoints = [20, 20, 20]
keyFrame5006.PositionMode = 'Path'
keyFrame5006.FocalPointMode = 'Path'
keyFrame5006.ClosedFocalPath = 0
keyFrame5006.ClosedPositionPath = 0

# ====================================================================
keyFrame5007 = CameraKeyFrame()
keyFrame5007.KeyTime = 0.0175
keyFrame5007.KeyValues = [0.0]
keyFrame5007.Position = [20.06299792823636, 20.0, 24.499559007414064]
keyFrame5007.FocalPoint = [20, 20, 20]
keyFrame5007.ViewUp = [0.4998510112466875, -0.866, -0.006998375054213215]
keyFrame5007.ViewAngle = 30.0
keyFrame5007.ParallelScale = 0.97681
keyFrame5007.PositionPathPoints = [20.06299792823636, 20.0, 24.499559007414064]
keyFrame5007.FocalPathPoints = [20, 20, 20]
keyFrame5007.PositionMode = 'Path'
keyFrame5007.FocalPointMode = 'Path'
keyFrame5007.ClosedFocalPath = 0
keyFrame5007.ClosedPositionPath = 0

# ====================================================================
keyFrame5008 = CameraKeyFrame()
keyFrame5008.KeyTime = 0.02
keyFrame5008.KeyValues = [0.0]
keyFrame5008.Position = [20.071996914255998, 20.0, 24.499424012528785]
keyFrame5008.FocalPoint = [20, 20, 20]
keyFrame5008.ViewUp = [0.49983601523053345, -0.866, -0.007998065530106976]
keyFrame5008.ViewAngle = 30.0
keyFrame5008.ParallelScale = 0.97681
keyFrame5008.PositionPathPoints = [20.071996914255998, 20.0, 24.499424012528785]
keyFrame5008.FocalPathPoints = [20, 20, 20]
keyFrame5008.PositionMode = 'Path'
keyFrame5008.FocalPointMode = 'Path'
keyFrame5008.ClosedFocalPath = 0
keyFrame5008.ClosedPositionPath = 0

# ====================================================================
keyFrame5009 = CameraKeyFrame()
keyFrame5009.KeyTime = 0.0225
keyFrame5009.KeyValues = [0.0]
keyFrame5009.Position = [20.080995612288113, 20.0, 24.499271019951966]
keyFrame5009.FocalPoint = [20, 20, 20]
keyFrame5009.ViewUp = [0.49981901995055217, -0.866, -0.008997724314817353]
keyFrame5009.ViewAngle = 30.0
keyFrame5009.ParallelScale = 0.97681
keyFrame5009.PositionPathPoints = [20.080995612288113, 20.0, 24.499271019951966]
keyFrame5009.FocalPathPoints = [20, 20, 20]
keyFrame5009.PositionMode = 'Path'
keyFrame5009.FocalPointMode = 'Path'
keyFrame5009.ClosedFocalPath = 0
keyFrame5009.ClosedPositionPath = 0

# ====================================================================
keyFrame5010 = CameraKeyFrame()
keyFrame5010.KeyTime = 0.025
keyFrame5010.KeyValues = [0.0]
keyFrame5010.Position = [20.08999398633785, 20.0, 24.499100030295146]
keyFrame5010.FocalPoint = [20, 20, 20]
keyFrame5010.ViewUp = [0.499800025447366, -0.866, -0.00999734719711733]
keyFrame5010.ViewAngle = 30.0
keyFrame5010.ParallelScale = 0.97681
keyFrame5010.PositionPathPoints = [20.08999398633785, 20.0, 24.499100030295146]
keyFrame5010.FocalPathPoints = [20, 20, 20]
keyFrame5010.PositionMode = 'Path'
keyFrame5010.FocalPointMode = 'Path'
keyFrame5010.ClosedFocalPath = 0
keyFrame5010.ClosedPositionPath = 0

# ====================================================================
keyFrame5011 = CameraKeyFrame()
keyFrame5011.KeyTime = 0.0275
keyFrame5011.KeyValues = [0.0]
keyFrame5011.Position = [20.098992000411734, 20.0, 24.498911044240387]
keyFrame5011.FocalPoint = [20, 20, 20]
keyFrame5011.ViewUp = [0.4997790317615972, -0.866, -0.010996929965779903]
keyFrame5011.ViewAngle = 30.0
keyFrame5011.ParallelScale = 0.97681
keyFrame5011.PositionPathPoints = [20.098992000411734, 20.0, 24.498911044240387]
keyFrame5011.FocalPathPoints = [20, 20, 20]
keyFrame5011.PositionMode = 'Path'
keyFrame5011.FocalPointMode = 'Path'
keyFrame5011.ClosedFocalPath = 0
keyFrame5011.ClosedPositionPath = 0

# ====================================================================
keyFrame5012 = CameraKeyFrame()
keyFrame5012.KeyTime = 0.03
keyFrame5012.KeyValues = [0.0]
keyFrame5012.Position = [20.107989618517745, 20.0, 24.498704062548818]
keyFrame5012.FocalPoint = [20, 20, 20]
keyFrame5012.ViewUp = [0.499756038933868, -0.866, -0.01199646840957806]
keyFrame5012.ViewAngle = 30.0
keyFrame5012.ParallelScale = 0.97681
keyFrame5012.PositionPathPoints = [20.107989618517745, 20.0, 24.498704062548818]
keyFrame5012.FocalPathPoints = [20, 20, 20]
keyFrame5012.PositionMode = 'Path'
keyFrame5012.FocalPointMode = 'Path'
keyFrame5012.ClosedFocalPath = 0
keyFrame5012.ClosedPositionPath = 0

# ====================================================================
keyFrame5013 = CameraKeyFrame()
keyFrame5013.KeyTime = 0.0325
keyFrame5013.KeyValues = [0.0]
keyFrame5013.Position = [20.116986804665473, 20.0, 24.498479086050644]
keyFrame5013.FocalPoint = [20, 20, 20]
keyFrame5013.ViewUp = [0.4997310470048006, -0.866, -0.012995958317284796]
keyFrame5013.ViewAngle = 30.0
keyFrame5013.ParallelScale = 0.97681
keyFrame5013.PositionPathPoints = [20.116986804665473, 20.0, 24.498479086050644]
keyFrame5013.FocalPathPoints = [20, 20, 20]
keyFrame5013.PositionMode = 'Path'
keyFrame5013.FocalPointMode = 'Path'
keyFrame5013.ClosedFocalPath = 0
keyFrame5013.ClosedPositionPath = 0

# ====================================================================
keyFrame5014 = CameraKeyFrame()
keyFrame5014.KeyTime = 0.035
keyFrame5014.KeyValues = [0.0]
keyFrame5014.Position = [20.12598352286614, 20.0, 24.49823611564212]
keyFrame5014.FocalPoint = [20, 20, 20]
keyFrame5014.ViewUp = [0.4997040560150173, -0.866, -0.013995395477673096]
keyFrame5014.ViewAngle = 30.0
keyFrame5014.ParallelScale = 0.97681
keyFrame5014.PositionPathPoints = [20.12598352286614, 20.0, 24.49823611564212]
keyFrame5014.FocalPathPoints = [20, 20, 20]
keyFrame5014.PositionMode = 'Path'
keyFrame5014.FocalPointMode = 'Path'
keyFrame5014.ClosedFocalPath = 0
keyFrame5014.ClosedPositionPath = 0

# ====================================================================
keyFrame5015 = CameraKeyFrame()
keyFrame5015.KeyTime = 0.0375
keyFrame5015.KeyValues = [0.0]
keyFrame5015.Position = [20.13497973713288, 20.0, 24.49797515229513]
keyFrame5015.FocalPoint = [20, 20, 20]
keyFrame5015.ViewUp = [0.4996750660051403, -0.866, -0.014994775679515952]
keyFrame5015.ViewAngle = 30.0
keyFrame5015.ParallelScale = 0.97681
keyFrame5015.PositionPathPoints = [20.13497973713288, 20.0, 24.49797515229513]
keyFrame5015.FocalPathPoints = [20, 20, 20]
keyFrame5015.PositionMode = 'Path'
keyFrame5015.FocalPointMode = 'Path'
keyFrame5015.ClosedFocalPath = 0
keyFrame5015.ClosedPositionPath = 0

# ====================================================================
keyFrame5016 = CameraKeyFrame()
keyFrame5016.KeyTime = 0.04
keyFrame5016.KeyValues = [0.0]
keyFrame5016.Position = [20.143975411480824, 20.0, 24.49769619705353]
keyFrame5016.FocalPoint = [20, 20, 20]
keyFrame5016.ViewUp = [0.4996440771893387, -0.866, -0.015994095170387343]
keyFrame5016.ViewAngle = 30.0
keyFrame5016.ParallelScale = 0.97681
keyFrame5016.PositionPathPoints = [20.143975411480824, 20.0, 24.49769619705353]
keyFrame5016.FocalPathPoints = [20, 20, 20]
keyFrame5016.PositionMode = 'Path'
keyFrame5016.FocalPointMode = 'Path'
keyFrame5016.ClosedFocalPath = 0
keyFrame5016.ClosedPositionPath = 0

# ====================================================================
keyFrame5017 = CameraKeyFrame()
keyFrame5017.KeyTime = 0.0425
keyFrame5017.KeyValues = [0.0]
keyFrame5017.Position = [20.15297050992737, 20.0, 24.497399251033137]
keyFrame5017.FocalPoint = [20, 20, 20]
keyFrame5017.ViewUp = [0.4996110899627806, -0.866, -0.016993350676363803]
keyFrame5017.ViewAngle = 30.0
keyFrame5017.ParallelScale = 0.97681
keyFrame5017.PositionPathPoints = [20.15297050992737, 20.0, 24.497399251033137]
keyFrame5017.FocalPathPoints = [20, 20, 20]
keyFrame5017.PositionMode = 'Path'
keyFrame5017.FocalPointMode = 'Path'
keyFrame5017.ClosedFocalPath = 0
keyFrame5017.ClosedPositionPath = 0

# ====================================================================
keyFrame5018 = CameraKeyFrame()
keyFrame5018.KeyTime = 0.045
keyFrame5018.KeyValues = [0.0]
keyFrame5018.Position = [20.16196499649207, 20.0, 24.497084315421738]
keyFrame5018.FocalPoint = [20, 20, 20]
keyFrame5018.ViewUp = [0.4995761044527533, -0.866, -0.017992538215332372]
keyFrame5018.ViewAngle = 30.0
keyFrame5018.ParallelScale = 0.97681
keyFrame5018.PositionPathPoints = [20.16196499649207, 20.0, 24.497084315421738]
keyFrame5018.FocalPathPoints = [20, 20, 20]
keyFrame5018.PositionMode = 'Path'
keyFrame5018.FocalPointMode = 'Path'
keyFrame5018.ClosedFocalPath = 0
keyFrame5018.ClosedPositionPath = 0

# ====================================================================
keyFrame5019 = CameraKeyFrame()
keyFrame5019.KeyTime = 0.0475
keyFrame5019.KeyValues = [0.0]
keyFrame5019.Position = [20.17095883520144, 20.0, 24.496751391478803]
keyFrame5019.FocalPoint = [20, 20, 20]
keyFrame5019.ViewUp = [0.49953912078087065, -0.866, -0.018991653790181105]
keyFrame5019.ViewAngle = 30.0
keyFrame5019.ParallelScale = 0.97681
keyFrame5019.PositionPathPoints = [20.17095883520144, 20.0, 24.496751391478803]
keyFrame5019.FocalPathPoints = [20, 20, 20]
keyFrame5019.PositionMode = 'Path'
keyFrame5019.FocalPointMode = 'Path'
keyFrame5019.ClosedFocalPath = 0
keyFrame5019.ClosedPositionPath = 0

# ====================================================================
keyFrame5020 = CameraKeyFrame()
keyFrame5020.KeyTime = 0.05
keyFrame5020.KeyValues = [0.0]
keyFrame5020.Position = [20.179951990084945, 20.0, 24.496400480535737]
keyFrame5020.FocalPoint = [20, 20, 20]
keyFrame5020.ViewUp = [0.49950013906874635, -0.866, -0.019990693403798054]
keyFrame5020.ViewAngle = 30.0
keyFrame5020.ParallelScale = 0.97681
keyFrame5020.PositionPathPoints = [20.179951990084945, 20.0, 24.496400480535737]
keyFrame5020.FocalPathPoints = [20, 20, 20]
keyFrame5020.PositionMode = 'Path'
keyFrame5020.FocalPointMode = 'Path'
keyFrame5020.ClosedFocalPath = 0
keyFrame5020.ClosedPositionPath = 0

# ====================================================================
keyFrame5021 = CameraKeyFrame()
keyFrame5021.KeyTime = 0.0525
keyFrame5021.KeyValues = [0.0]
keyFrame5021.Position = [20.18894442517056, 20.0, 24.496031583996114]
keyFrame5021.FocalPoint = [20, 20, 20]
keyFrame5021.ViewUp = [0.4994591594379941, -0.866, -0.02098965305907128]
keyFrame5021.ViewAngle = 30.0
keyFrame5021.ParallelScale = 0.97681
keyFrame5021.PositionPathPoints = [20.18894442517056, 20.0, 24.496031583996114]
keyFrame5021.FocalPathPoints = [20, 20, 20]
keyFrame5021.PositionMode = 'Path'
keyFrame5021.FocalPointMode = 'Path'
keyFrame5021.ClosedFocalPath = 0
keyFrame5021.ClosedPositionPath = 0

# ====================================================================
keyFrame5022 = CameraKeyFrame()
keyFrame5022.KeyTime = 0.055
keyFrame5022.KeyValues = [0.0]
keyFrame5022.Position = [20.197936104488836, 20.0, 24.495644703335472]
keyFrame5022.FocalPoint = [20, 20, 20]
keyFrame5022.ViewUp = [0.49941618201022775, -0.866, -0.021988528758888827]
keyFrame5022.ViewAngle = 30.0
keyFrame5022.ParallelScale = 0.97681
keyFrame5022.PositionPathPoints = [20.197936104488836, 20.0, 24.495644703335472]
keyFrame5022.FocalPathPoints = [20, 20, 20]
keyFrame5022.PositionMode = 'Path'
keyFrame5022.FocalPointMode = 'Path'
keyFrame5022.ClosedFocalPath = 0
keyFrame5022.ClosedPositionPath = 0

# ====================================================================
keyFrame5023 = CameraKeyFrame()
keyFrame5023.KeyTime = 0.0575
keyFrame5023.KeyValues = [0.0]
keyFrame5023.Position = [20.206926992073043, 20.0, 24.49523984010128]
keyFrame5023.FocalPoint = [20, 20, 20]
keyFrame5023.ViewUp = [0.49937120690706094, -0.866, -0.022987316506138757]
keyFrame5023.ViewAngle = 30.0
keyFrame5023.ParallelScale = 0.97681
keyFrame5023.PositionPathPoints = [20.206926992073043, 20.0, 24.49523984010128]
keyFrame5023.FocalPathPoints = [20, 20, 20]
keyFrame5023.PositionMode = 'Path'
keyFrame5023.FocalPointMode = 'Path'
keyFrame5023.ClosedFocalPath = 0
keyFrame5023.ClosedPositionPath = 0

# ====================================================================
keyFrame5024 = CameraKeyFrame()
keyFrame5024.KeyTime = 0.06
keyFrame5024.KeyValues = [0.0]
keyFrame5024.Position = [20.215917051959345, 20.0, 24.494816995912966]
keyFrame5024.FocalPoint = [20, 20, 20]
keyFrame5024.ViewUp = [0.4993242342501075, -0.866, -0.02398601230370912]
keyFrame5024.ViewAngle = 30.0
keyFrame5024.ParallelScale = 0.97681
keyFrame5024.PositionPathPoints = [20.215917051959345, 20.0, 24.494816995912966]
keyFrame5024.FocalPathPoints = [20, 20, 20]
keyFrame5024.PositionMode = 'Path'
keyFrame5024.FocalPointMode = 'Path'
keyFrame5024.ClosedFocalPath = 0
keyFrame5024.ClosedPositionPath = 0

# ====================================================================
keyFrame5025 = CameraKeyFrame()
keyFrame5025.KeyTime = 0.0625
keyFrame5025.KeyValues = [0.0]
keyFrame5025.Position = [20.22490624818691, 20.0, 24.494376172461894]
keyFrame5025.FocalPoint = [20, 20, 20]
keyFrame5025.ViewUp = [0.4992752641609812, -0.866, -0.024984612154487974]
keyFrame5025.ViewAngle = 30.0
keyFrame5025.ParallelScale = 0.97681
keyFrame5025.PositionPathPoints = [20.22490624818691, 20.0, 24.494376172461894]
keyFrame5025.FocalPathPoints = [20, 20, 20]
keyFrame5025.PositionMode = 'Path'
keyFrame5025.FocalPointMode = 'Path'
keyFrame5025.ClosedFocalPath = 0
keyFrame5025.ClosedPositionPath = 0

# ====================================================================
keyFrame5026 = CameraKeyFrame()
keyFrame5026.KeyTime = 0.065
keyFrame5026.KeyValues = [0.0]
keyFrame5026.Position = [20.23389454479811, 20.0, 24.49391737151135]
keyFrame5026.FocalPoint = [20, 20, 20]
keyFrame5026.ViewUp = [0.4992242967612957, -0.866, -0.025983112061363372]
keyFrame5026.ViewAngle = 30.0
keyFrame5026.ParallelScale = 0.97681
keyFrame5026.PositionPathPoints = [20.23389454479811, 20.0, 24.49391737151135]
keyFrame5026.FocalPathPoints = [20, 20, 20]
keyFrame5026.PositionMode = 'Path'
keyFrame5026.FocalPointMode = 'Path'
keyFrame5026.ClosedFocalPath = 0
keyFrame5026.ClosedPositionPath = 0

# ====================================================================
keyFrame5027 = CameraKeyFrame()
keyFrame5027.KeyTime = 0.0675
keyFrame5027.KeyValues = [0.0]
keyFrame5027.Position = [20.242881905838612, 20.0, 24.493440594896573]
keyFrame5027.FocalPoint = [20, 20, 20]
keyFrame5027.ViewUp = [0.49917133220525184, -0.866, -0.026981508028545566]
keyFrame5027.ViewAngle = 30.0
keyFrame5027.ParallelScale = 0.97681
keyFrame5027.PositionPathPoints = [20.242881905838612, 20.0, 24.493440594896573]
keyFrame5027.FocalPathPoints = [20, 20, 20]
keyFrame5027.PositionMode = 'Path'
keyFrame5027.FocalPointMode = 'Path'
keyFrame5027.ClosedFocalPath = 0
keyFrame5027.ClosedPositionPath = 0

# ====================================================================
keyFrame5028 = CameraKeyFrame()
keyFrame5028.KeyTime = 0.07
keyFrame5028.KeyValues = [0.0]
keyFrame5028.Position = [20.25186829535758, 20.0, 24.4929458445247]
keyFrame5028.FocalPoint = [20, 20, 20]
keyFrame5028.ViewUp = [0.49911637103199524, -0.866, -0.027979796075863938]
keyFrame5028.ViewAngle = 30.0
keyFrame5028.ParallelScale = 0.97681
keyFrame5028.PositionPathPoints = [20.25186829535758, 20.0, 24.4929458445247]
keyFrame5028.FocalPathPoints = [20, 20, 20]
keyFrame5028.PositionMode = 'Path'
keyFrame5028.FocalPointMode = 'Path'
keyFrame5028.ClosedFocalPath = 0
keyFrame5028.ClosedPositionPath = 0

# ====================================================================
keyFrame5029 = CameraKeyFrame()
keyFrame5029.KeyTime = 0.0725
keyFrame5029.KeyValues = [0.0]
keyFrame5029.Position = [20.260853677407795, 20.0, 24.492433122374816]
keyFrame5029.FocalPoint = [20, 20, 20]
keyFrame5029.ViewUp = [0.49905941356183214, -0.866, -0.02897797221426844]
keyFrame5029.ViewAngle = 30.0
keyFrame5029.ParallelScale = 0.97681
keyFrame5029.PositionPathPoints = [20.260853677407795, 20.0, 24.492433122374816]
keyFrame5029.FocalPathPoints = [20, 20, 20]
keyFrame5029.PositionMode = 'Path'
keyFrame5029.FocalPointMode = 'Path'
keyFrame5029.ClosedFocalPath = 0
keyFrame5029.ClosedPositionPath = 0

# ====================================================================
keyFrame5030 = CameraKeyFrame()
keyFrame5030.KeyTime = 0.075
keyFrame5030.KeyValues = [0.0]
keyFrame5030.Position = [20.269838016045814, 20.0, 24.49190243049791]
keyFrame5030.FocalPoint = [20, 20, 20]
keyFrame5030.ViewUp = [0.49900046000781084, -0.866, -0.02997603245035708]
keyFrame5030.ViewAngle = 30.0
keyFrame5030.ParallelScale = 0.97681
keyFrame5030.PositionPathPoints = [20.269838016045814, 20.0, 24.49190243049791]
keyFrame5030.FocalPathPoints = [20, 20, 20]
keyFrame5030.PositionMode = 'Path'
keyFrame5030.FocalPointMode = 'Path'
keyFrame5030.ClosedFocalPath = 0
keyFrame5030.ClosedPositionPath = 0

# ====================================================================
keyFrame5031 = CameraKeyFrame()
keyFrame5031.KeyTime = 0.0775
keyFrame5031.KeyValues = [0.0]
keyFrame5031.Position = [20.278821275332106, 20.0, 24.491353771016882]
keyFrame5031.FocalPoint = [20, 20, 20]
keyFrame5031.ViewUp = [0.4989395105829797, -0.866, -0.03097397279072786]
keyFrame5031.ViewAngle = 30.0
keyFrame5031.ParallelScale = 0.97681
keyFrame5031.PositionPathPoints = [20.278821275332106, 20.0, 24.491353771016882]
keyFrame5031.FocalPathPoints = [20, 20, 20]
keyFrame5031.PositionMode = 'Path'
keyFrame5031.FocalPointMode = 'Path'
keyFrame5031.ClosedFocalPath = 0
keyFrame5031.ClosedPositionPath = 0

# ====================================================================
keyFrame5032 = CameraKeyFrame()
keyFrame5032.KeyTime = 0.08
keyFrame5032.KeyValues = [0.0]
keyFrame5032.Position = [20.28780341933123, 20.0, 24.490787146126547]
keyFrame5032.FocalPoint = [20, 20, 20]
keyFrame5032.ViewUp = [0.49887656550038706, -0.866, -0.03197178924197877]
keyFrame5032.ViewAngle = 30.0
keyFrame5032.ParallelScale = 0.97681
keyFrame5032.PositionPathPoints = [20.28780341933123, 20.0, 24.490787146126547]
keyFrame5032.FocalPathPoints = [20, 20, 20]
keyFrame5032.PositionMode = 'Path'
keyFrame5032.FocalPointMode = 'Path'
keyFrame5032.ClosedFocalPath = 0
keyFrame5032.ClosedPositionPath = 0

# ====================================================================
keyFrame5033 = CameraKeyFrame()
keyFrame5033.KeyTime = 0.0825
keyFrame5033.KeyValues = [0.0]
keyFrame5033.Position = [20.29678441211195, 20.0, 24.490202558093625]
keyFrame5033.FocalPoint = [20, 20, 20]
keyFrame5033.ViewUp = [0.49881162497308124, -0.866, -0.03296947781070782]
keyFrame5033.ViewAngle = 30.0
keyFrame5033.ParallelScale = 0.97681
keyFrame5033.PositionPathPoints = [20.29678441211195, 20.0, 24.490202558093625]
keyFrame5033.FocalPathPoints = [20, 20, 20]
keyFrame5033.PositionMode = 'Path'
keyFrame5033.FocalPointMode = 'Path'
keyFrame5033.ClosedFocalPath = 0
keyFrame5033.ClosedPositionPath = 0

# ====================================================================
keyFrame5034 = CameraKeyFrame()
keyFrame5034.KeyTime = 0.085
keyFrame5034.KeyValues = [0.0]
keyFrame5034.Position = [20.305764217747413, 20.0, 24.489600009256737]
keyFrame5034.FocalPoint = [20, 20, 20]
keyFrame5034.ViewUp = [0.4987446892141106, -0.866, -0.033967034503513]
keyFrame5034.ViewAngle = 30.0
keyFrame5034.ParallelScale = 0.97681
keyFrame5034.PositionPathPoints = [20.305764217747413, 20.0, 24.489600009256737]
keyFrame5034.FocalPathPoints = [20, 20, 20]
keyFrame5034.PositionMode = 'Path'
keyFrame5034.FocalPointMode = 'Path'
keyFrame5034.ClosedFocalPath = 0
keyFrame5034.ClosedPositionPath = 0

# ====================================================================
keyFrame5035 = CameraKeyFrame()
keyFrame5035.KeyTime = 0.0875
keyFrame5035.KeyValues = [0.0]
keyFrame5035.Position = [20.314742800315276, 20.0, 24.488979502026393]
keyFrame5035.FocalPoint = [20, 20, 20]
keyFrame5035.ViewUp = [0.49867575843652345, -0.866, -0.03496445532699232]
keyFrame5035.ViewAngle = 30.0
keyFrame5035.ParallelScale = 0.97681
keyFrame5035.PositionPathPoints = [20.314742800315276, 20.0, 24.488979502026393]
keyFrame5035.FocalPathPoints = [20, 20, 20]
keyFrame5035.PositionMode = 'Path'
keyFrame5035.FocalPointMode = 'Path'
keyFrame5035.ClosedFocalPath = 0
keyFrame5035.ClosedPositionPath = 0

# ====================================================================
keyFrame5036 = CameraKeyFrame()
keyFrame5036.KeyTime = 0.09
keyFrame5036.KeyValues = [0.0]
keyFrame5036.Position = [20.32372012389787, 20.0, 24.488341038885004]
keyFrame5036.FocalPoint = [20, 20, 20]
keyFrame5036.ViewUp = [0.49860483285336815, -0.866, -0.035961736287743774]
keyFrame5036.ViewAngle = 30.0
keyFrame5036.ParallelScale = 0.97681
keyFrame5036.PositionPathPoints = [20.32372012389787, 20.0, 24.488341038885004]
keyFrame5036.FocalPathPoints = [20, 20, 20]
keyFrame5036.PositionMode = 'Path'
keyFrame5036.FocalPointMode = 'Path'
keyFrame5036.ClosedFocalPath = 0
keyFrame5036.ClosedPositionPath = 0

# ====================================================================
keyFrame5037 = CameraKeyFrame()
keyFrame5037.KeyTime = 0.0925
keyFrame5037.KeyValues = [0.0]
keyFrame5037.Position = [20.33269615258235, 20.0, 24.487684622386862]
keyFrame5037.FocalPoint = [20, 20, 20]
keyFrame5037.ViewUp = [0.4985319126776931, -0.866, -0.03695887339236536]
keyFrame5037.ViewAngle = 30.0
keyFrame5037.ParallelScale = 0.97681
keyFrame5037.PositionPathPoints = [20.33269615258235, 20.0, 24.487684622386862]
keyFrame5037.FocalPathPoints = [20, 20, 20]
keyFrame5037.PositionMode = 'Path'
keyFrame5037.FocalPointMode = 'Path'
keyFrame5037.ClosedFocalPath = 0
keyFrame5037.ClosedPositionPath = 0

# ====================================================================
keyFrame5038 = CameraKeyFrame()
keyFrame5038.KeyTime = 0.095
keyFrame5038.KeyValues = [0.0]
keyFrame5038.Position = [20.341670850460968, 20.0, 24.48701025515812]
keyFrame5038.FocalPoint = [20, 20, 20]
keyFrame5038.ViewUp = [0.4984569981225465, -0.866, -0.03795586264745508]
keyFrame5038.ViewAngle = 30.0
keyFrame5038.ParallelScale = 0.97681
keyFrame5038.PositionPathPoints = [20.341670850460968, 20.0, 24.48701025515812]
keyFrame5038.FocalPathPoints = [20, 20, 20]
keyFrame5038.PositionMode = 'Path'
keyFrame5038.FocalPointMode = 'Path'
keyFrame5038.ClosedFocalPath = 0
keyFrame5038.ClosedPositionPath = 0

# ====================================================================
keyFrame5039 = CameraKeyFrame()
keyFrame5039.KeyTime = 0.0975
keyFrame5039.KeyValues = [0.0]
keyFrame5039.Position = [20.35064418164341, 20.0, 24.486317939894164]
keyFrame5039.FocalPoint = [20, 20, 20]
keyFrame5039.ViewUp = [0.49838009386564974, -0.866, -0.03895270035303934]
keyFrame5039.ViewAngle = 30.0
keyFrame5039.ParallelScale = 0.97681
keyFrame5039.PositionPathPoints = [20.35064418164341, 20.0, 24.486317939894164]
keyFrame5039.FocalPathPoints = [20, 20, 20]
keyFrame5039.PositionMode = 'Path'
keyFrame5039.FocalPointMode = 'Path'
keyFrame5039.ClosedFocalPath = 0
keyFrame5039.ClosedPositionPath = 0

# ====================================================================
keyFrame5040 = CameraKeyFrame()
keyFrame5040.KeyTime = 0.1
keyFrame5040.KeyValues = [0.0]
keyFrame5040.Position = [20.35961611024303, 20.0, 24.48560767936261]
keyFrame5040.FocalPoint = [20, 20, 20]
keyFrame5040.ViewUp = [0.498301190602249, -0.866, -0.039949381890184654]
keyFrame5040.ViewAngle = 30.0
keyFrame5040.ParallelScale = 0.97681
keyFrame5040.PositionPathPoints = [20.35961611024303, 20.0, 24.48560767936261]
keyFrame5040.FocalPathPoints = [20, 20, 20]
keyFrame5040.PositionMode = 'Path'
keyFrame5040.FocalPointMode = 'Path'
keyFrame5040.ClosedFocalPath = 0
keyFrame5040.ClosedPositionPath = 0

# ====================================================================
keyFrame5041 = CameraKeyFrame()
keyFrame5041.KeyTime = 0.1025
keyFrame5041.KeyValues = [0.0]
keyFrame5041.Position = [20.368586600371778, 20.0, 24.484879476404394]
keyFrame5041.FocalPoint = [20, 20, 20]
keyFrame5041.ViewUp = [0.49822029466745454, -0.866, -0.040945903667844785]
keyFrame5041.ViewAngle = 30.0
keyFrame5041.ParallelScale = 0.97681
keyFrame5041.PositionPathPoints = [20.368586600371778, 20.0, 24.484879476404394]
keyFrame5041.FocalPathPoints = [20, 20, 20]
keyFrame5041.PositionMode = 'Path'
keyFrame5041.FocalPointMode = 'Path'
keyFrame5041.ClosedFocalPath = 0
keyFrame5041.ClosedPositionPath = 0

# ====================================================================
keyFrame5042 = CameraKeyFrame()
keyFrame5042.KeyTime = 0.105
keyFrame5042.KeyValues = [0.0]
keyFrame5042.Position = [20.377555616147482, 20.0, 24.484133333932252]
keyFrame5042.FocalPoint = [20, 20, 20]
keyFrame5042.ViewUp = [0.4981374062931046, -0.866, -0.04194226169385264]
keyFrame5042.ViewAngle = 30.0
keyFrame5042.ParallelScale = 0.97681
keyFrame5042.PositionPathPoints = [20.377555616147482, 20.0, 24.484133333932252]
keyFrame5042.FocalPathPoints = [20, 20, 20]
keyFrame5042.PositionMode = 'Path'
keyFrame5042.FocalPointMode = 'Path'
keyFrame5042.ClosedFocalPath = 0
keyFrame5042.ClosedPositionPath = 0

# ====================================================================
keyFrame5043 = CameraKeyFrame()
keyFrame5043.KeyTime = 0.1075
keyFrame5043.KeyValues = [0.0]
keyFrame5043.Position = [20.386523121694015, 20.0, 24.483369254930725]
keyFrame5043.FocalPoint = [20, 20, 20]
keyFrame5043.ViewUp = [0.498052525719019, -0.866, -0.0429384519765657]
keyFrame5043.ViewAngle = 30.0
keyFrame5043.ParallelScale = 0.97681
keyFrame5043.PositionPathPoints = [20.386523121694015, 20.0, 24.483369254930725]
keyFrame5043.FocalPathPoints = [20, 20, 20]
keyFrame5043.PositionMode = 'Path'
keyFrame5043.FocalPointMode = 'Path'
keyFrame5043.ClosedFocalPath = 0
keyFrame5043.ClosedPositionPath = 0

# ====================================================================
keyFrame5044 = CameraKeyFrame()
keyFrame5044.KeyTime = 0.11
keyFrame5044.KeyValues = [0.0]
keyFrame5044.Position = [20.39548908114144, 20.0, 24.482587242456123]
keyFrame5044.FocalPoint = [20, 20, 20]
keyFrame5044.ViewUp = [0.497965653192999, -0.866, -0.043934470524866]
keyFrame5044.ViewAngle = 30.0
keyFrame5044.ParallelScale = 0.97681
keyFrame5044.PositionPathPoints = [20.39548908114144, 20.0, 24.482587242456123]
keyFrame5044.FocalPathPoints = [20, 20, 20]
keyFrame5044.PositionMode = 'Path'
keyFrame5044.FocalPointMode = 'Path'
keyFrame5044.ClosedFocalPath = 0
keyFrame5044.ClosedPositionPath = 0

# ====================================================================
keyFrame5045 = CameraKeyFrame()
keyFrame5045.KeyTime = 0.1125
keyFrame5045.KeyValues = [0.0]
keyFrame5045.Position = [20.40445345862618, 20.0, 24.48178729963655]
keyFrame5045.FocalPoint = [20, 20, 20]
keyFrame5045.ViewUp = [0.49787678897082754, -0.866, -0.044930313348160174]
keyFrame5045.ViewAngle = 30.0
keyFrame5045.ParallelScale = 0.97681
keyFrame5045.PositionPathPoints = [20.40445345862618, 20.0, 24.48178729963655]
keyFrame5045.FocalPathPoints = [20, 20, 20]
keyFrame5045.PositionMode = 'Path'
keyFrame5045.FocalPointMode = 'Path'
keyFrame5045.ClosedFocalPath = 0
keyFrame5045.ClosedPositionPath = 0

# ====================================================================
keyFrame5046 = CameraKeyFrame()
keyFrame5046.KeyTime = 0.115
keyFrame5046.KeyValues = [0.0]
keyFrame5046.Position = [20.413416218291168, 20.0, 24.48096942967188]
keyFrame5046.FocalPoint = [20, 20, 20]
keyFrame5046.ViewUp = [0.49778593331626897, -0.866, -0.04592597645637938]
keyFrame5046.ViewAngle = 30.0
keyFrame5046.ParallelScale = 0.97681
keyFrame5046.PositionPathPoints = [20.413416218291168, 20.0, 24.48096942967188]
keyFrame5046.FocalPathPoints = [20, 20, 20]
keyFrame5046.PositionMode = 'Path'
keyFrame5046.FocalPointMode = 'Path'
keyFrame5046.ClosedFocalPath = 0
keyFrame5046.ClosedPositionPath = 0

# ====================================================================
keyFrame5047 = CameraKeyFrame()
keyFrame5047.KeyTime = 0.1175
keyFrame5047.KeyValues = [0.0]
keyFrame5047.Position = [20.42237732428601, 20.0, 24.480133635833756]
keyFrame5047.FocalPoint = [20, 20, 20]
keyFrame5047.ViewUp = [0.4976930865010693, -0.866, -0.04692145585997936]
keyFrame5047.ViewAngle = 30.0
keyFrame5047.ParallelScale = 0.97681
keyFrame5047.PositionPathPoints = [20.42237732428601, 20.0, 24.480133635833756]
keyFrame5047.FocalPathPoints = [20, 20, 20]
keyFrame5047.PositionMode = 'Path'
keyFrame5047.FocalPointMode = 'Path'
keyFrame5047.ClosedFocalPath = 0
keyFrame5047.ClosedPositionPath = 0

# ====================================================================
keyFrame5048 = CameraKeyFrame()
keyFrame5048.KeyTime = 0.12
keyFrame5048.KeyValues = [0.0]
keyFrame5048.Position = [20.431336740767154, 20.0, 24.479279921465576]
keyFrame5048.FocalPoint = [20, 20, 20]
keyFrame5048.ViewUp = [0.49759824880495596, -0.866, -0.04791674756994042]
keyFrame5048.ViewAngle = 30.0
keyFrame5048.ParallelScale = 0.97681
keyFrame5048.PositionPathPoints = [20.431336740767154, 20.0, 24.479279921465576]
keyFrame5048.FocalPathPoints = [20, 20, 20]
keyFrame5048.PositionMode = 'Path'
keyFrame5048.FocalPointMode = 'Path'
keyFrame5048.ClosedFocalPath = 0
keyFrame5048.ClosedPositionPath = 0

# ====================================================================
keyFrame5049 = CameraKeyFrame()
keyFrame5049.KeyTime = 0.1225
keyFrame5049.KeyValues = [0.0]
keyFrame5049.Position = [20.440294431898028, 20.0, 24.4784082899825]
keyFrame5049.FocalPoint = [20, 20, 20]
keyFrame5049.ViewUp = [0.49750142051563806, -0.866, -0.04891184759776743]
keyFrame5049.ViewAngle = 30.0
keyFrame5049.ParallelScale = 0.97681
keyFrame5049.PositionPathPoints = [20.440294431898028, 20.0, 24.4784082899825]
keyFrame5049.FocalPathPoints = [20, 20, 20]
keyFrame5049.PositionMode = 'Path'
keyFrame5049.FocalPointMode = 'Path'
keyFrame5049.ClosedFocalPath = 0
keyFrame5049.ClosedPositionPath = 0

# ====================================================================
keyFrame5050 = CameraKeyFrame()
keyFrame5050.KeyTime = 0.125
keyFrame5050.KeyValues = [0.0]
keyFrame5050.Position = [20.44925036184922, 20.0, 24.47751874487144]
keyFrame5050.FocalPoint = [20, 20, 20]
keyFrame5050.ViewUp = [0.4974026019593449, -0.866, -0.04990675195874769]
keyFrame5050.ViewAngle = 30.0
keyFrame5050.ParallelScale = 0.97681
keyFrame5050.PositionPathPoints = [20.44925036184922, 20.0, 24.47751874487144]
keyFrame5050.FocalPathPoints = [20, 20, 20]
keyFrame5050.PositionMode = 'Path'
keyFrame5050.FocalPointMode = 'Path'
keyFrame5050.ClosedFocalPath = 0
keyFrame5050.ClosedPositionPath = 0

# ====================================================================
keyFrame5051 = CameraKeyFrame()
keyFrame5051.KeyTime = 0.1275
keyFrame5051.KeyValues = [0.0]
keyFrame5051.Position = [20.458204494798622, 20.0, 24.476611289691036]
keyFrame5051.FocalPoint = [20, 20, 20]
keyFrame5051.ViewUp = [0.49730179380370815, -0.866, -0.050901456704262646]
keyFrame5051.ViewAngle = 30.0
keyFrame5051.ParallelScale = 0.97681
keyFrame5051.PositionPathPoints = [20.458204494798622, 20.0, 24.476611289691036]
keyFrame5051.FocalPathPoints = [20, 20, 20]
keyFrame5051.PositionMode = 'Path'
keyFrame5051.FocalPointMode = 'Path'
keyFrame5051.ClosedFocalPath = 0
keyFrame5051.ClosedPositionPath = 0

# ====================================================================
keyFrame5052 = CameraKeyFrame()
keyFrame5052.KeyTime = 0.13
keyFrame5052.KeyValues = [0.0]
keyFrame5052.Position = [20.467156794931597, 20.0, 24.47568592807168]
keyFrame5052.FocalPoint = [20, 20, 20]
keyFrame5052.ViewUp = [0.4971989965163678, -0.866, -0.05189595786403153]
keyFrame5052.ViewAngle = 30.0
keyFrame5052.ParallelScale = 0.97681
keyFrame5052.PositionPathPoints = [20.467156794931597, 20.0, 24.47568592807168]
keyFrame5052.FocalPathPoints = [20, 20, 20]
keyFrame5052.PositionMode = 'Path'
keyFrame5052.FocalPointMode = 'Path'
keyFrame5052.ClosedFocalPath = 0
keyFrame5052.ClosedPositionPath = 0

# ====================================================================
keyFrame5053 = CameraKeyFrame()
keyFrame5053.KeyTime = 0.1325
keyFrame5053.KeyValues = [0.0]
keyFrame5053.Position = [20.47610722644114, 20.0, 24.474742663715485]
keyFrame5053.FocalPoint = [20, 20, 20]
keyFrame5053.ViewUp = [0.49709421048299324, -0.866, -0.05289025145870205]
keyFrame5053.ViewAngle = 30.0
keyFrame5053.ParallelScale = 0.97681
keyFrame5053.PositionPathPoints = [20.47610722644114, 20.0, 24.474742663715485]
keyFrame5053.FocalPathPoints = [20, 20, 20]
keyFrame5053.PositionMode = 'Path'
keyFrame5053.FocalPointMode = 'Path'
keyFrame5053.ClosedFocalPath = 0
keyFrame5053.ClosedPositionPath = 0

# ====================================================================
keyFrame5054 = CameraKeyFrame()
keyFrame5054.KeyTime = 0.135
keyFrame5054.KeyValues = [0.0]
keyFrame5054.Position = [20.485055753528034, 20.0, 24.473781500396292]
keyFrame5054.FocalPoint = [20, 20, 20]
keyFrame5054.ViewUp = [0.49698743609990953, -0.866, -0.05388433350973172]
keyFrame5054.ViewAngle = 30.0
keyFrame5054.ParallelScale = 0.97681
keyFrame5054.PositionPathPoints = [20.485055753528034, 20.0, 24.473781500396292]
keyFrame5054.FocalPathPoints = [20, 20, 20]
keyFrame5054.PositionMode = 'Path'
keyFrame5054.FocalPointMode = 'Path'
keyFrame5054.ClosedFocalPath = 0
keyFrame5054.ClosedPositionPath = 0

# ====================================================================
keyFrame5055 = CameraKeyFrame()
keyFrame5055.KeyTime = 0.1375
keyFrame5055.KeyValues = [0.0]
keyFrame5055.Position = [20.494002340400996, 20.0, 24.47280244195965]
keyFrame5055.FocalPoint = [20, 20, 20]
keyFrame5055.ViewUp = [0.49687867377409745, -0.866, -0.054878200039387925]
keyFrame5055.ViewAngle = 30.0
keyFrame5055.ParallelScale = 0.97681
keyFrame5055.PositionPathPoints = [20.494002340400996, 20.0, 24.47280244195965]
keyFrame5055.FocalPathPoints = [20, 20, 20]
keyFrame5055.PositionMode = 'Path'
keyFrame5055.FocalPointMode = 'Path'
keyFrame5055.ClosedFocalPath = 0
keyFrame5055.ClosedPositionPath = 0

# ====================================================================
keyFrame5056 = CameraKeyFrame()
keyFrame5056.KeyTime = 0.14
keyFrame5056.KeyValues = [0.0]
keyFrame5056.Position = [20.50294695127687, 20.0, 24.47180549232283]
keyFrame5056.FocalPoint = [20, 20, 20]
keyFrame5056.ViewUp = [0.4967679239231932, -0.866, -0.05587184707074788]
keyFrame5056.ViewAngle = 30.0
keyFrame5056.ParallelScale = 0.97681
keyFrame5056.PositionPathPoints = [20.50294695127687, 20.0, 24.47180549232283]
keyFrame5056.FocalPathPoints = [20, 20, 20]
keyFrame5056.PositionMode = 'Path'
keyFrame5056.FocalPointMode = 'Path'
keyFrame5056.ClosedFocalPath = 0
keyFrame5056.ClosedPositionPath = 0

# ====================================================================
keyFrame5057 = CameraKeyFrame()
keyFrame5057.KeyTime = 0.1425
keyFrame5057.KeyValues = [0.0]
keyFrame5057.Position = [20.511889550380744, 20.0, 24.4707906554748]
keyFrame5057.FocalPoint = [20, 20, 20]
keyFrame5057.ViewUp = [0.4966551869754888, -0.866, -0.05686527062769863]
keyFrame5057.ViewAngle = 30.0
keyFrame5057.ParallelScale = 0.97681
keyFrame5057.PositionPathPoints = [20.511889550380744, 20.0, 24.4707906554748]
keyFrame5057.FocalPathPoints = [20, 20, 20]
keyFrame5057.PositionMode = 'Path'
keyFrame5057.FocalPointMode = 'Path'
keyFrame5057.ClosedFocalPath = 0
keyFrame5057.ClosedPositionPath = 0

# ====================================================================
keyFrame5058 = CameraKeyFrame()
keyFrame5058.KeyTime = 0.145
keyFrame5058.KeyValues = [0.0]
keyFrame5058.Position = [20.520830101945574, 20.0, 24.469757935476018]
keyFrame5058.FocalPoint = [20, 20, 20]
keyFrame5058.ViewUp = [0.49654046336993185, -0.866, -0.05785846673493706]
keyFrame5058.ViewAngle = 30.0
keyFrame5058.ParallelScale = 0.97681
keyFrame5058.PositionPathPoints = [20.520830101945574, 20.0, 24.469757935476018]
keyFrame5058.FocalPathPoints = [20, 20, 20]
keyFrame5058.PositionMode = 'Path'
keyFrame5058.FocalPointMode = 'Path'
keyFrame5058.ClosedFocalPath = 0
keyFrame5058.ClosedPositionPath = 0

# ====================================================================
keyFrame5059 = CameraKeyFrame()
keyFrame5059.KeyTime = 0.1475
keyFrame5059.KeyValues = [0.0]
keyFrame5059.Position = [20.529768570195646, 20.0, 24.468707336452105]
keyFrame5059.FocalPoint = [20, 20, 20]
keyFrame5059.ViewUp = [0.4964237535561256, -0.866, -0.05885143141796989]
keyFrame5059.ViewAngle = 30.0
keyFrame5059.ParallelScale = 0.97681
keyFrame5059.PositionPathPoints = [20.529768570195646, 20.0, 24.468707336452105]
keyFrame5059.FocalPathPoints = [20, 20, 20]
keyFrame5059.PositionMode = 'Path'
keyFrame5059.FocalPointMode = 'Path'
keyFrame5059.ClosedFocalPath = 0
keyFrame5059.ClosedPositionPath = 0

# ====================================================================
keyFrame5060 = CameraKeyFrame()
keyFrame5060.KeyTime = 0.15
keyFrame5060.KeyValues = [0.0]
keyFrame5060.Position = [20.53870491936977, 20.0, 24.467638862602563]
keyFrame5060.FocalPoint = [20, 20, 20]
keyFrame5060.ViewUp = [0.49630505799432884, -0.866, -0.05984416070311369]
keyFrame5060.ViewAngle = 30.0
keyFrame5060.ParallelScale = 0.97681
keyFrame5060.PositionPathPoints = [20.53870491936977, 20.0, 24.467638862602563]
keyFrame5060.FocalPathPoints = [20, 20, 20]
keyFrame5060.PositionMode = 'Path'
keyFrame5060.FocalPointMode = 'Path'
keyFrame5060.ClosedFocalPath = 0
keyFrame5060.ClosedPositionPath = 0

# ====================================================================
keyFrame5061 = CameraKeyFrame()
keyFrame5061.KeyTime = 0.1525
keyFrame5061.KeyValues = [0.0]
keyFrame5061.Position = [20.547639113722507, 20.0, 24.46655251820115]
keyFrame5061.FocalPoint = [20, 20, 20]
keyFrame5061.ViewUp = [0.49618437715545605, -0.866, -0.06083665061749487]
keyFrame5061.ViewAngle = 30.0
keyFrame5061.ParallelScale = 0.97681
keyFrame5061.PositionPathPoints = [20.547639113722507, 20.0, 24.46655251820115]
keyFrame5061.FocalPathPoints = [20, 20, 20]
keyFrame5061.PositionMode = 'Path'
keyFrame5061.FocalPointMode = 'Path'
keyFrame5061.ClosedFocalPath = 0
keyFrame5061.ClosedPositionPath = 0

# ====================================================================
keyFrame5062 = CameraKeyFrame()
keyFrame5062.KeyTime = 0.155
keyFrame5062.KeyValues = [0.0]
keyFrame5062.Position = [20.55657111751707, 20.0, 24.465448307593153]
keyFrame5062.FocalPoint = [20, 20, 20]
keyFrame5062.ViewUp = [0.49606171152107736, -0.866, -0.06182889718904966]
keyFrame5062.ViewAngle = 30.0
keyFrame5062.ParallelScale = 0.97681
keyFrame5062.PositionPathPoints = [20.55657111751707, 20.0, 24.465448307593153]
keyFrame5062.FocalPathPoints = [20, 20, 20]
keyFrame5062.PositionMode = 'Path'
keyFrame5062.FocalPointMode = 'Path'
keyFrame5062.ClosedFocalPath = 0
keyFrame5062.ClosedPositionPath = 0

# ====================================================================
keyFrame5063 = CameraKeyFrame()
keyFrame5063.KeyTime = 0.1575
keyFrame5063.KeyValues = [0.0]
keyFrame5063.Position = [20.56550089502548, 20.0, 24.46432623519536]
keyFrame5063.FocalPoint = [20, 20, 20]
keyFrame5063.ViewUp = [0.49593706158341855, -0.866, -0.06282089644652414]
keyFrame5063.ViewAngle = 30.0
keyFrame5063.ParallelScale = 0.97681
keyFrame5063.PositionPathPoints = [20.56550089502548, 20.0, 24.46432623519536]
keyFrame5063.FocalPathPoints = [20, 20, 20]
keyFrame5063.PositionMode = 'Path'
keyFrame5063.FocalPointMode = 'Path'
keyFrame5063.ClosedFocalPath = 0
keyFrame5063.ClosedPositionPath = 0

# ====================================================================
keyFrame5064 = CameraKeyFrame()
keyFrame5064.KeyTime = 0.16
keyFrame5064.KeyValues = [0.0]
keyFrame5064.Position = [20.574428410528714, 20.0, 24.463186305496073]
keyFrame5064.FocalPoint = [20, 20, 20]
keyFrame5064.ViewUp = [0.495810427845361, -0.866, -0.06381264441947423]
keyFrame5064.ViewAngle = 30.0
keyFrame5064.ParallelScale = 0.97681
keyFrame5064.PositionPathPoints = [20.574428410528714, 20.0, 24.463186305496073]
keyFrame5064.FocalPathPoints = [20, 20, 20]
keyFrame5064.PositionMode = 'Path'
keyFrame5064.FocalPointMode = 'Path'
keyFrame5064.ClosedFocalPath = 0
keyFrame5064.ClosedPositionPath = 0

# ====================================================================
keyFrame5065 = CameraKeyFrame()
keyFrame5065.KeyTime = 0.1625
keyFrame5065.KeyValues = [0.0]
keyFrame5065.Position = [20.58335362831685, 20.0, 24.462028523055068]
keyFrame5065.FocalPoint = [20, 20, 20]
keyFrame5065.ViewUp = [0.4956818108204416, -0.866, -0.06480413713826569]
keyFrame5065.ViewAngle = 30.0
keyFrame5065.ParallelScale = 0.97681
keyFrame5065.PositionPathPoints = [20.58335362831685, 20.0, 24.462028523055068]
keyFrame5065.FocalPathPoints = [20, 20, 20]
keyFrame5065.PositionMode = 'Path'
keyFrame5065.FocalPointMode = 'Path'
keyFrame5065.ClosedFocalPath = 0
keyFrame5065.ClosedPositionPath = 0

# ====================================================================
keyFrame5066 = CameraKeyFrame()
keyFrame5066.KeyTime = 0.165
keyFrame5066.KeyValues = [0.0]
keyFrame5066.Position = [20.59227651268921, 20.0, 24.460852892503596]
keyFrame5066.FocalPoint = [20, 20, 20]
keyFrame5066.ViewUp = [0.49555121103285316, -0.866, -0.0657953706340741]
keyFrame5066.ViewAngle = 30.0
keyFrame5066.ParallelScale = 0.97681
keyFrame5066.PositionPathPoints = [20.59227651268921, 20.0, 24.460852892503596]
keyFrame5066.FocalPathPoints = [20, 20, 20]
keyFrame5066.PositionMode = 'Path'
keyFrame5066.FocalPointMode = 'Path'
keyFrame5066.ClosedFocalPath = 0
keyFrame5066.ClosedPositionPath = 0

# ====================================================================
keyFrame5067 = CameraKeyFrame()
keyFrame5067.KeyTime = 0.1675
keyFrame5067.KeyValues = [0.0]
keyFrame5067.Position = [20.601197027954512, 20.0, 24.45965941854439]
keyFrame5067.FocalPoint = [20, 20, 20]
keyFrame5067.ViewUp = [0.49541862901744377, -0.866, -0.0667863409388849]
keyFrame5067.ViewAngle = 30.0
keyFrame5067.ParallelScale = 0.97681
keyFrame5067.PositionPathPoints = [20.601197027954512, 20.0, 24.45965941854439]
keyFrame5067.FocalPathPoints = [20, 20, 20]
keyFrame5067.PositionMode = 'Path'
keyFrame5067.FocalPointMode = 'Path'
keyFrame5067.ClosedFocalPath = 0
keyFrame5067.ClosedPositionPath = 0

# ====================================================================
keyFrame5068 = CameraKeyFrame()
keyFrame5068.KeyTime = 0.17
keyFrame5068.KeyValues = [0.0]
keyFrame5068.Position = [20.61011513843101, 20.0, 24.458448105951625]
keyFrame5068.FocalPoint = [20, 20, 20]
keyFrame5068.ViewUp = [0.49528406531971747, -0.866, -0.06777704408549336]
keyFrame5068.ViewAngle = 30.0
keyFrame5068.ParallelScale = 0.97681
keyFrame5068.PositionPathPoints = [20.61011513843101, 20.0, 24.458448105951625]
keyFrame5068.FocalPathPoints = [20, 20, 20]
keyFrame5068.PositionMode = 'Path'
keyFrame5068.FocalPointMode = 'Path'
keyFrame5068.ClosedFocalPath = 0
keyFrame5068.ClosedPositionPath = 0

# ====================================================================
keyFrame5069 = CameraKeyFrame()
keyFrame5069.KeyTime = 0.1725
keyFrame5069.KeyValues = [0.0]
keyFrame5069.Position = [20.61903080844665, 20.0, 24.457218959570923]
keyFrame5069.FocalPoint = [20, 20, 20]
keyFrame5069.ViewUp = [0.4951475204958337, -0.866, -0.06876747610750458]
keyFrame5069.ViewAngle = 30.0
keyFrame5069.ParallelScale = 0.97681
keyFrame5069.PositionPathPoints = [20.61903080844665, 20.0, 24.457218959570923]
keyFrame5069.FocalPathPoints = [20, 20, 20]
keyFrame5069.PositionMode = 'Path'
keyFrame5069.FocalPointMode = 'Path'
keyFrame5069.ClosedFocalPath = 0
keyFrame5069.ClosedPositionPath = 0

# ====================================================================
keyFrame5070 = CameraKeyFrame()
keyFrame5070.KeyTime = 0.175
keyFrame5070.KeyValues = [0.0]
keyFrame5070.Position = [20.627944002339206, 20.0, 24.45597198431934]
keyFrame5070.FocalPoint = [20, 20, 20]
keyFrame5070.ViewUp = [0.4950089951126077, -0.866, -0.06975763303933354]
keyFrame5070.ViewAngle = 30.0
keyFrame5070.ParallelScale = 0.97681
keyFrame5070.PositionPathPoints = [20.627944002339206, 20.0, 24.45597198431934]
keyFrame5070.FocalPathPoints = [20, 20, 20]
keyFrame5070.PositionMode = 'Path'
keyFrame5070.FocalPointMode = 'Path'
keyFrame5070.ClosedFocalPath = 0
keyFrame5070.ClosedPositionPath = 0

# ====================================================================
keyFrame5071 = CameraKeyFrame()
keyFrame5071.KeyTime = 0.1775
keyFrame5071.KeyValues = [0.0]
keyFrame5071.Position = [20.636854684456434, 20.0, 24.454707185185352]
keyFrame5071.FocalPoint = [20, 20, 20]
keyFrame5071.ViewUp = [0.49486848974751024, -0.866, -0.07074751091620497]
keyFrame5071.ViewAngle = 30.0
keyFrame5071.ParallelScale = 0.97681
keyFrame5071.PositionPathPoints = [20.636854684456434, 20.0, 24.454707185185352]
keyFrame5071.FocalPathPoints = [20, 20, 20]
keyFrame5071.PositionMode = 'Path'
keyFrame5071.FocalPointMode = 'Path'
keyFrame5071.ClosedFocalPath = 0
keyFrame5071.ClosedPositionPath = 0

# ====================================================================
keyFrame5072 = CameraKeyFrame()
keyFrame5072.KeyTime = 0.18
keyFrame5072.KeyValues = [0.0]
keyFrame5072.Position = [20.645762819156218, 20.0, 24.453424567228847]
keyFrame5072.FocalPoint = [20, 20, 20]
keyFrame5072.ViewUp = [0.4947260049886677, -0.866, -0.07173710577415354]
keyFrame5072.ViewAngle = 30.0
keyFrame5072.ParallelScale = 0.97681
keyFrame5072.PositionPathPoints = [20.645762819156218, 20.0, 24.453424567228847]
keyFrame5072.FocalPathPoints = [20, 20, 20]
keyFrame5072.PositionMode = 'Path'
keyFrame5072.FocalPointMode = 'Path'
keyFrame5072.ClosedFocalPath = 0
keyFrame5072.ClosedPositionPath = 0

# ====================================================================
keyFrame5073 = CameraKeyFrame()
keyFrame5073.KeyTime = 0.1825
keyFrame5073.KeyValues = [0.0]
keyFrame5073.Position = [20.654668370806714, 20.0, 24.45212413558111]
keyFrame5073.FocalPoint = [20, 20, 20]
keyFrame5073.ViewUp = [0.4945815414008557, -0.866, -0.07272641365618296]
keyFrame5073.ViewAngle = 30.0
keyFrame5073.ParallelScale = 0.97681
keyFrame5073.PositionPathPoints = [20.654668370806714, 20.0, 24.45212413558111]
keyFrame5073.FocalPathPoints = [20, 20, 20]
keyFrame5073.PositionMode = 'Path'
keyFrame5073.FocalPointMode = 'Path'
keyFrame5073.ClosedFocalPath = 0
keyFrame5073.ClosedPositionPath = 0

# ====================================================================
keyFrame5074 = CameraKeyFrame()
keyFrame5074.KeyTime = 0.185
keyFrame5074.KeyValues = [0.0]
keyFrame5074.Position = [20.6635713037865, 20.0, 24.450805895444816]
keyFrame5074.FocalPoint = [20, 20, 20]
keyFrame5074.ViewUp = [0.4944350993962434, -0.866, -0.07371543063567708]
keyFrame5074.ViewAngle = 30.0
keyFrame5074.ParallelScale = 0.97681
keyFrame5074.PositionPathPoints = [20.6635713037865, 20.0, 24.450805895444816]
keyFrame5074.FocalPathPoints = [20, 20, 20]
keyFrame5074.PositionMode = 'Path'
keyFrame5074.FocalPointMode = 'Path'
keyFrame5074.ClosedFocalPath = 0
keyFrame5074.ClosedPositionPath = 0

# ====================================================================
keyFrame5075 = CameraKeyFrame()
keyFrame5075.KeyTime = 0.1875
keyFrame5075.KeyValues = [0.0]
keyFrame5075.Position = [20.672471582484715, 20.0, 24.44946985209402]
keyFrame5075.FocalPoint = [20, 20, 20]
keyFrame5075.ViewUp = [0.49428667953526234, -0.866, -0.07470415276190603]
keyFrame5075.ViewAngle = 30.0
keyFrame5075.ParallelScale = 0.97681
keyFrame5075.PositionPathPoints = [20.672471582484715, 20.0, 24.44946985209402]
keyFrame5075.FocalPathPoints = [20, 20, 20]
keyFrame5075.PositionMode = 'Path'
keyFrame5075.FocalPointMode = 'Path'
keyFrame5075.ClosedFocalPath = 0
keyFrame5075.ClosedPositionPath = 0

# ====================================================================
keyFrame5076 = CameraKeyFrame()
keyFrame5076.KeyTime = 0.19
keyFrame5076.KeyValues = [0.0]
keyFrame5076.Position = [20.681369171301213, 20.0, 24.448116010874138]
keyFrame5076.FocalPoint = [20, 20, 20]
keyFrame5076.ViewUp = [0.4941362824142006, -0.866, -0.07569257608038538]
keyFrame5076.ViewAngle = 30.0
keyFrame5076.ParallelScale = 0.97681
keyFrame5076.PositionPathPoints = [20.681369171301213, 20.0, 24.448116010874138]
keyFrame5076.FocalPathPoints = [20, 20, 20]
keyFrame5076.PositionMode = 'Path'
keyFrame5076.FocalPointMode = 'Path'
keyFrame5076.ClosedFocalPath = 0
keyFrame5076.ClosedPositionPath = 0

# ====================================================================
keyFrame5077 = CameraKeyFrame()
keyFrame5077.KeyTime = 0.1925
keyFrame5077.KeyValues = [0.0]
keyFrame5077.Position = [20.690264034646713, 20.0, 24.44674437720195]
keyFrame5077.FocalPoint = [20, 20, 20]
keyFrame5077.ViewUp = [0.4939839086386158, -0.866, -0.07668069663769159]
keyFrame5077.ViewAngle = 30.0
keyFrame5077.ParallelScale = 0.97681
keyFrame5077.PositionPathPoints = [20.690264034646713, 20.0, 24.44674437720195]
keyFrame5077.FocalPathPoints = [20, 20, 20]
keyFrame5077.PositionMode = 'Path'
keyFrame5077.FocalPointMode = 'Path'
keyFrame5077.ClosedFocalPath = 0
keyFrame5077.ClosedPositionPath = 0

# ====================================================================
keyFrame5078 = CameraKeyFrame()
keyFrame5078.KeyTime = 0.195
keyFrame5078.KeyValues = [0.0]
keyFrame5078.Position = [20.69915613694258, 20.0, 24.44535495656503]
keyFrame5078.FocalPoint = [20, 20, 20]
keyFrame5078.ViewUp = [0.4938295588233348, -0.866, -0.07766851048146206]
keyFrame5078.ViewAngle = 30.0
keyFrame5078.ParallelScale = 0.97681
keyFrame5078.PositionPathPoints = [20.69915613694258, 20.0, 24.44535495656503]
keyFrame5078.FocalPathPoints = [20, 20, 20]
keyFrame5078.PositionMode = 'Path'
keyFrame5078.FocalPointMode = 'Path'
keyFrame5078.ClosedFocalPath = 0
keyFrame5078.ClosedPositionPath = 0

# ====================================================================
keyFrame5079 = CameraKeyFrame()
keyFrame5079.KeyTime = 0.1975
keyFrame5079.KeyValues = [0.0]
keyFrame5079.Position = [20.7080454426161, 20.0, 24.443947754514355]
keyFrame5079.FocalPoint = [20, 20, 20]
keyFrame5079.ViewUp = [0.4936732335924539, -0.866, -0.07865601366039507]
keyFrame5079.ViewAngle = 30.0
keyFrame5079.ParallelScale = 0.97681
keyFrame5079.PositionPathPoints = [20.7080454426161, 20.0, 24.443947754514355]
keyFrame5079.FocalPathPoints = [20, 20, 20]
keyFrame5079.PositionMode = 'Path'
keyFrame5079.FocalPointMode = 'Path'
keyFrame5079.ClosedFocalPath = 0
keyFrame5079.ClosedPositionPath = 0

# ====================================================================
keyFrame5080 = CameraKeyFrame()
keyFrame5080.KeyTime = 0.2
keyFrame5080.KeyValues = [0.0]
keyFrame5080.Position = [20.71693191610843, 20.0, 24.442522776676107]
keyFrame5080.FocalPoint = [20, 20, 20]
keyFrame5080.ViewUp = [0.493514933579339, -0.866, -0.07964320222424985]
keyFrame5080.ViewAngle = 30.0
keyFrame5080.ParallelScale = 0.97681
keyFrame5080.PositionPathPoints = [20.71693191610843, 20.0, 24.442522776676107]
keyFrame5080.FocalPathPoints = [20, 20, 20]
keyFrame5080.PositionMode = 'Path'
keyFrame5080.FocalPointMode = 'Path'
keyFrame5080.ClosedFocalPath = 0
keyFrame5080.ClosedPositionPath = 0

# ====================================================================
keyFrame5081 = CameraKeyFrame()
keyFrame5081.KeyTime = 0.2025
keyFrame5081.KeyValues = [0.0]
keyFrame5081.Position = [20.72581552187366, 20.0, 24.44108002875007]
keyFrame5081.FocalPoint = [20, 20, 20]
keyFrame5081.ViewUp = [0.49335465942662526, -0.866, -0.08063007222384651]
keyFrame5081.ViewAngle = 30.0
keyFrame5081.ParallelScale = 0.97681
keyFrame5081.PositionPathPoints = [20.72581552187366, 20.0, 24.44108002875007]
keyFrame5081.FocalPathPoints = [20, 20, 20]
keyFrame5081.PositionMode = 'Path'
keyFrame5081.FocalPointMode = 'Path'
keyFrame5081.ClosedFocalPath = 0
keyFrame5081.ClosedPositionPath = 0

# ====================================================================
keyFrame5082 = CameraKeyFrame()
keyFrame5082.KeyTime = 0.205
keyFrame5082.KeyValues = [0.0]
keyFrame5082.Position = [20.73469622437738, 20.0, 24.43961951650715]
keyFrame5082.FocalPoint = [20, 20, 20]
keyFrame5082.ViewUp = [0.4931924117862173, -0.866, -0.08161661971106608]
keyFrame5082.ViewAngle = 30.0
keyFrame5082.ParallelScale = 0.97681
keyFrame5082.PositionPathPoints = [20.73469622437738, 20.0, 24.43961951650715]
keyFrame5082.FocalPathPoints = [20, 20, 20]
keyFrame5082.PositionMode = 'Path'
keyFrame5082.FocalPointMode = 'Path'
keyFrame5082.ClosedFocalPath = 0
keyFrame5082.ClosedPositionPath = 0

# ====================================================================
keyFrame5083 = CameraKeyFrame()
keyFrame5083.KeyTime = 0.2075
keyFrame5083.KeyValues = [0.0]
keyFrame5083.Position = [20.743573988096784, 20.0, 24.438141245789357]
keyFrame5083.FocalPoint = [20, 20, 20]
keyFrame5083.ViewUp = [0.49302819131928904, -0.866, -0.08260284073885049]
keyFrame5083.ViewAngle = 30.0
keyFrame5083.ParallelScale = 0.97681
keyFrame5083.PositionPathPoints = [20.743573988096784, 20.0, 24.438141245789357]
keyFrame5083.FocalPathPoints = [20, 20, 20]
keyFrame5083.PositionMode = 'Path'
keyFrame5083.FocalPointMode = 'Path'
keyFrame5083.ClosedFocalPath = 0
keyFrame5083.ClosedPositionPath = 0

# ====================================================================
keyFrame5084 = CameraKeyFrame()
keyFrame5084.KeyTime = 0.21
keyFrame5084.KeyValues = [0.0]
keyFrame5084.Position = [20.75244877752084, 20.0, 24.436645222509796]
keyFrame5084.FocalPoint = [20, 20, 20]
keyFrame5084.ViewUp = [0.49286199869628405, -0.866, -0.08358873136120262]
keyFrame5084.ViewAngle = 30.0
keyFrame5084.ParallelScale = 0.97681
keyFrame5084.PositionPathPoints = [20.75244877752084, 20.0, 24.436645222509796]
keyFrame5084.FocalPathPoints = [20, 20, 20]
keyFrame5084.PositionMode = 'Path'
keyFrame5084.FocalPointMode = 'Path'
keyFrame5084.ClosedFocalPath = 0
keyFrame5084.ClosedPositionPath = 0

# ====================================================================
keyFrame5085 = CameraKeyFrame()
keyFrame5085.KeyTime = 0.2125
keyFrame5085.KeyValues = [0.0]
keyFrame5085.Position = [20.761320557150405, 20.0, 24.43513145265264]
keyFrame5085.FocalPoint = [20, 20, 20]
keyFrame5085.ViewUp = [0.4926938345969151, -0.866, -0.0845742876331862]
keyFrame5085.ViewAngle = 30.0
keyFrame5085.ParallelScale = 0.97681
keyFrame5085.PositionPathPoints = [20.761320557150405, 20.0, 24.43513145265264]
keyFrame5085.FocalPathPoints = [20, 20, 20]
keyFrame5085.PositionMode = 'Path'
keyFrame5085.FocalPointMode = 'Path'
keyFrame5085.ClosedFocalPath = 0
keyFrame5085.ClosedPositionPath = 0

# ====================================================================
keyFrame5086 = CameraKeyFrame()
keyFrame5086.KeyTime = 0.215
keyFrame5086.KeyValues = [0.0]
keyFrame5086.Position = [20.7701892914984, 20.0, 24.433599942273126]
keyFrame5086.FocalPoint = [20, 20, 20]
keyFrame5086.ViewUp = [0.4925236997101645, -0.866, -0.08555950561092593]
keyFrame5086.ViewAngle = 30.0
keyFrame5086.ParallelScale = 0.97681
keyFrame5086.PositionPathPoints = [20.7701892914984, 20.0, 24.433599942273126]
keyFrame5086.FocalPathPoints = [20, 20, 20]
keyFrame5086.PositionMode = 'Path'
keyFrame5086.FocalPointMode = 'Path'
keyFrame5086.ClosedFocalPath = 0
keyFrame5086.ClosedPositionPath = 0

# ====================================================================
keyFrame5087 = CameraKeyFrame()
keyFrame5087.KeyTime = 0.2175
keyFrame5087.KeyValues = [0.0]
keyFrame5087.Position = [20.779054945089936, 20.0, 24.43205069749752]
keyFrame5087.FocalPoint = [20, 20, 20]
keyFrame5087.ViewUp = [0.49235159473428397, -0.866, -0.08654438135160739]
keyFrame5087.ViewAngle = 30.0
keyFrame5087.ParallelScale = 0.97681
keyFrame5087.PositionPathPoints = [20.779054945089936, 20.0, 24.43205069749752]
keyFrame5087.FocalPathPoints = [20, 20, 20]
keyFrame5087.PositionMode = 'Path'
keyFrame5087.FocalPointMode = 'Path'
keyFrame5087.ClosedFocalPath = 0
keyFrame5087.ClosedPositionPath = 0

# ====================================================================
keyFrame5088 = CameraKeyFrame()
keyFrame5088.KeyTime = 0.22
keyFrame5088.KeyValues = [0.0]
keyFrame5088.Position = [20.787917482462447, 20.0, 24.43048372452312]
keyFrame5088.FocalPoint = [20, 20, 20]
keyFrame5088.ViewUp = [0.49217752037679463, -0.866, -0.08752891091347706]
keyFrame5088.ViewAngle = 30.0
keyFrame5088.ParallelScale = 0.97681
keyFrame5088.PositionPathPoints = [20.787917482462447, 20.0, 24.43048372452312]
keyFrame5088.FocalPathPoints = [20, 20, 20]
keyFrame5088.PositionMode = 'Path'
keyFrame5088.FocalPointMode = 'Path'
keyFrame5088.ClosedFocalPath = 0
keyFrame5088.ClosedPositionPath = 0

# ====================================================================
keyFrame5089 = CameraKeyFrame()
keyFrame5089.KeyTime = 0.2225
keyFrame5089.KeyValues = [0.0]
keyFrame5089.Position = [20.796776868165857, 20.0, 24.428899029618236]
keyFrame5089.FocalPoint = [20, 20, 20]
keyFrame5089.ViewUp = [0.4920014773544869, -0.866, -0.08851309035584237]
keyFrame5089.ViewAngle = 30.0
keyFrame5089.ParallelScale = 0.97681
keyFrame5089.PositionPathPoints = [20.796776868165857, 20.0, 24.428899029618236]
keyFrame5089.FocalPathPoints = [20, 20, 20]
keyFrame5089.PositionMode = 'Path'
keyFrame5089.FocalPointMode = 'Path'
keyFrame5089.ClosedFocalPath = 0
keyFrame5089.ClosedPositionPath = 0

# ====================================================================
keyFrame5090 = CameraKeyFrame()
keyFrame5090.KeyTime = 0.225
keyFrame5090.KeyValues = [0.0]
keyFrame5090.Position = [20.805633066762702, 20.0, 24.42729661912216]
keyFrame5090.FocalPoint = [20, 20, 20]
keyFrame5090.ViewUp = [0.49182346639342084, -0.866, -0.08949691573907162]
keyFrame5090.ViewAngle = 30.0
keyFrame5090.ParallelScale = 0.97681
keyFrame5090.PositionPathPoints = [20.805633066762702, 20.0, 24.42729661912216]
keyFrame5090.FocalPathPoints = [20, 20, 20]
keyFrame5090.PositionMode = 'Path'
keyFrame5090.FocalPointMode = 'Path'
keyFrame5090.ClosedFocalPath = 0
keyFrame5090.ClosedPositionPath = 0

# ====================================================================
keyFrame5091 = CameraKeyFrame()
keyFrame5091.KeyTime = 0.2275
keyFrame5091.KeyValues = [0.0]
keyFrame5091.Position = [20.81448604282829, 20.0, 24.425676499445153]
keyFrame5091.FocalPoint = [20, 20, 20]
keyFrame5091.ViewUp = [0.49164348822892573, -0.866, -0.09048038312459407]
keyFrame5091.ViewAngle = 30.0
keyFrame5091.ParallelScale = 0.97681
keyFrame5091.PositionPathPoints = [20.81448604282829, 20.0, 24.425676499445153]
keyFrame5091.FocalPathPoints = [20, 20, 20]
keyFrame5091.PositionMode = 'Path'
keyFrame5091.FocalPointMode = 'Path'
keyFrame5091.ClosedFocalPath = 0
keyFrame5091.ClosedPositionPath = 0

# ====================================================================
keyFrame5092 = CameraKeyFrame()
keyFrame5092.KeyTime = 0.23
keyFrame5092.KeyValues = [0.0]
keyFrame5092.Position = [20.823335760950823, 20.0, 24.424038677068452]
keyFrame5092.FocalPoint = [20, 20, 20]
keyFrame5092.ViewUp = [0.4914615436056004, -0.866, -0.09146348857489982]
keyFrame5092.ViewAngle = 30.0
keyFrame5092.ParallelScale = 0.97681
keyFrame5092.PositionPathPoints = [20.823335760950823, 20.0, 24.424038677068452]
keyFrame5092.FocalPathPoints = [20, 20, 20]
keyFrame5092.PositionMode = 'Path'
keyFrame5092.FocalPointMode = 'Path'
keyFrame5092.ClosedFocalPath = 0
keyFrame5092.ClosedPositionPath = 0

# ====================================================================
keyFrame5093 = CameraKeyFrame()
keyFrame5093.KeyTime = 0.2325
keyFrame5093.KeyValues = [0.0]
keyFrame5093.Position = [20.83218218573157, 20.0, 24.422383158544218]
keyFrame5093.FocalPoint = [20, 20, 20]
keyFrame5093.ViewUp = [0.491277633277313, -0.866, -0.09244622815353995]
keyFrame5093.ViewAngle = 30.0
keyFrame5093.ParallelScale = 0.97681
keyFrame5093.PositionPathPoints = [20.83218218573157, 20.0, 24.422383158544218]
keyFrame5093.FocalPathPoints = [20, 20, 20]
keyFrame5093.PositionMode = 'Path'
keyFrame5093.FocalPointMode = 'Path'
keyFrame5093.ClosedFocalPath = 0
keyFrame5093.ClosedPositionPath = 0

# ====================================================================
keyFrame5094 = CameraKeyFrame()
keyFrame5094.KeyTime = 0.235
keyFrame5094.KeyValues = [0.0]
keyFrame5094.Position = [20.841025281784976, 20.0, 24.420709950495542]
keyFrame5094.FocalPoint = [20, 20, 20]
keyFrame5094.ViewUp = [0.4910917580072012, -0.866, -0.09342859792512641]
keyFrame5094.ViewAngle = 30.0
keyFrame5094.ParallelScale = 0.97681
keyFrame5094.PositionPathPoints = [20.841025281784976, 20.0, 24.420709950495542]
keyFrame5094.FocalPathPoints = [20, 20, 20]
keyFrame5094.PositionMode = 'Path'
keyFrame5094.FocalPointMode = 'Path'
keyFrame5094.ClosedFocalPath = 0
keyFrame5094.ClosedPositionPath = 0

# ====================================================================
keyFrame5095 = CameraKeyFrame()
keyFrame5095.KeyTime = 0.2375
keyFrame5095.KeyValues = [0.0]
keyFrame5095.Position = [20.84986501373883, 20.0, 24.419019059616428]
keyFrame5095.FocalPoint = [20, 20, 20]
keyFrame5095.ViewUp = [0.49090391856767196, -0.866, -0.09441059395533208]
keyFrame5095.ViewAngle = 30.0
keyFrame5095.ParallelScale = 0.97681
keyFrame5095.PositionPathPoints = [20.84986501373883, 20.0, 24.419019059616428]
keyFrame5095.FocalPathPoints = [20, 20, 20]
keyFrame5095.PositionMode = 'Path'
keyFrame5095.FocalPointMode = 'Path'
keyFrame5095.ClosedFocalPath = 0
keyFrame5095.ClosedPositionPath = 0

# ====================================================================
keyFrame5096 = CameraKeyFrame()
keyFrame5096.KeyTime = 0.24
keyFrame5096.KeyValues = [0.0]
keyFrame5096.Position = [20.8587013462344, 20.0, 24.41731049267176]
keyFrame5096.FocalPoint = [20, 20, 20]
keyFrame5096.ViewUp = [0.49071411568130807, -0.866, -0.09539221232283793]
keyFrame5096.ViewAngle = 30.0
keyFrame5096.ParallelScale = 0.97681
keyFrame5096.PositionPathPoints = [20.8587013462344, 20.0, 24.41731049267176]
keyFrame5096.FocalPathPoints = [20, 20, 20]
keyFrame5096.PositionMode = 'Path'
keyFrame5096.FocalPointMode = 'Path'
keyFrame5096.ClosedFocalPath = 0
keyFrame5096.ClosedPositionPath = 0

# ====================================================================
keyFrame5097 = CameraKeyFrame()
keyFrame5097.KeyTime = 0.2425
keyFrame5097.KeyValues = [0.0]
keyFrame5097.Position = [20.867534243926578, 20.0, 24.41558425649731]
keyFrame5097.FocalPoint = [20, 20, 20]
keyFrame5097.ViewUp = [0.49052234994692545, -0.866, -0.09637344913428213]
keyFrame5097.ViewAngle = 30.0
keyFrame5097.ParallelScale = 0.97681
keyFrame5097.PositionPathPoints = [20.867534243926578, 20.0, 24.41558425649731]
keyFrame5097.FocalPathPoints = [20, 20, 20]
keyFrame5097.PositionMode = 'Path'
keyFrame5097.FocalPointMode = 'Path'
keyFrame5097.ClosedFocalPath = 0
keyFrame5097.ClosedPositionPath = 0

# ====================================================================
keyFrame5098 = CameraKeyFrame()
keyFrame5098.KeyTime = 0.245
keyFrame5098.KeyValues = [0.0]
keyFrame5098.Position = [20.876363671483873, 20.0, 24.41384035799873]
keyFrame5098.FocalPoint = [20, 20, 20]
keyFrame5098.ViewUp = [0.49032862212019596, -0.866, -0.0973543004675258]
keyFrame5098.ViewAngle = 30.0
keyFrame5098.ParallelScale = 0.97681
keyFrame5098.PositionPathPoints = [20.876363671483873, 20.0, 24.41384035799873]
keyFrame5098.FocalPathPoints = [20, 20, 20]
keyFrame5098.PositionMode = 'Path'
keyFrame5098.FocalPointMode = 'Path'
keyFrame5098.ClosedFocalPath = 0
keyFrame5098.ClosedPositionPath = 0

# ====================================================================
keyFrame5099 = CameraKeyFrame()
keyFrame5099.KeyTime = 0.2475
keyFrame5099.KeyValues = [0.0]
keyFrame5099.Position = [20.885189593587537, 20.0, 24.4120788041442]
keyFrame5099.FocalPoint = [20, 20, 20]
keyFrame5099.ViewUp = [0.49013293297600524, -0.866, -0.0983347623994805]
keyFrame5099.ViewAngle = 30.0
keyFrame5099.ParallelScale = 0.97681
keyFrame5099.PositionPathPoints = [20.885189593587537, 20.0, 24.4120788041442]
keyFrame5099.FocalPathPoints = [20, 20, 20]
keyFrame5099.PositionMode = 'Path'
keyFrame5099.FocalPointMode = 'Path'
keyFrame5099.ClosedFocalPath = 0
keyFrame5099.ClosedPositionPath = 0

# ====================================================================
keyFrame5100 = CameraKeyFrame()
keyFrame5100.KeyTime = 0.25
keyFrame5100.KeyValues = [0.0]
keyFrame5100.Position = [20.894011974933598, 20.0, 24.410299601977883]
keyFrame5100.FocalPoint = [20, 20, 20]
keyFrame5100.ViewUp = [0.48993528329712577, -0.866, -0.09931483100839814]
keyFrame5100.ViewAngle = 30.0
keyFrame5100.ParallelScale = 0.97681
keyFrame5100.PositionPathPoints = [20.894011974933598, 20.0, 24.410299601977883]
keyFrame5100.FocalPathPoints = [20, 20, 20]
keyFrame5100.PositionMode = 'Path'
keyFrame5100.FocalPointMode = 'Path'
keyFrame5100.ClosedFocalPath = 0
keyFrame5100.ClosedPositionPath = 0

# ====================================================================
keyFrame5101 = CameraKeyFrame()
keyFrame5101.KeyTime = 0.2525
keyFrame5101.KeyValues = [0.0]
keyFrame5101.Position = [20.90283078023252, 20.0, 24.40850275861646]
keyFrame5101.FocalPoint = [20, 20, 20]
keyFrame5101.ViewUp = [0.48973567387421674, -0.866, -0.10029450237387112]
keyFrame5101.ViewAngle = 30.0
keyFrame5101.ParallelScale = 0.97681
keyFrame5101.PositionPathPoints = [20.90283078023252, 20.0, 24.40850275861646]
keyFrame5101.FocalPathPoints = [20, 20, 20]
keyFrame5101.PositionMode = 'Path'
keyFrame5101.FocalPointMode = 'Path'
keyFrame5101.ClosedFocalPath = 0
keyFrame5101.ClosedPositionPath = 0

# ====================================================================
keyFrame5102 = CameraKeyFrame()
keyFrame5102.KeyTime = 0.255
keyFrame5102.KeyValues = [0.0]
keyFrame5102.Position = [20.911645974209083, 20.0, 24.406688281247227]
keyFrame5102.FocalPoint = [20, 20, 20]
keyFrame5102.ViewUp = [0.48953410550582444, -0.866, -0.10127377257683229]
keyFrame5102.ViewAngle = 30.0
keyFrame5102.ParallelScale = 0.97681
keyFrame5102.PositionPathPoints = [20.911645974209083, 20.0, 24.406688281247227]
keyFrame5102.FocalPathPoints = [20, 20, 20]
keyFrame5102.PositionMode = 'Path'
keyFrame5102.FocalPointMode = 'Path'
keyFrame5102.ClosedFocalPath = 0
keyFrame5102.ClosedPositionPath = 0

# ====================================================================
keyFrame5103 = CameraKeyFrame()
keyFrame5103.KeyTime = 0.2575
keyFrame5103.KeyValues = [0.0]
keyFrame5103.Position = [20.920457521602508, 20.0, 24.404856177128064]
keyFrame5103.FocalPoint = [20, 20, 20]
keyFrame5103.ViewUp = [0.4893305789983817, -0.866, -0.10225263769955484]
keyFrame5103.ViewAngle = 30.0
keyFrame5103.ParallelScale = 0.97681
keyFrame5103.PositionPathPoints = [20.920457521602508, 20.0, 24.404856177128064]
keyFrame5103.FocalPathPoints = [20, 20, 20]
keyFrame5103.PositionMode = 'Path'
keyFrame5103.FocalPointMode = 'Path'
keyFrame5103.ClosedFocalPath = 0
keyFrame5103.ClosedPositionPath = 0

# ====================================================================
keyFrame5104 = CameraKeyFrame()
keyFrame5104.KeyTime = 0.26
keyFrame5104.KeyValues = [0.0]
keyFrame5104.Position = [20.929265387166623, 20.0, 24.403006453587405]
keyFrame5104.FocalPoint = [20, 20, 20]
keyFrame5104.ViewUp = [0.48912509516620856, -0.866, -0.10323109382565249]
keyFrame5104.ViewAngle = 30.0
keyFrame5104.ParallelScale = 0.97681
keyFrame5104.PositionPathPoints = [20.929265387166623, 20.0, 24.403006453587405]
keyFrame5104.FocalPathPoints = [20, 20, 20]
keyFrame5104.PositionMode = 'Path'
keyFrame5104.FocalPointMode = 'Path'
keyFrame5104.ClosedFocalPath = 0
keyFrame5104.ClosedPositionPath = 0

# ====================================================================
keyFrame5105 = CameraKeyFrame()
keyFrame5105.KeyTime = 0.2625
keyFrame5105.KeyValues = [0.0]
keyFrame5105.Position = [20.938069535669985, 20.0, 24.401139118024236]
keyFrame5105.FocalPoint = [20, 20, 20]
keyFrame5105.ViewUp = [0.4889176548315116, -0.866, -0.1042091370400793]
keyFrame5105.ViewAngle = 30.0
keyFrame5105.ParallelScale = 0.97681
keyFrame5105.PositionPathPoints = [20.938069535669985, 20.0, 24.401139118024236]
keyFrame5105.FocalPathPoints = [20, 20, 20]
keyFrame5105.PositionMode = 'Path'
keyFrame5105.FocalPointMode = 'Path'
keyFrame5105.ClosedFocalPath = 0
keyFrame5105.ClosedPositionPath = 0

# ====================================================================
keyFrame5106 = CameraKeyFrame()
keyFrame5106.KeyTime = 0.265
keyFrame5106.KeyValues = [0.0]
keyFrame5106.Position = [20.946869931896035, 20.0, 24.399254177908055]
keyFrame5106.FocalPoint = [20, 20, 20]
keyFrame5106.ViewUp = [0.48870825882438446, -0.866, -0.10518676342912985]
keyFrame5106.ViewAngle = 30.0
keyFrame5106.ParallelScale = 0.97681
keyFrame5106.PositionPathPoints = [20.946869931896035, 20.0, 24.399254177908055]
keyFrame5106.FocalPathPoints = [20, 20, 20]
keyFrame5106.PositionMode = 'Path'
keyFrame5106.FocalPointMode = 'Path'
keyFrame5106.ClosedFocalPath = 0
keyFrame5106.ClosedPositionPath = 0

# ====================================================================
keyFrame5107 = CameraKeyFrame()
keyFrame5107.KeyTime = 0.2675
keyFrame5107.KeyValues = [0.0]
keyFrame5107.Position = [20.955666540643236, 20.0, 24.397351640778858]
keyFrame5107.FocalPoint = [20, 20, 20]
keyFrame5107.ViewUp = [0.4884969079828075, -0.866, -0.10616396908043906]
keyFrame5107.ViewAngle = 30.0
keyFrame5107.ParallelScale = 0.97681
keyFrame5107.PositionPathPoints = [20.955666540643236, 20.0, 24.397351640778858]
keyFrame5107.FocalPathPoints = [20, 20, 20]
keyFrame5107.PositionMode = 'Path'
keyFrame5107.FocalPointMode = 'Path'
keyFrame5107.ClosedFocalPath = 0
keyFrame5107.ClosedPositionPath = 0

# ====================================================================
keyFrame5108 = CameraKeyFrame()
keyFrame5108.KeyTime = 0.27
keyFrame5108.KeyValues = [0.0]
keyFrame5108.Position = [20.964459326725216, 20.0, 24.39543151424711]
keyFrame5108.FocalPoint = [20, 20, 20]
keyFrame5108.ViewUp = [0.48828360315264796, -0.866, -0.10714075008298234]
keyFrame5108.ViewAngle = 30.0
keyFrame5108.ParallelScale = 0.97681
keyFrame5108.PositionPathPoints = [20.964459326725216, 20.0, 24.39543151424711]
keyFrame5108.FocalPathPoints = [20, 20, 20]
keyFrame5108.PositionMode = 'Path'
keyFrame5108.FocalPointMode = 'Path'
keyFrame5108.ClosedFocalPath = 0
keyFrame5108.ClosedPositionPath = 0

# ====================================================================
keyFrame5109 = CameraKeyFrame()
keyFrame5109.KeyTime = 0.2725
keyFrame5109.KeyValues = [0.0]
keyFrame5109.Position = [20.973248254970898, 20.0, 24.393493805993742]
keyFrame5109.FocalPoint = [20, 20, 20]
keyFrame5109.ViewUp = [0.48806834518765996, -0.866, -0.10811710252707549]
keyFrame5109.ViewAngle = 30.0
keyFrame5109.ParallelScale = 0.97681
keyFrame5109.PositionPathPoints = [20.973248254970898, 20.0, 24.393493805993742]
keyFrame5109.FocalPathPoints = [20, 20, 20]
keyFrame5109.PositionMode = 'Path'
keyFrame5109.FocalPointMode = 'Path'
keyFrame5109.ClosedFocalPath = 0
keyFrame5109.ClosedPositionPath = 0

# ====================================================================
keyFrame5110 = CameraKeyFrame()
keyFrame5110.KeyTime = 0.275
keyFrame5110.KeyValues = [0.0]
keyFrame5110.Position = [20.982033290224674, 20.0, 24.391538523770095]
keyFrame5110.FocalPoint = [20, 20, 20]
keyFrame5110.ViewUp = [0.4878511349494845, -0.866, -0.10909302250437478]
keyFrame5110.ViewAngle = 30.0
keyFrame5110.ParallelScale = 0.97681
keyFrame5110.PositionPathPoints = [20.982033290224674, 20.0, 24.391538523770095]
keyFrame5110.FocalPathPoints = [20, 20, 20]
keyFrame5110.PositionMode = 'Path'
keyFrame5110.FocalPointMode = 'Path'
keyFrame5110.ClosedFocalPath = 0
keyFrame5110.ClosedPositionPath = 0

# ====================================================================
keyFrame5111 = CameraKeyFrame()
keyFrame5111.KeyTime = 0.2775
keyFrame5111.KeyValues = [0.0]
keyFrame5111.Position = [20.990814397346504, 20.0, 24.389565675397925]
keyFrame5111.FocalPoint = [20, 20, 20]
keyFrame5111.ViewUp = [0.48763197330764935, -0.866, -0.11006850610787687]
keyFrame5111.ViewAngle = 30.0
keyFrame5111.ParallelScale = 0.97681
keyFrame5111.PositionPathPoints = [20.990814397346504, 20.0, 24.389565675397925]
keyFrame5111.FocalPathPoints = [20, 20, 20]
keyFrame5111.PositionMode = 'Path'
keyFrame5111.FocalPointMode = 'Path'
keyFrame5111.ClosedFocalPath = 0
keyFrame5111.ClosedPositionPath = 0

# ====================================================================
keyFrame5112 = CameraKeyFrame()
keyFrame5112.KeyTime = 0.28
keyFrame5112.KeyValues = [0.0]
keyFrame5112.Position = [20.9995915412121, 20.0, 24.387575268769382]
keyFrame5112.FocalPoint = [20, 20, 20]
keyFrame5112.ViewUp = [0.48741086113956916, -0.866, -0.11104354943191888]
keyFrame5112.ViewAngle = 30.0
keyFrame5112.ParallelScale = 0.97681
keyFrame5112.PositionPathPoints = [20.9995915412121, 20.0, 24.387575268769382]
keyFrame5112.FocalPathPoints = [20, 20, 20]
keyFrame5112.PositionMode = 'Path'
keyFrame5112.FocalPointMode = 'Path'
keyFrame5112.ClosedFocalPath = 0
keyFrame5112.ClosedPositionPath = 0

# ====================================================================
keyFrame5113 = CameraKeyFrame()
keyFrame5113.KeyTime = 0.2825
keyFrame5113.KeyValues = [0.0]
keyFrame5113.Position = [21.008364686713037, 20.0, 24.385567311846962]
keyFrame5113.FocalPoint = [20, 20, 20]
keyFrame5113.ViewUp = [0.4871877993305455, -0.866, -0.11201814857217832]
keyFrame5113.ViewAngle = 30.0
keyFrame5113.ParallelScale = 0.97681
keyFrame5113.PositionPathPoints = [21.008364686713037, 20.0, 24.385567311846962]
keyFrame5113.FocalPathPoints = [20, 20, 20]
keyFrame5113.PositionMode = 'Path'
keyFrame5113.FocalPointMode = 'Path'
keyFrame5113.ClosedFocalPath = 0
keyFrame5113.ClosedPositionPath = 0

# ====================================================================
keyFrame5114 = CameraKeyFrame()
keyFrame5114.KeyTime = 0.285
keyFrame5114.KeyValues = [0.0]
keyFrame5114.Position = [21.017133798756912, 20.0, 24.383541812663513]
keyFrame5114.FocalPoint = [20, 20, 20]
keyFrame5114.ViewUp = [0.4869627887737667, -0.866, -0.11299229962567317]
keyFrame5114.ViewAngle = 30.0
keyFrame5114.ParallelScale = 0.97681
keyFrame5114.PositionPathPoints = [21.017133798756912, 20.0, 24.383541812663513]
keyFrame5114.FocalPathPoints = [20, 20, 20]
keyFrame5114.PositionMode = 'Path'
keyFrame5114.FocalPointMode = 'Path'
keyFrame5114.ClosedFocalPath = 0
keyFrame5114.ClosedPositionPath = 0

# ====================================================================
keyFrame5115 = CameraKeyFrame()
keyFrame5115.KeyTime = 0.2875
keyFrame5115.KeyValues = [0.0]
keyFrame5115.Position = [21.02589884226748, 20.0, 24.381498779322193]
keyFrame5115.FocalPoint = [20, 20, 20]
keyFrame5115.ViewUp = [0.48673583037030793, -0.866, -0.11396599869076181]
keyFrame5115.ViewAngle = 30.0
keyFrame5115.ParallelScale = 0.97681
keyFrame5115.PositionPathPoints = [21.02589884226748, 20.0, 24.381498779322193]
keyFrame5115.FocalPathPoints = [20, 20, 20]
keyFrame5115.PositionMode = 'Path'
keyFrame5115.FocalPointMode = 'Path'
keyFrame5115.ClosedFocalPath = 0
keyFrame5115.ClosedPositionPath = 0

# ====================================================================
keyFrame5116 = CameraKeyFrame()
keyFrame5116.KeyTime = 0.29
keyFrame5116.KeyValues = [0.0]
keyFrame5116.Position = [21.0346597821848, 20.0, 24.379438219996462]
keyFrame5116.FocalPoint = [20, 20, 20]
keyFrame5116.ViewUp = [0.4865069250291313, -0.866, -0.11493924186714308]
keyFrame5116.ViewAngle = 30.0
keyFrame5116.ParallelScale = 0.97681
keyFrame5116.PositionPathPoints = [21.0346597821848, 20.0, 24.379438219996462]
keyFrame5116.FocalPathPoints = [20, 20, 20]
keyFrame5116.PositionMode = 'Path'
keyFrame5116.FocalPointMode = 'Path'
keyFrame5116.ClosedFocalPath = 0
keyFrame5116.ClosedPositionPath = 0

# ====================================================================
keyFrame5117 = CameraKeyFrame()
keyFrame5117.KeyTime = 0.2925
keyFrame5117.KeyValues = [0.0]
keyFrame5117.Position = [21.04341658346537, 20.0, 24.37736014293005]
keyFrame5117.FocalPoint = [20, 20, 20]
keyFrame5117.ViewUp = [0.4862760736670857, -0.866, -0.1159120252558562]
keyFrame5117.ViewAngle = 30.0
keyFrame5117.ParallelScale = 0.97681
keyFrame5117.PositionPathPoints = [21.04341658346537, 20.0, 24.37736014293005]
keyFrame5117.FocalPathPoints = [20, 20, 20]
keyFrame5117.PositionMode = 'Path'
keyFrame5117.FocalPointMode = 'Path'
keyFrame5117.ClosedFocalPath = 0
keyFrame5117.ClosedPositionPath = 0

# ====================================================================
keyFrame5118 = CameraKeyFrame()
keyFrame5118.KeyTime = 0.295
keyFrame5118.KeyValues = [0.0]
keyFrame5118.Position = [21.052169211078407, 20.0, 24.375264556414503]
keyFrame5118.FocalPoint = [20, 20, 20]
keyFrame5118.ViewUp = [0.48604327720890694, -0.866, -0.11688434495928086]
keyFrame5118.ViewAngle = 30.0
keyFrame5118.ParallelScale = 0.97681
keyFrame5118.PositionPathPoints = [21.052169211078407, 20.0, 24.375264556414503]
keyFrame5118.FocalPathPoints = [20, 20, 20]
keyFrame5118.PositionMode = 'Path'
keyFrame5118.FocalPointMode = 'Path'
keyFrame5118.ClosedFocalPath = 0
keyFrame5118.ClosedPositionPath = 0

# ====================================================================
keyFrame5119 = CameraKeyFrame()
keyFrame5119.KeyTime = 0.2975
keyFrame5119.KeyValues = [0.0]
keyFrame5119.Position = [21.06091763002032, 20.0, 24.37315146887225]
keyFrame5119.FocalPoint = [20, 20, 20]
keyFrame5119.ViewUp = [0.48580853658240397, -0.866, -0.11785619710435885]
keyFrame5119.ViewAngle = 30.0
keyFrame5119.ParallelScale = 0.97681
keyFrame5119.PositionPathPoints = [21.06091763002032, 20.0, 24.37315146887225]
keyFrame5119.FocalPathPoints = [20, 20, 20]
keyFrame5119.PositionMode = 'Path'
keyFrame5119.FocalPointMode = 'Path'
keyFrame5119.ClosedFocalPath = 0
keyFrame5119.ClosedPositionPath = 0

# ====================================================================
keyFrame5120 = CameraKeyFrame()
keyFrame5120.KeyTime = 0.3
keyFrame5120.KeyValues = [0.0]
keyFrame5120.Position = [21.069661805292352, 20.0, 24.37102088872615]
keyFrame5120.FocalPoint = [20, 20, 20]
keyFrame5120.ViewUp = [0.4855718527189277, -0.866, -0.11882757784033317]
keyFrame5120.ViewAngle = 30.0
keyFrame5120.ParallelScale = 0.97681
keyFrame5120.PositionPathPoints = [21.069661805292352, 20.0, 24.37102088872615]
keyFrame5120.FocalPathPoints = [20, 20, 20]
keyFrame5120.PositionMode = 'Path'
keyFrame5120.FocalPointMode = 'Path'
keyFrame5120.ClosedFocalPath = 0
keyFrame5120.ClosedPositionPath = 0

# ====================================================================
keyFrame5121 = CameraKeyFrame()
keyFrame5121.KeyTime = 0.3025
keyFrame5121.KeyValues = [0.0]
keyFrame5121.Position = [21.078401701917834, 20.0, 24.368872824498677]
keyFrame5121.FocalPoint = [20, 20, 20]
keyFrame5121.ViewUp = [0.4853332265649849, -0.866, -0.11979848328272055]
keyFrame5121.ViewAngle = 30.0
keyFrame5121.ParallelScale = 0.97681
keyFrame5121.PositionPathPoints = [21.078401701917834, 20.0, 24.368872824498677]
keyFrame5121.FocalPathPoints = [20, 20, 20]
keyFrame5121.PositionMode = 'Path'
keyFrame5121.FocalPointMode = 'Path'
keyFrame5121.ClosedFocalPath = 0
keyFrame5121.ClosedPositionPath = 0

# ====================================================================
keyFrame5122 = CameraKeyFrame()
keyFrame5122.KeyTime = 0.305
keyFrame5122.KeyValues = [0.0]
keyFrame5122.Position = [21.087137284937214, 20.0, 24.36670728478224]
keyFrame5122.FocalPoint = [20, 20, 20]
keyFrame5122.ViewUp = [0.48509265907502574, -0.866, -0.12076890954810453]
keyFrame5122.ViewAngle = 30.0
keyFrame5122.ParallelScale = 0.97681
keyFrame5122.PositionPathPoints = [21.087137284937214, 20.0, 24.36670728478224]
keyFrame5122.FocalPathPoints = [20, 20, 20]
keyFrame5122.PositionMode = 'Path'
keyFrame5122.FocalPointMode = 'Path'
keyFrame5122.ClosedFocalPath = 0
keyFrame5122.ClosedPositionPath = 0

# ====================================================================
keyFrame5123 = CameraKeyFrame()
keyFrame5123.KeyTime = 0.3075
keyFrame5123.KeyValues = [0.0]
keyFrame5123.Position = [21.095868519408196, 20.0, 24.36452427823916]
keyFrame5123.FocalPoint = [20, 20, 20]
keyFrame5123.ViewUp = [0.48485015121131464, -0.866, -0.12173885275476011]
keyFrame5123.ViewAngle = 30.0
keyFrame5123.ParallelScale = 0.97681
keyFrame5123.PositionPathPoints = [21.095868519408196, 20.0, 24.36452427823916]
keyFrame5123.FocalPathPoints = [20, 20, 20]
keyFrame5123.PositionMode = 'Path'
keyFrame5123.FocalPointMode = 'Path'
keyFrame5123.ClosedFocalPath = 0
keyFrame5123.ClosedPositionPath = 0

# ====================================================================
keyFrame5124 = CameraKeyFrame()
keyFrame5124.KeyTime = 0.31
keyFrame5124.KeyValues = [0.0]
keyFrame5124.Position = [21.10459537040589, 20.0, 24.362323813601645]
keyFrame5124.FocalPoint = [20, 20, 20]
keyFrame5124.ViewUp = [0.4846057039439301, -0.866, -0.12270830902265374]
keyFrame5124.ViewAngle = 30.0
keyFrame5124.ParallelScale = 0.97681
keyFrame5124.PositionPathPoints = [21.10459537040589, 20.0, 24.362323813601645]
keyFrame5124.FocalPathPoints = [20, 20, 20]
keyFrame5124.PositionMode = 'Path'
keyFrame5124.FocalPointMode = 'Path'
keyFrame5124.ClosedFocalPath = 0
keyFrame5124.ClosedPositionPath = 0

# ====================================================================
keyFrame5125 = CameraKeyFrame()
keyFrame5125.KeyTime = 0.3125
keyFrame5125.KeyValues = [0.0]
keyFrame5125.Position = [21.113317803022934, 20.0, 24.36010589967178]
keyFrame5125.FocalPoint = [20, 20, 20]
keyFrame5125.ViewUp = [0.48435931825076456, -0.866, -0.12367727447344327]
keyFrame5125.ViewAngle = 30.0
keyFrame5125.ParallelScale = 0.97681
keyFrame5125.PositionPathPoints = [21.113317803022934, 20.0, 24.36010589967178]
keyFrame5125.FocalPathPoints = [20, 20, 20]
keyFrame5125.PositionMode = 'Path'
keyFrame5125.FocalPointMode = 'Path'
keyFrame5125.ClosedFocalPath = 0
keyFrame5125.ClosedPositionPath = 0

# ====================================================================
keyFrame5126 = CameraKeyFrame()
keyFrame5126.KeyTime = 0.315
keyFrame5126.KeyValues = [0.0]
keyFrame5126.Position = [21.122035782369668, 20.0, 24.357870545321482]
keyFrame5126.FocalPoint = [20, 20, 20]
keyFrame5126.ViewUp = [0.48411099511752476, -0.866, -0.12464574523047803]
keyFrame5126.ViewAngle = 30.0
keyFrame5126.ParallelScale = 0.97681
keyFrame5126.PositionPathPoints = [21.122035782369668, 20.0, 24.357870545321482]
keyFrame5126.FocalPathPoints = [20, 20, 20]
keyFrame5126.PositionMode = 'Path'
keyFrame5126.FocalPointMode = 'Path'
keyFrame5126.ClosedFocalPath = 0
keyFrame5126.ClosedPositionPath = 0

# ====================================================================
keyFrame5127 = CameraKeyFrame()
keyFrame5127.KeyTime = 0.3175
keyFrame5127.KeyValues = [0.0]
keyFrame5127.Position = [21.13074927357425, 20.0, 24.35561775949249]
keyFrame5127.FocalPoint = [20, 20, 20]
keyFrame5127.ViewUp = [0.4838607355377314, -0.866, -0.12561371741879876]
keyFrame5127.ViewAngle = 30.0
keyFrame5127.ParallelScale = 0.97681
keyFrame5127.PositionPathPoints = [21.13074927357425, 20.0, 24.35561775949249]
keyFrame5127.FocalPathPoints = [20, 20, 20]
keyFrame5127.PositionMode = 'Path'
keyFrame5127.FocalPointMode = 'Path'
keyFrame5127.ClosedFocalPath = 0
keyFrame5127.ClosedPositionPath = 0

# ====================================================================
keyFrame5128 = CameraKeyFrame()
keyFrame5128.KeyTime = 0.32
keyFrame5128.KeyValues = [0.0]
keyFrame5128.Position = [21.139458241782798, 20.0, 24.353347551196336]
keyFrame5128.FocalPoint = [20, 20, 20]
keyFrame5128.ViewUp = [0.4836085405127193, -0.866, -0.1265811871651376]
keyFrame5128.ViewAngle = 30.0
keyFrame5128.ParallelScale = 0.97681
keyFrame5128.PositionPathPoints = [21.139458241782798, 20.0, 24.353347551196336]
keyFrame5128.FocalPathPoints = [20, 20, 20]
keyFrame5128.PositionMode = 'Path'
keyFrame5128.FocalPointMode = 'Path'
keyFrame5128.ClosedFocalPath = 0
keyFrame5128.ClosedPositionPath = 0

# ====================================================================
keyFrame5129 = CameraKeyFrame()
keyFrame5129.KeyTime = 0.3225
keyFrame5129.KeyValues = [0.0]
keyFrame5129.Position = [21.148162652159552, 20.0, 24.351059929514314]
keyFrame5129.FocalPoint = [20, 20, 20]
keyFrame5129.ViewUp = [0.4833544110516373, -0.866, -0.12754815059791821]
keyFrame5129.ViewAngle = 30.0
keyFrame5129.ParallelScale = 0.97681
keyFrame5129.PositionPathPoints = [21.148162652159552, 20.0, 24.351059929514314]
keyFrame5129.FocalPathPoints = [20, 20, 20]
keyFrame5129.PositionMode = 'Path'
keyFrame5129.FocalPointMode = 'Path'
keyFrame5129.ClosedFocalPath = 0
keyFrame5129.ClosedPositionPath = 0

# ====================================================================
keyFrame5130 = CameraKeyFrame()
keyFrame5130.KeyTime = 0.325
keyFrame5130.KeyValues = [0.0]
keyFrame5130.Position = [21.156862469886995, 20.0, 24.348754903597474]
keyFrame5130.FocalPoint = [20, 20, 20]
keyFrame5130.ViewUp = [0.48309834817144853, -0.866, -0.12851460384725566]
keyFrame5130.ViewAngle = 30.0
keyFrame5130.ParallelScale = 0.97681
keyFrame5130.PositionPathPoints = [21.156862469886995, 20.0, 24.348754903597474]
keyFrame5130.FocalPathPoints = [20, 20, 20]
keyFrame5130.PositionMode = 'Path'
keyFrame5130.FocalPointMode = 'Path'
keyFrame5130.ClosedFocalPath = 0
keyFrame5130.ClosedPositionPath = 0

# ====================================================================
keyFrame5131 = CameraKeyFrame()
keyFrame5131.KeyTime = 0.3275
keyFrame5131.KeyValues = [0.0]
keyFrame5131.Position = [21.16555766016601, 20.0, 24.34643248266657]
keyFrame5131.FocalPoint = [20, 20, 20]
keyFrame5131.ViewUp = [0.48284035289693, -0.866, -0.12948054304495638]
keyFrame5131.ViewAngle = 30.0
keyFrame5131.ParallelScale = 0.97681
keyFrame5131.PositionPathPoints = [21.16555766016601, 20.0, 24.34643248266657]
keyFrame5131.FocalPathPoints = [20, 20, 20]
keyFrame5131.PositionMode = 'Path'
keyFrame5131.FocalPointMode = 'Path'
keyFrame5131.ClosedFocalPath = 0
keyFrame5131.ClosedPositionPath = 0

# ====================================================================
keyFrame5132 = CameraKeyFrame()
keyFrame5132.KeyTime = 0.33
keyFrame5132.KeyValues = [0.0]
keyFrame5132.Position = [21.174248188216, 20.0, 24.34409267601206]
keyFrame5132.FocalPoint = [20, 20, 20]
keyFrame5132.ViewUp = [0.4825804262606729, -0.866, -0.1304459643245183]
keyFrame5132.ViewAngle = 30.0
keyFrame5132.ParallelScale = 0.97681
keyFrame5132.PositionPathPoints = [21.174248188216, 20.0, 24.34409267601206]
keyFrame5132.FocalPathPoints = [20, 20, 20]
keyFrame5132.PositionMode = 'Path'
keyFrame5132.FocalPointMode = 'Path'
keyFrame5132.ClosedFocalPath = 0
keyFrame5132.ClosedPositionPath = 0

# ====================================================================
keyFrame5133 = CameraKeyFrame()
keyFrame5133.KeyTime = 0.3325
keyFrame5133.KeyValues = [0.0]
keyFrame5133.Position = [21.182934019275066, 20.0, 24.34173549299406]
keyFrame5133.FocalPoint = [20, 20, 20]
keyFrame5133.ViewUp = [0.4823185693030825, -0.866, -0.1314108638211308]
keyFrame5133.ViewAngle = 30.0
keyFrame5133.ParallelScale = 0.97681
keyFrame5133.PositionPathPoints = [21.182934019275066, 20.0, 24.34173549299406]
keyFrame5133.FocalPathPoints = [20, 20, 20]
keyFrame5133.PositionMode = 'Path'
keyFrame5133.FocalPointMode = 'Path'
keyFrame5133.ClosedFocalPath = 0
keyFrame5133.ClosedPositionPath = 0

# ====================================================================
keyFrame5134 = CameraKeyFrame()
keyFrame5134.KeyTime = 0.335
keyFrame5134.KeyValues = [0.0]
keyFrame5134.Position = [21.191615118600108, 20.0, 24.339360943042337]
keyFrame5134.FocalPoint = [20, 20, 20]
keyFrame5134.ViewUp = [0.4820547830723782, -0.866, -0.13237523767167467]
keyFrame5134.ViewAngle = 30.0
keyFrame5134.ParallelScale = 0.97681
keyFrame5134.PositionPathPoints = [21.191615118600108, 20.0, 24.339360943042337]
keyFrame5134.FocalPathPoints = [20, 20, 20]
keyFrame5134.PositionMode = 'Path'
keyFrame5134.FocalPointMode = 'Path'
keyFrame5134.ClosedFocalPath = 0
keyFrame5134.ClosedPositionPath = 0

# ====================================================================
keyFrame5135 = CameraKeyFrame()
keyFrame5135.KeyTime = 0.3375
keyFrame5135.KeyValues = [0.0]
keyFrame5135.Position = [21.200291451466992, 20.0, 24.33696903565625]
keyFrame5135.FocalPoint = [20, 20, 20]
keyFrame5135.ViewUp = [0.4817890686245934, -0.866, -0.13333908201472214]
keyFrame5135.ViewAngle = 30.0
keyFrame5135.ParallelScale = 0.97681
keyFrame5135.PositionPathPoints = [21.200291451466992, 20.0, 24.33696903565625]
keyFrame5135.FocalPathPoints = [20, 20, 20]
keyFrame5135.PositionMode = 'Path'
keyFrame5135.FocalPointMode = 'Path'
keyFrame5135.ClosedFocalPath = 0
keyFrame5135.ClosedPositionPath = 0

# ====================================================================
keyFrame5136 = CameraKeyFrame()
keyFrame5136.KeyTime = 0.34
keyFrame5136.KeyValues = [0.0]
keyFrame5136.Position = [21.208962983170686, 20.0, 24.334559780404767]
keyFrame5136.FocalPoint = [20, 20, 20]
keyFrame5136.ViewUp = [0.4815214270235757, -0.866, -0.1343023929905369]
keyFrame5136.ViewAngle = 30.0
keyFrame5136.ParallelScale = 0.97681
keyFrame5136.PositionPathPoints = [21.208962983170686, 20.0, 24.334559780404767]
keyFrame5136.FocalPathPoints = [20, 20, 20]
keyFrame5136.PositionMode = 'Path'
keyFrame5136.FocalPointMode = 'Path'
keyFrame5136.ClosedFocalPath = 0
keyFrame5136.ClosedPositionPath = 0

# ====================================================================
keyFrame5137 = CameraKeyFrame()
keyFrame5137.KeyTime = 0.3425
keyFrame5137.KeyValues = [0.0]
keyFrame5137.Position = [21.217629679025393, 20.0, 24.332133186926402]
keyFrame5137.FocalPoint = [20, 20, 20]
keyFrame5137.ViewUp = [0.4812518593409867, -0.866, -0.135265166741074]
keyFrame5137.ViewAngle = 30.0
keyFrame5137.ParallelScale = 0.97681
keyFrame5137.PositionPathPoints = [21.217629679025393, 20.0, 24.332133186926402]
keyFrame5137.FocalPathPoints = [20, 20, 20]
keyFrame5137.PositionMode = 'Path'
keyFrame5137.FocalPointMode = 'Path'
keyFrame5137.ClosedFocalPath = 0
keyFrame5137.ClosedPositionPath = 0

# ====================================================================
keyFrame5138 = CameraKeyFrame()
keyFrame5138.KeyTime = 0.345
keyFrame5138.KeyValues = [0.0]
keyFrame5138.Position = [21.226291504363417, 20.0, 24.32968926492375]
keyFrame5138.FocalPoint = [20, 20, 20]
keyFrame5138.ViewUp = [0.4809803666563021, -0.866, -0.13622739940998002]
keyFrame5138.ViewAngle = 30.0
keyFrame5138.ParallelScale = 0.97681
keyFrame5138.PositionPathPoints = [21.226291504363417, 20.0, 24.32968926492375]
keyFrame5138.FocalPathPoints = [20, 20, 20]
keyFrame5138.PositionMode = 'Path'
keyFrame5138.FocalPointMode = 'Path'
keyFrame5138.ClosedFocalPath = 0
keyFrame5138.ClosedPositionPath = 0

# ====================================================================
keyFrame5139 = CameraKeyFrame()
keyFrame5139.KeyTime = 0.3475
keyFrame5139.KeyValues = [0.0]
keyFrame5139.Position = [21.234948424532373, 20.0, 24.327228024151005]
keyFrame5139.FocalPoint = [20, 20, 20]
keyFrame5139.ViewUp = [0.48070695005681174, -0.866, -0.1371890871425929]
keyFrame5139.ViewAngle = 30.0
keyFrame5139.ParallelScale = 0.97681
keyFrame5139.PositionPathPoints = [21.234948424532373, 20.0, 24.327228024151005]
keyFrame5139.FocalPathPoints = [20, 20, 20]
keyFrame5139.PositionMode = 'Path'
keyFrame5139.FocalPointMode = 'Path'
keyFrame5139.ClosedFocalPath = 0
keyFrame5139.ClosedPositionPath = 0

# ====================================================================
keyFrame5140 = CameraKeyFrame()
keyFrame5140.KeyTime = 0.35
keyFrame5140.KeyValues = [0.0]
keyFrame5140.Position = [21.243600404903802, 20.0, 24.324749474449938]
keyFrame5140.FocalPoint = [20, 20, 20]
keyFrame5140.ViewUp = [0.4804316106376196, -0.866, -0.1381502260859421]
keyFrame5140.ViewAngle = 30.0
keyFrame5140.ParallelScale = 0.97681
keyFrame5140.PositionPathPoints = [21.243600404903802, 20.0, 24.324749474449938]
keyFrame5140.FocalPathPoints = [20, 20, 20]
keyFrame5140.PositionMode = 'Path'
keyFrame5140.FocalPointMode = 'Path'
keyFrame5140.ClosedFocalPath = 0
keyFrame5140.ClosedPositionPath = 0

# ====================================================================
keyFrame5141 = CameraKeyFrame()
keyFrame5141.KeyTime = 0.3525
keyFrame5141.KeyValues = [0.0]
keyFrame5141.Position = [21.252247410869547, 20.0, 24.32225362573391]
keyFrame5141.FocalPoint = [20, 20, 20]
keyFrame5141.ViewUp = [0.4801543496943449, -0.866, -0.13911081158284416]
keyFrame5141.ViewAngle = 30.0
keyFrame5141.ParallelScale = 0.97681
keyFrame5141.PositionPathPoints = [21.252247410869547, 20.0, 24.32225362573391]
keyFrame5141.FocalPathPoints = [20, 20, 20]
keyFrame5141.PositionMode = 'Path'
keyFrame5141.FocalPointMode = 'Path'
keyFrame5141.ClosedFocalPath = 0
keyFrame5141.ClosedPositionPath = 0

# ====================================================================
keyFrame5142 = CameraKeyFrame()
keyFrame5142.KeyTime = 0.355
keyFrame5142.KeyValues = [0.0]
keyFrame5142.Position = [21.260889407841383, 20.0, 24.31974048798555]
keyFrame5142.FocalPoint = [20, 20, 20]
keyFrame5142.ViewUp = [0.47987516790551815, -0.866, -0.14007084159123967]
keyFrame5142.ViewAngle = 30.0
keyFrame5142.ParallelScale = 0.97681
keyFrame5142.PositionPathPoints = [21.260889407841383, 20.0, 24.31974048798555]
keyFrame5142.FocalPathPoints = [20, 20, 20]
keyFrame5142.PositionMode = 'Path'
keyFrame5142.FocalPointMode = 'Path'
keyFrame5142.ClosedFocalPath = 0
keyFrame5142.ClosedPositionPath = 0

# ====================================================================
keyFrame5143 = CameraKeyFrame()
keyFrame5143.KeyTime = 0.3575
keyFrame5143.KeyValues = [0.0]
keyFrame5143.Position = [21.26952636125112, 20.0, 24.317210071256714]
keyFrame5143.FocalPoint = [20, 20, 20]
keyFrame5143.ViewUp = [0.4795940666187654, -0.866, -0.14103031130518823]
keyFrame5143.ViewAngle = 30.0
keyFrame5143.ParallelScale = 0.97681
keyFrame5143.PositionPathPoints = [21.26952636125112, 20.0, 24.317210071256714]
keyFrame5143.FocalPathPoints = [20, 20, 20]
keyFrame5143.PositionMode = 'Path'
keyFrame5143.FocalPointMode = 'Path'
keyFrame5143.ClosedFocalPath = 0
keyFrame5143.ClosedPositionPath = 0

# ====================================================================
keyFrame5144 = CameraKeyFrame()
keyFrame5144.KeyTime = 0.36
keyFrame5144.KeyValues = [0.0]
keyFrame5144.Position = [21.278158236550777, 20.0, 24.314662385668484]
keyFrame5144.FocalPoint = [20, 20, 20]
keyFrame5144.ViewUp = [0.47931104695751453, -0.866, -0.14198921689074828]
keyFrame5144.ViewAngle = 30.0
keyFrame5144.ParallelScale = 0.97681
keyFrame5144.PositionPathPoints = [21.278158236550777, 20.0, 24.314662385668484]
keyFrame5144.FocalPathPoints = [20, 20, 20]
keyFrame5144.PositionMode = 'Path'
keyFrame5144.FocalPointMode = 'Path'
keyFrame5144.ClosedFocalPath = 0
keyFrame5144.ClosedPositionPath = 0

# ====================================================================
keyFrame5145 = CameraKeyFrame()
keyFrame5145.KeyTime = 0.3625
keyFrame5145.KeyValues = [0.0]
keyFrame5145.Position = [21.28678499921269, 20.0, 24.312097441411108]
keyFrame5145.FocalPoint = [20, 20, 20]
keyFrame5145.ViewUp = [0.4790261100530001, -0.866, -0.1429475545157012]
keyFrame5145.ViewAngle = 30.0
keyFrame5145.ParallelScale = 0.97681
keyFrame5145.PositionPathPoints = [21.28678499921269, 20.0, 24.312097441411108]
keyFrame5145.FocalPathPoints = [20, 20, 20]
keyFrame5145.PositionMode = 'Path'
keyFrame5145.FocalPointMode = 'Path'
keyFrame5145.ClosedFocalPath = 0
keyFrame5145.ClosedPositionPath = 0

# ====================================================================
keyFrame5146 = CameraKeyFrame()
keyFrame5146.KeyTime = 0.365
keyFrame5146.KeyValues = [0.0]
keyFrame5146.Position = [21.295406614729682, 20.0, 24.309515248743974]
keyFrame5146.FocalPoint = [20, 20, 20]
keyFrame5146.ViewUp = [0.4787392570442594, -0.866, -0.14390532034956732]
keyFrame5146.ViewAngle = 30.0
keyFrame5146.ParallelScale = 0.97681
keyFrame5146.PositionPathPoints = [21.295406614729682, 20.0, 24.309515248743974]
keyFrame5146.FocalPathPoints = [20, 20, 20]
keyFrame5146.PositionMode = 'Path'
keyFrame5146.FocalPointMode = 'Path'
keyFrame5146.ClosedFocalPath = 0
keyFrame5146.ClosedPositionPath = 0

# ====================================================================
keyFrame5147 = CameraKeyFrame()
keyFrame5147.KeyTime = 0.3675
keyFrame5147.KeyValues = [0.0]
keyFrame5147.Position = [21.304023048615186, 20.0, 24.306915817995577]
keyFrame5147.FocalPoint = [20, 20, 20]
keyFrame5147.ViewUp = [0.47845048907812876, -0.866, -0.14486251056362115]
keyFrame5147.ViewAngle = 30.0
keyFrame5147.ParallelScale = 0.97681
keyFrame5147.PositionPathPoints = [21.304023048615186, 20.0, 24.306915817995577]
keyFrame5147.FocalPathPoints = [20, 20, 20]
keyFrame5147.PositionMode = 'Path'
keyFrame5147.FocalPointMode = 'Path'
keyFrame5147.ClosedFocalPath = 0
keyFrame5147.ClosedPositionPath = 0

# ====================================================================
keyFrame5148 = CameraKeyFrame()
keyFrame5148.KeyTime = 0.37
keyFrame5148.KeyValues = [0.0]
keyFrame5148.Position = [21.31263426640339, 20.0, 24.304299159563485]
keyFrame5148.FocalPoint = [20, 20, 20]
keyFrame5148.ViewUp = [0.47815980730923974, -0.866, -0.14581912133090738]
keyFrame5148.ViewAngle = 30.0
keyFrame5148.ParallelScale = 0.97681
keyFrame5148.PositionPathPoints = [21.31263426640339, 20.0, 24.304299159563485]
keyFrame5148.FocalPathPoints = [20, 20, 20]
keyFrame5148.PositionMode = 'Path'
keyFrame5148.FocalPointMode = 'Path'
keyFrame5148.ClosedFocalPath = 0
keyFrame5148.ClosedPositionPath = 0

# ====================================================================
keyFrame5149 = CameraKeyFrame()
keyFrame5149.KeyTime = 0.3725
keyFrame5149.KeyValues = [0.0]
keyFrame5149.Position = [21.321240233649366, 20.0, 24.301665283914303]
keyFrame5149.FocalPoint = [20, 20, 20]
keyFrame5149.ViewUp = [0.47786721290001555, -0.866, -0.14677514882625636]
keyFrame5149.ViewAngle = 30.0
keyFrame5149.ParallelScale = 0.97681
keyFrame5149.PositionPathPoints = [21.321240233649366, 20.0, 24.301665283914303]
keyFrame5149.FocalPathPoints = [20, 20, 20]
keyFrame5149.PositionMode = 'Path'
keyFrame5149.FocalPointMode = 'Path'
keyFrame5149.ClosedFocalPath = 0
keyFrame5149.ClosedPositionPath = 0

# ====================================================================
keyFrame5150 = CameraKeyFrame()
keyFrame5150.KeyTime = 0.375
keyFrame5150.KeyValues = [0.0]
keyFrame5150.Position = [21.329840915929235, 20.0, 24.299014201583642]
keyFrame5150.FocalPoint = [20, 20, 20]
keyFrame5150.ViewUp = [0.4775727070206671, -0.866, -0.1477305892262998]
keyFrame5150.ViewAngle = 30.0
keyFrame5150.ParallelScale = 0.97681
keyFrame5150.PositionPathPoints = [21.329840915929235, 20.0, 24.299014201583642]
keyFrame5150.FocalPathPoints = [20, 20, 20]
keyFrame5150.PositionMode = 'Path'
keyFrame5150.FocalPointMode = 'Path'
keyFrame5150.ClosedFocalPath = 0
keyFrame5150.ClosedPositionPath = 0

# ====================================================================
keyFrame5151 = CameraKeyFrame()
keyFrame5151.KeyTime = 0.3775
keyFrame5151.KeyValues = [0.0]
keyFrame5151.Position = [21.33843627884028, 20.0, 24.296345923176077]
keyFrame5151.FocalPoint = [20, 20, 20]
keyFrame5151.ViewUp = [0.47727629084918954, -0.866, -0.14868543870948647]
keyFrame5151.ViewAngle = 30.0
keyFrame5151.ParallelScale = 0.97681
keyFrame5151.PositionPathPoints = [21.33843627884028, 20.0, 24.296345923176077]
keyFrame5151.FocalPathPoints = [20, 20, 20]
keyFrame5151.PositionMode = 'Path'
keyFrame5151.FocalPointMode = 'Path'
keyFrame5151.ClosedFocalPath = 0
keyFrame5151.ClosedPositionPath = 0

# ====================================================================
keyFrame5152 = CameraKeyFrame()
keyFrame5152.KeyTime = 0.38
keyFrame5152.KeyValues = [0.0]
keyFrame5152.Position = [21.3470262880011, 20.0, 24.29366045936512]
keyFrame5152.FocalPoint = [20, 20, 20]
keyFrame5152.ViewUp = [0.4769779655713582, -0.866, -0.14963969345609773]
keyFrame5152.ViewAngle = 30.0
keyFrame5152.ParallelScale = 0.97681
keyFrame5152.PositionPathPoints = [21.3470262880011, 20.0, 24.29366045936512]
keyFrame5152.FocalPathPoints = [20, 20, 20]
keyFrame5152.PositionMode = 'Path'
keyFrame5152.FocalPointMode = 'Path'
keyFrame5152.ClosedFocalPath = 0
keyFrame5152.ClosedPositionPath = 0

# ====================================================================
keyFrame5153 = CameraKeyFrame()
keyFrame5153.KeyTime = 0.3825
keyFrame5153.KeyValues = [0.0]
keyFrame5153.Position = [21.355610909051745, 20.0, 24.290957820893176]
keyFrame5153.FocalPoint = [20, 20, 20]
keyFrame5153.ViewUp = [0.4766777323807249, -0.866, -0.15059334964826332]
keyFrame5153.ViewAngle = 30.0
keyFrame5153.ParallelScale = 0.97681
keyFrame5153.PositionPathPoints = [21.355610909051745, 20.0, 24.290957820893176]
keyFrame5153.FocalPathPoints = [20, 20, 20]
keyFrame5153.PositionMode = 'Path'
keyFrame5153.FocalPointMode = 'Path'
keyFrame5153.ClosedFocalPath = 0
keyFrame5153.ClosedPositionPath = 0

# ====================================================================
keyFrame5154 = CameraKeyFrame()
keyFrame5154.KeyTime = 0.385
keyFrame5154.KeyValues = [0.0]
keyFrame5154.Position = [21.364190107653855, 20.0, 24.288238018571512]
keyFrame5154.FocalPoint = [20, 20, 20]
keyFrame5154.ViewUp = [0.47637559247861455, -0.866, -0.1515464034699769]
keyFrame5154.ViewAngle = 30.0
keyFrame5154.ParallelScale = 0.97681
keyFrame5154.PositionPathPoints = [21.364190107653855, 20.0, 24.288238018571512]
keyFrame5154.FocalPathPoints = [20, 20, 20]
keyFrame5154.PositionMode = 'Path'
keyFrame5154.FocalPointMode = 'Path'
keyFrame5154.ClosedFocalPath = 0
keyFrame5154.ClosedPositionPath = 0

# ====================================================================
keyFrame5155 = CameraKeyFrame()
keyFrame5155.KeyTime = 0.3875
keyFrame5155.KeyValues = [0.0]
keyFrame5155.Position = [21.37276384949081, 20.0, 24.28550106328022]
keyFrame5155.FocalPoint = [20, 20, 20]
keyFrame5155.ViewUp = [0.4760715470741209, -0.866, -0.15249885110711178]
keyFrame5155.ViewAngle = 30.0
keyFrame5155.ParallelScale = 0.97681
keyFrame5155.PositionPathPoints = [21.37276384949081, 20.0, 24.28550106328022]
keyFrame5155.FocalPathPoints = [20, 20, 20]
keyFrame5155.PositionMode = 'Path'
keyFrame5155.FocalPointMode = 'Path'
keyFrame5155.ClosedFocalPath = 0
keyFrame5155.ClosedPositionPath = 0

# ====================================================================
keyFrame5156 = CameraKeyFrame()
keyFrame5156.KeyTime = 0.39
keyFrame5156.KeyValues = [0.0]
keyFrame5156.Position = [21.381332100267844, 20.0, 24.282746965968173]
keyFrame5156.FocalPoint = [20, 20, 20]
keyFrame5156.ViewUp = [0.4757655973841033, -0.866, -0.1534506887474366]
keyFrame5156.ViewAngle = 30.0
keyFrame5156.ParallelScale = 0.97681
keyFrame5156.PositionPathPoints = [21.381332100267844, 20.0, 24.282746965968173]
keyFrame5156.FocalPathPoints = [20, 20, 20]
keyFrame5156.PositionMode = 'Path'
keyFrame5156.FocalPointMode = 'Path'
keyFrame5156.ClosedFocalPath = 0
keyFrame5156.ClosedPositionPath = 0

# ====================================================================
keyFrame5157 = CameraKeyFrame()
keyFrame5157.KeyTime = 0.3925
keyFrame5157.KeyValues = [0.0]
keyFrame5157.Position = [21.389894825712226, 20.0, 24.279975737653004]
keyFrame5157.FocalPoint = [20, 20, 20]
keyFrame5157.ViewUp = [0.4754577446331824, -0.866, -0.15440191258063085]
keyFrame5157.ViewAngle = 30.0
keyFrame5157.ParallelScale = 0.97681
keyFrame5157.PositionPathPoints = [21.389894825712226, 20.0, 24.279975737653004]
keyFrame5157.FocalPathPoints = [20, 20, 20]
keyFrame5157.PositionMode = 'Path'
keyFrame5157.FocalPointMode = 'Path'
keyFrame5157.ClosedFocalPath = 0
keyFrame5157.ClosedPositionPath = 0

# ====================================================================
keyFrame5158 = CameraKeyFrame()
keyFrame5158.KeyTime = 0.395
keyFrame5158.KeyValues = [0.0]
keyFrame5158.Position = [21.398451991573346, 20.0, 24.277187389421048]
keyFrame5158.FocalPoint = [20, 20, 20]
keyFrame5158.ViewUp = [0.475147990053737, -0.866, -0.1553525187983007]
keyFrame5158.ViewAngle = 30.0
keyFrame5158.ParallelScale = 0.97681
keyFrame5158.PositionPathPoints = [21.398451991573346, 20.0, 24.277187389421048]
keyFrame5158.FocalPathPoints = [20, 20, 20]
keyFrame5158.PositionMode = 'Path'
keyFrame5158.FocalPointMode = 'Path'
keyFrame5158.ClosedFocalPath = 0
keyFrame5158.ClosedPositionPath = 0

# ====================================================================
keyFrame5159 = CameraKeyFrame()
keyFrame5159.KeyTime = 0.3975
keyFrame5159.KeyValues = [0.0]
keyFrame5159.Position = [21.407003563622908, 20.0, 24.274381932427328]
keyFrame5159.FocalPoint = [20, 20, 20]
keyFrame5159.ViewUp = [0.4748363348858998, -0.866, -0.15630250359399447]
keyFrame5159.ViewAngle = 30.0
keyFrame5159.ParallelScale = 0.97681
keyFrame5159.PositionPathPoints = [21.407003563622908, 20.0, 24.274381932427328]
keyFrame5159.FocalPathPoints = [20, 20, 20]
keyFrame5159.PositionMode = 'Path'
keyFrame5159.FocalPointMode = 'Path'
keyFrame5159.ClosedFocalPath = 0
keyFrame5159.ClosedPositionPath = 0

# ====================================================================
keyFrame5160 = CameraKeyFrame()
keyFrame5160.KeyTime = 0.4
keyFrame5160.KeyValues = [0.0]
keyFrame5160.Position = [21.415549507655022, 20.0, 24.271559377895493]
keyFrame5160.FocalPoint = [20, 20, 20]
keyFrame5160.ViewUp = [0.47452278037755413, -0.866, -0.15725186316321843]
keyFrame5160.ViewAngle = 30.0
keyFrame5160.ParallelScale = 0.97681
keyFrame5160.PositionPathPoints = [21.415549507655022, 20.0, 24.271559377895493]
keyFrame5160.FocalPathPoints = [20, 20, 20]
keyFrame5160.PositionMode = 'Path'
keyFrame5160.FocalPointMode = 'Path'
keyFrame5160.ClosedFocalPath = 0
keyFrame5160.ClosedPositionPath = 0

# ====================================================================
keyFrame5161 = CameraKeyFrame()
keyFrame5161.KeyTime = 0.4025
keyFrame5161.KeyValues = [0.0]
keyFrame5161.Position = [21.424089789486388, 20.0, 24.268719737117795]
keyFrame5161.FocalPoint = [20, 20, 20]
keyFrame5161.ViewUp = [0.47420732778432967, -0.866, -0.15820059370345244]
keyFrame5161.ViewAngle = 30.0
keyFrame5161.ParallelScale = 0.97681
keyFrame5161.PositionPathPoints = [21.424089789486388, 20.0, 24.268719737117795]
keyFrame5161.FocalPathPoints = [20, 20, 20]
keyFrame5161.PositionMode = 'Path'
keyFrame5161.FocalPointMode = 'Path'
keyFrame5161.ClosedFocalPath = 0
keyFrame5161.ClosedPositionPath = 0

# ====================================================================
keyFrame5162 = CameraKeyFrame()
keyFrame5162.KeyTime = 0.405
keyFrame5162.KeyValues = [0.0]
keyFrame5162.Position = [21.432624374956387, 20.0, 24.26586302145504]
keyFrame5162.FocalPoint = [20, 20, 20]
keyFrame5162.ViewUp = [0.4738899783695991, -0.866, -0.15914869141416546]
keyFrame5162.ViewAngle = 30.0
keyFrame5162.ParallelScale = 0.97681
keyFrame5162.PositionPathPoints = [21.432624374956387, 20.0, 24.26586302145504]
keyFrame5162.FocalPathPoints = [20, 20, 20]
keyFrame5162.PositionMode = 'Path'
keyFrame5162.FocalPointMode = 'Path'
keyFrame5162.ClosedFocalPath = 0
keyFrame5162.ClosedPositionPath = 0

# ====================================================================
keyFrame5163 = CameraKeyFrame()
keyFrame5163.KeyTime = 0.4075
keyFrame5163.KeyValues = [0.0]
keyFrame5163.Position = [21.441153229927266, 20.0, 24.262989242336563]
keyFrame5163.FocalPoint = [20, 20, 20]
keyFrame5163.ViewUp = [0.47357073340447436, -0.866, -0.1600961524968314]
keyFrame5163.ViewAngle = 30.0
keyFrame5163.ParallelScale = 0.97681
keyFrame5163.PositionPathPoints = [21.441153229927266, 20.0, 24.262989242336563]
keyFrame5163.FocalPathPoints = [20, 20, 20]
keyFrame5163.PositionMode = 'Path'
keyFrame5163.FocalPointMode = 'Path'
keyFrame5163.ClosedFocalPath = 0
keyFrame5163.ClosedPositionPath = 0

# ====================================================================
keyFrame5164 = CameraKeyFrame()
keyFrame5164.KeyTime = 0.41
keyFrame5164.KeyValues = [0.0]
keyFrame5164.Position = [21.449676320284244, 20.0, 24.260098411260174]
keyFrame5164.FocalPoint = [20, 20, 20]
keyFrame5164.ViewUp = [0.473249594167308, -0.866, -0.16104297315655855]
keyFrame5164.ViewAngle = 30.0
keyFrame5164.ParallelScale = 0.97681
keyFrame5164.PositionPathPoints = [21.449676320284244, 20.0, 24.260098411260174]
keyFrame5164.FocalPathPoints = [20, 20, 20]
keyFrame5164.PositionMode = 'Path'
keyFrame5164.FocalPointMode = 'Path'
keyFrame5164.ClosedFocalPath = 0
keyFrame5164.ClosedPositionPath = 0

# ====================================================================
keyFrame5165 = CameraKeyFrame()
keyFrame5165.KeyTime = 0.4125
keyFrame5165.KeyValues = [0.0]
keyFrame5165.Position = [21.45819361193567, 20.0, 24.25719053979213]
keyFrame5165.FocalPoint = [20, 20, 20]
keyFrame5165.ViewUp = [0.4729265619257819, -0.866, -0.16198914966053699]
keyFrame5165.ViewAngle = 30.0
keyFrame5165.ParallelScale = 0.97681
keyFrame5165.PositionPathPoints = [21.45819361193567, 20.0, 24.25719053979213]
keyFrame5165.FocalPathPoints = [20, 20, 20]
keyFrame5165.PositionMode = 'Path'
keyFrame5165.FocalPointMode = 'Path'
keyFrame5165.ClosedFocalPath = 0
keyFrame5165.ClosedPositionPath = 0

# ====================================================================
keyFrame5166 = CameraKeyFrame()
keyFrame5166.KeyTime = 0.415
keyFrame5166.KeyValues = [0.0]
keyFrame5166.Position = [21.46670507081315, 20.0, 24.25426563956708]
keyFrame5166.FocalPoint = [20, 20, 20]
keyFrame5166.ViewUp = [0.47260163796275206, -0.866, -0.16293467825371252]
keyFrame5166.ViewAngle = 30.0
keyFrame5166.ParallelScale = 0.97681
keyFrame5166.PositionPathPoints = [21.46670507081315, 20.0, 24.25426563956708]
keyFrame5166.FocalPathPoints = [20, 20, 20]
keyFrame5166.PositionMode = 'Path'
keyFrame5166.FocalPointMode = 'Path'
keyFrame5166.ClosedFocalPath = 0
keyFrame5166.ClosedPositionPath = 0

# ====================================================================
keyFrame5167 = CameraKeyFrame()
keyFrame5167.KeyTime = 0.4175
keyFrame5167.KeyValues = [0.0]
keyFrame5167.Position = [21.47521066287169, 20.0, 24.251323722288046]
keyFrame5167.FocalPoint = [20, 20, 20]
keyFrame5167.ViewUp = [0.4722748235777172, -0.866, -0.1638795551539971]
keyFrame5167.ViewAngle = 30.0
keyFrame5167.ParallelScale = 0.97681
keyFrame5167.PositionPathPoints = [21.47521066287169, 20.0, 24.251323722288046]
keyFrame5167.FocalPathPoints = [20, 20, 20]
keyFrame5167.PositionMode = 'Path'
keyFrame5167.FocalPointMode = 'Path'
keyFrame5167.ClosedFocalPath = 0
keyFrame5167.ClosedPositionPath = 0

# ====================================================================
keyFrame5168 = CameraKeyFrame()
keyFrame5168.KeyTime = 0.42
keyFrame5168.KeyValues = [0.0]
keyFrame5168.Position = [21.483710354089837, 20.0, 24.24836479972636]
keyFrame5168.FocalPoint = [20, 20, 20]
keyFrame5168.ViewUp = [0.47194612007780345, -0.866, -0.1648237765816904]
keyFrame5168.ViewAngle = 30.0
keyFrame5168.ParallelScale = 0.97681
keyFrame5168.PositionPathPoints = [21.483710354089837, 20.0, 24.24836479972636]
keyFrame5168.FocalPathPoints = [20, 20, 20]
keyFrame5168.PositionMode = 'Path'
keyFrame5168.FocalPointMode = 'Path'
keyFrame5168.ClosedFocalPath = 0
keyFrame5168.ClosedPositionPath = 0

# ====================================================================
keyFrame5169 = CameraKeyFrame()
keyFrame5169.KeyTime = 0.4225
keyFrame5169.KeyValues = [0.0]
keyFrame5169.Position = [21.492204110469824, 20.0, 24.24538888372164]
keyFrame5169.FocalPoint = [20, 20, 20]
keyFrame5169.ViewUp = [0.4716155287777587, -0.866, -0.16576733875949984]
keyFrame5169.ViewAngle = 30.0
keyFrame5169.ParallelScale = 0.97681
keyFrame5169.PositionPathPoints = [21.492204110469824, 20.0, 24.24538888372164]
keyFrame5169.FocalPathPoints = [20, 20, 20]
keyFrame5169.PositionMode = 'Path'
keyFrame5169.FocalPointMode = 'Path'
keyFrame5169.ClosedFocalPath = 0
keyFrame5169.ClosedPositionPath = 0

# ====================================================================
keyFrame5170 = CameraKeyFrame()
keyFrame5170.KeyTime = 0.425
keyFrame5170.KeyValues = [0.0]
keyFrame5170.Position = [21.500691898037687, 20.0, 24.242395986181734]
keyFrame5170.FocalPoint = [20, 20, 20]
keyFrame5170.ViewUp = [0.4712830509999477, -0.866, -0.166710237912561]
keyFrame5170.ViewAngle = 30.0
keyFrame5170.ParallelScale = 0.97681
keyFrame5170.PositionPathPoints = [21.500691898037687, 20.0, 24.242395986181734]
keyFrame5170.FocalPathPoints = [20, 20, 20]
keyFrame5170.PositionMode = 'Path'
keyFrame5170.FocalPointMode = 'Path'
keyFrame5170.ClosedFocalPath = 0
keyFrame5170.ClosedPositionPath = 0

# ====================================================================
keyFrame5171 = CameraKeyFrame()
keyFrame5171.KeyTime = 0.4275
keyFrame5171.KeyValues = [0.0]
keyFrame5171.Position = [21.50917368284342, 20.0, 24.239386119082695]
keyFrame5171.FocalPoint = [20, 20, 20]
keyFrame5171.ViewUp = [0.4709486880743469, -0.866, -0.1676524702684577]
keyFrame5171.ViewAngle = 30.0
keyFrame5171.ParallelScale = 0.97681
keyFrame5171.PositionPathPoints = [21.50917368284342, 20.0, 24.239386119082695]
keyFrame5171.FocalPathPoints = [20, 20, 20]
keyFrame5171.PositionMode = 'Path'
keyFrame5171.FocalPointMode = 'Path'
keyFrame5171.ClosedFocalPath = 0
keyFrame5171.ClosedPositionPath = 0

# ====================================================================
keyFrame5172 = CameraKeyFrame()
keyFrame5172.KeyTime = 0.43
keyFrame5172.KeyValues = [0.0]
keyFrame5172.Position = [21.517649430961125, 20.0, 24.236359294468727]
keyFrame5172.FocalPoint = [20, 20, 20]
keyFrame5172.ViewUp = [0.4706124413385394, -0.866, -0.16859403205724222]
keyFrame5172.ViewAngle = 30.0
keyFrame5172.ParallelScale = 0.97681
keyFrame5172.PositionPathPoints = [21.517649430961125, 20.0, 24.236359294468727]
keyFrame5172.FocalPathPoints = [20, 20, 20]
keyFrame5172.PositionMode = 'Path'
keyFrame5172.FocalPointMode = 'Path'
keyFrame5172.ClosedFocalPath = 0
keyFrame5172.ClosedPositionPath = 0

# ====================================================================
keyFrame5173 = CameraKeyFrame()
keyFrame5173.KeyTime = 0.4325
keyFrame5173.KeyValues = [0.0]
keyFrame5173.Position = [21.526119108489116, 20.0, 24.233315524452145]
keyFrame5173.FocalPoint = [20, 20, 20]
keyFrame5173.ViewUp = [0.4702743121377096, -0.866, -0.16953491951145558]
keyFrame5173.ViewAngle = 30.0
keyFrame5173.ParallelScale = 0.97681
keyFrame5173.PositionPathPoints = [21.526119108489116, 20.0, 24.233315524452145]
keyFrame5173.FocalPathPoints = [20, 20, 20]
keyFrame5173.PositionMode = 'Path'
keyFrame5173.FocalPointMode = 'Path'
keyFrame5173.ClosedFocalPath = 0
keyFrame5173.ClosedPositionPath = 0

# ====================================================================
keyFrame5174 = CameraKeyFrame()
keyFrame5174.KeyTime = 0.435
keyFrame5174.KeyValues = [0.0]
keyFrame5174.Position = [21.53458268155009, 20.0, 24.230254821213336]
keyFrame5174.FocalPoint = [20, 20, 20]
keyFrame5174.ViewUp = [0.4699343018246381, -0.866, -0.17047512886614774]
keyFrame5174.ViewAngle = 30.0
keyFrame5174.ParallelScale = 0.97681
keyFrame5174.PositionPathPoints = [21.53458268155009, 20.0, 24.230254821213336]
keyFrame5174.FocalPathPoints = [20, 20, 20]
keyFrame5174.PositionMode = 'Path'
keyFrame5174.FocalPointMode = 'Path'
keyFrame5174.ClosedFocalPath = 0
keyFrame5174.ClosedPositionPath = 0

# ====================================================================
keyFrame5175 = CameraKeyFrame()
keyFrame5175.KeyTime = 0.4375
keyFrame5175.KeyValues = [0.0]
keyFrame5175.Position = [21.543040116291248, 20.0, 24.22717719700071]
keyFrame5175.FocalPoint = [20, 20, 20]
keyFrame5175.ViewUp = [0.4695924117596968, -0.866, -0.17141465635889766]
keyFrame5175.ViewAngle = 30.0
keyFrame5175.ParallelScale = 0.97681
keyFrame5175.PositionPathPoints = [21.543040116291248, 20.0, 24.22717719700071]
keyFrame5175.FocalPathPoints = [20, 20, 20]
keyFrame5175.PositionMode = 'Path'
keyFrame5175.FocalPointMode = 'Path'
keyFrame5175.ClosedFocalPath = 0
keyFrame5175.ClosedPositionPath = 0

# ====================================================================
keyFrame5176 = CameraKeyFrame()
keyFrame5176.KeyTime = 0.44
keyFrame5176.KeyValues = [0.0]
keyFrame5176.Position = [21.55149137888444, 20.0, 24.22408266413066]
keyFrame5176.FocalPoint = [20, 20, 20]
keyFrame5176.ViewUp = [0.4692486433108434, -0.866, -0.1723534982298337]
keyFrame5176.ViewAngle = 30.0
keyFrame5176.ParallelScale = 0.97681
keyFrame5176.PositionPathPoints = [21.55149137888444, 20.0, 24.22408266413066]
keyFrame5176.FocalPathPoints = [20, 20, 20]
keyFrame5176.PositionMode = 'Path'
keyFrame5176.FocalPointMode = 'Path'
keyFrame5176.ClosedFocalPath = 0
keyFrame5176.ClosedPositionPath = 0

# ====================================================================
keyFrame5177 = CameraKeyFrame()
keyFrame5177.KeyTime = 0.4425
keyFrame5177.KeyValues = [0.0]
keyFrame5177.Position = [21.5599364355263, 20.0, 24.220971234987516]
keyFrame5177.FocalPoint = [20, 20, 20]
keyFrame5177.ViewUp = [0.4689029978536167, -0.866, -0.17329165072165384]
keyFrame5177.ViewAngle = 30.0
keyFrame5177.ParallelScale = 0.97681
keyFrame5177.PositionPathPoints = [21.5599364355263, 20.0, 24.220971234987516]
keyFrame5177.FocalPathPoints = [20, 20, 20]
keyFrame5177.PositionMode = 'Path'
keyFrame5177.FocalPointMode = 'Path'
keyFrame5177.ClosedFocalPath = 0
keyFrame5177.ClosedPositionPath = 0

# ====================================================================
keyFrame5178 = CameraKeyFrame()
keyFrame5178.KeyTime = 0.445
keyFrame5178.KeyValues = [0.0]
keyFrame5178.Position = [21.568375252438386, 20.0, 24.217842922023515]
keyFrame5178.FocalPoint = [20, 20, 20]
keyFrame5178.ViewUp = [0.468555476771131, -0.866, -0.17422911007964564]
keyFrame5178.ViewAngle = 30.0
keyFrame5178.ParallelScale = 0.97681
keyFrame5178.PositionPathPoints = [21.568375252438386, 20.0, 24.217842922023515]
keyFrame5178.FocalPathPoints = [20, 20, 20]
keyFrame5178.PositionMode = 'Path'
keyFrame5178.FocalPointMode = 'Path'
keyFrame5178.ClosedFocalPath = 0
keyFrame5178.ClosedPositionPath = 0

# ====================================================================
keyFrame5179 = CameraKeyFrame()
keyFrame5179.KeyTime = 0.4475
keyFrame5179.KeyValues = [0.0]
keyFrame5179.Position = [21.57680779586732, 20.0, 24.21469773775873]
keyFrame5179.FocalPoint = [20, 20, 20]
keyFrame5179.ViewUp = [0.4682060814540713, -0.866, -0.17516587255170676]
keyFrame5179.ViewAngle = 30.0
keyFrame5179.ParallelScale = 0.97681
keyFrame5179.PositionPathPoints = [21.57680779586732, 20.0, 24.21469773775873]
keyFrame5179.FocalPathPoints = [20, 20, 20]
keyFrame5179.PositionMode = 'Path'
keyFrame5179.FocalPointMode = 'Path'
keyFrame5179.ClosedFocalPath = 0
keyFrame5179.ClosedPositionPath = 0

# ====================================================================
keyFrame5180 = CameraKeyFrame()
keyFrame5180.KeyTime = 0.45
keyFrame5180.KeyValues = [0.0]
keyFrame5180.Position = [21.585234032084916, 20.0, 24.21153569478105]
keyFrame5180.FocalPoint = [20, 20, 20]
keyFrame5180.ViewUp = [0.46785481330068784, -0.866, -0.17610193438836494]
keyFrame5180.ViewAngle = 30.0
keyFrame5180.ParallelScale = 0.97681
keyFrame5180.PositionPathPoints = [21.585234032084916, 20.0, 24.21153569478105]
keyFrame5180.FocalPathPoints = [20, 20, 20]
keyFrame5180.PositionMode = 'Path'
keyFrame5180.FocalPointMode = 'Path'
keyFrame5180.ClosedFocalPath = 0
keyFrame5180.ClosedPositionPath = 0

# ====================================================================
keyFrame5181 = CameraKeyFrame()
keyFrame5181.KeyTime = 0.4525
keyFrame5181.KeyValues = [0.0]
keyFrame5181.Position = [21.59365392738673, 20.0, 24.208356805740927]
keyFrame5181.FocalPoint = [20, 20, 20]
keyFrame5181.ViewUp = [0.4675016737167914, -0.866, -0.17703729184279832]
keyFrame5181.ViewAngle = 30.0
keyFrame5181.ParallelScale = 0.97681
keyFrame5181.PositionPathPoints = [21.59365392738673, 20.0, 24.208356805740927]
keyFrame5181.FocalPathPoints = [20, 20, 20]
keyFrame5181.PositionMode = 'Path'
keyFrame5181.FocalPointMode = 'Path'
keyFrame5181.ClosedFocalPath = 0
keyFrame5181.ClosedPositionPath = 0

# ====================================================================
keyFrame5182 = CameraKeyFrame()
keyFrame5182.KeyTime = 0.455
keyFrame5182.KeyValues = [0.0]
keyFrame5182.Position = [21.602067448077452, 20.0, 24.205161083303754]
keyFrame5182.FocalPoint = [20, 20, 20]
keyFrame5182.ViewUp = [0.4671466641157478, -0.866, -0.17797194117085563]
keyFrame5182.ViewAngle = 30.0
keyFrame5182.ParallelScale = 0.97681
keyFrame5182.PositionPathPoints = [21.602067448077452, 20.0, 24.205161083303754]
keyFrame5182.FocalPathPoints = [20, 20, 20]
keyFrame5182.PositionMode = 'Path'
keyFrame5182.FocalPointMode = 'Path'
keyFrame5182.ClosedFocalPath = 0
keyFrame5182.ClosedPositionPath = 0

# ====================================================================
keyFrame5183 = CameraKeyFrame()
keyFrame5183.KeyTime = 0.4575
keyFrame5183.KeyValues = [0.0]
keyFrame5183.Position = [21.61047456049848, 20.0, 24.201948540238426]
keyFrame5183.FocalPoint = [20, 20, 20]
keyFrame5183.ViewUp = [0.46678978591847275, -0.866, -0.17890587863107643]
keyFrame5183.ViewAngle = 30.0
keyFrame5183.ParallelScale = 0.97681
keyFrame5183.PositionPathPoints = [21.61047456049848, 20.0, 24.201948540238426]
keyFrame5183.FocalPathPoints = [20, 20, 20]
keyFrame5183.PositionMode = 'Path'
keyFrame5183.FocalPointMode = 'Path'
keyFrame5183.ClosedFocalPath = 0
keyFrame5183.ClosedPositionPath = 0

# ====================================================================
keyFrame5184 = CameraKeyFrame()
keyFrame5184.KeyTime = 0.46
keyFrame5184.KeyValues = [0.0]
keyFrame5184.Position = [21.618875231021367, 20.0, 24.1987191893957]
keyFrame5184.FocalPoint = [20, 20, 20]
keyFrame5184.ViewUp = [0.46643104055342716, -0.866, -0.17983910048471125]
keyFrame5184.ViewAngle = 30.0
keyFrame5184.ParallelScale = 0.97681
keyFrame5184.PositionPathPoints = [21.618875231021367, 20.0, 24.1987191893957]
keyFrame5184.FocalPathPoints = [20, 20, 20]
keyFrame5184.PositionMode = 'Path'
keyFrame5184.FocalPointMode = 'Path'
keyFrame5184.ClosedFocalPath = 0
keyFrame5184.ClosedPositionPath = 0

# ====================================================================
keyFrame5185 = CameraKeyFrame()
keyFrame5185.KeyTime = 0.4625
keyFrame5185.KeyValues = [0.0]
keyFrame5185.Position = [21.62726942604343, 20.0, 24.19547304369353]
keyFrame5185.FocalPoint = [20, 20, 20]
keyFrame5185.ViewUp = [0.4660704294566113, -0.866, -0.18077160299574185]
keyFrame5185.ViewAngle = 30.0
keyFrame5185.ParallelScale = 0.97681
keyFrame5185.PositionPathPoints = [21.62726942604343, 20.0, 24.19547304369353]
keyFrame5185.FocalPathPoints = [20, 20, 20]
keyFrame5185.PositionMode = 'Path'
keyFrame5185.FocalPointMode = 'Path'
keyFrame5185.ClosedFocalPath = 0
keyFrame5185.ClosedPositionPath = 0

# ====================================================================
keyFrame5186 = CameraKeyFrame()
keyFrame5186.KeyTime = 0.465
keyFrame5186.KeyValues = [0.0]
keyFrame5186.Position = [21.635657111987904, 20.0, 24.192210116117025]
keyFrame5186.FocalPoint = [20, 20, 20]
keyFrame5186.ViewUp = [0.4657079540715603, -0.866, -0.1817033824309014]
keyFrame5186.ViewAngle = 30.0
keyFrame5186.ParallelScale = 0.97681
keyFrame5186.PositionPathPoints = [21.635657111987904, 20.0, 24.192210116117025]
keyFrame5186.FocalPathPoints = [20, 20, 20]
keyFrame5186.PositionMode = 'Path'
keyFrame5186.FocalPointMode = 'Path'
keyFrame5186.ClosedFocalPath = 0
keyFrame5186.ClosedPositionPath = 0

# ====================================================================
keyFrame5187 = CameraKeyFrame()
keyFrame5187.KeyTime = 0.4675
keyFrame5187.KeyValues = [0.0]
keyFrame5187.Position = [21.644038255304064, 20.0, 24.188930419718385]
keyFrame5187.FocalPoint = [20, 20, 20]
keyFrame5187.ViewUp = [0.46534361584933864, -0.866, -0.18263443505969473]
keyFrame5187.ViewAngle = 30.0
keyFrame5187.ParallelScale = 0.97681
keyFrame5187.PositionPathPoints = [21.644038255304064, 20.0, 24.188930419718385]
keyFrame5187.FocalPathPoints = [20, 20, 20]
keyFrame5187.PositionMode = 'Path'
keyFrame5187.FocalPointMode = 'Path'
keyFrame5187.ClosedFocalPath = 0
keyFrame5187.ClosedPositionPath = 0

# ====================================================================
keyFrame5188 = CameraKeyFrame()
keyFrame5188.KeyTime = 0.47
keyFrame5188.KeyValues = [0.0]
keyFrame5188.Position = [21.652412822467355, 20.0, 24.185633967616848]
keyFrame5188.FocalPoint = [20, 20, 20]
keyFrame5188.ViewUp = [0.46497741624853517, -0.866, -0.18356475715441856]
keyFrame5188.ViewAngle = 30.0
keyFrame5188.ParallelScale = 0.97681
keyFrame5188.PositionPathPoints = [21.652412822467355, 20.0, 24.185633967616848]
keyFrame5188.FocalPathPoints = [20, 20, 20]
keyFrame5188.PositionMode = 'Path'
keyFrame5188.FocalPointMode = 'Path'
keyFrame5188.ClosedFocalPath = 0
keyFrame5188.ClosedPositionPath = 0

# ====================================================================
keyFrame5189 = CameraKeyFrame()
keyFrame5189.KeyTime = 0.4725
keyFrame5189.KeyValues = [0.0]
keyFrame5189.Position = [21.660780779979543, 20.0, 24.182320772998622]
keyFrame5189.FocalPoint = [20, 20, 20]
keyFrame5189.ViewUp = [0.46460935673525783, -0.866, -0.18449434499018155]
keyFrame5189.ViewAngle = 30.0
keyFrame5189.ParallelScale = 0.97681
keyFrame5189.PositionPathPoints = [21.660780779979543, 20.0, 24.182320772998622]
keyFrame5189.FocalPathPoints = [20, 20, 20]
keyFrame5189.PositionMode = 'Path'
keyFrame5189.FocalPointMode = 'Path'
keyFrame5189.ClosedFocalPath = 0
keyFrame5189.ClosedPositionPath = 0

# ====================================================================
keyFrame5190 = CameraKeyFrame()
keyFrame5190.KeyTime = 0.475
keyFrame5190.KeyValues = [0.0]
keyFrame5190.Position = [21.669142094368834, 20.0, 24.17899084911684]
keyFrame5190.FocalPoint = [20, 20, 20]
keyFrame5190.ViewUp = [0.4642394387831286, -0.866, -0.18542319484492475]
keyFrame5190.ViewAngle = 30.0
keyFrame5190.ParallelScale = 0.97681
keyFrame5190.PositionPathPoints = [21.669142094368834, 20.0, 24.17899084911684]
keyFrame5190.FocalPathPoints = [20, 20, 20]
keyFrame5190.PositionMode = 'Path'
keyFrame5190.FocalPointMode = 'Path'
keyFrame5190.ClosedFocalPath = 0
keyFrame5190.ClosedPositionPath = 0

# ====================================================================
keyFrame5191 = CameraKeyFrame()
keyFrame5191.KeyTime = 0.4775
keyFrame5191.KeyValues = [0.0]
keyFrame5191.Position = [21.677496732190015, 20.0, 24.175644209291498]
keyFrame5191.FocalPoint = [20, 20, 20]
keyFrame5191.ViewUp = [0.4638676638732786, -0.866, -0.1863513029994416]
keyFrame5191.ViewAngle = 30.0
keyFrame5191.ParallelScale = 0.97681
keyFrame5191.PositionPathPoints = [21.677496732190015, 20.0, 24.175644209291498]
keyFrame5191.FocalPathPoints = [20, 20, 20]
keyFrame5191.PositionMode = 'Path'
keyFrame5191.FocalPointMode = 'Path'
keyFrame5191.ClosedFocalPath = 0
keyFrame5191.ClosedPositionPath = 0

# ====================================================================
keyFrame5192 = CameraKeyFrame()
keyFrame5192.KeyTime = 0.48
keyFrame5192.KeyValues = [0.0]
keyFrame5192.Position = [21.685844660024586, 20.0, 24.172280866909393]
keyFrame5192.FocalPoint = [20, 20, 20]
keyFrame5192.ViewUp = [0.4634940334943424, -0.866, -0.18727866573739832]
keyFrame5192.ViewAngle = 30.0
keyFrame5192.ParallelScale = 0.97681
keyFrame5192.PositionPathPoints = [21.685844660024586, 20.0, 24.172280866909393]
keyFrame5192.FocalPathPoints = [20, 20, 20]
keyFrame5192.PositionMode = 'Path'
keyFrame5192.FocalPointMode = 'Path'
keyFrame5192.ClosedFocalPath = 0
keyFrame5192.ClosedPositionPath = 0

# ====================================================================
keyFrame5193 = CameraKeyFrame()
keyFrame5193.KeyTime = 0.4825
keyFrame5193.KeyValues = [0.0]
keyFrame5193.Position = [21.6941858444809, 20.0, 24.168900835424065]
keyFrame5193.FocalPoint = [20, 20, 20]
keyFrame5193.ViewUp = [0.46311854914245326, -0.866, -0.18820527934535394]
keyFrame5193.ViewAngle = 30.0
keyFrame5193.ParallelScale = 0.97681
keyFrame5193.PositionPathPoints = [21.6941858444809, 20.0, 24.168900835424065]
keyFrame5193.FocalPathPoints = [20, 20, 20]
keyFrame5193.PositionMode = 'Path'
keyFrame5193.FocalPointMode = 'Path'
keyFrame5193.ClosedFocalPath = 0
keyFrame5193.ClosedPositionPath = 0

# ====================================================================
keyFrame5194 = CameraKeyFrame()
keyFrame5194.KeyTime = 0.485
keyFrame5194.KeyValues = [0.0]
keyFrame5194.Position = [21.702520252194283, 20.0, 24.16550412835574]
keyFrame5194.FocalPoint = [20, 20, 20]
keyFrame5194.ViewUp = [0.46274121232123805, -0.866, -0.18913114011278068]
keyFrame5194.ViewAngle = 30.0
keyFrame5194.ParallelScale = 0.97681
keyFrame5194.PositionPathPoints = [21.702520252194283, 20.0, 24.16550412835574]
keyFrame5194.FocalPathPoints = [20, 20, 20]
keyFrame5194.PositionMode = 'Path'
keyFrame5194.FocalPointMode = 'Path'
keyFrame5194.ClosedFocalPath = 0
keyFrame5194.ClosedPositionPath = 0

# ====================================================================
keyFrame5195 = CameraKeyFrame()
keyFrame5195.KeyTime = 0.4875
keyFrame5195.KeyValues = [0.0]
keyFrame5195.Position = [21.71084784982719, 20.0, 24.16209075929126]
keyFrame5195.FocalPoint = [20, 20, 20]
keyFrame5195.ViewUp = [0.4623620245418119, -0.866, -0.19005624433208396]
keyFrame5195.ViewAngle = 30.0
keyFrame5195.ParallelScale = 0.97681
keyFrame5195.PositionPathPoints = [21.71084784982719, 20.0, 24.16209075929126]
keyFrame5195.FocalPathPoints = [20, 20, 20]
keyFrame5195.PositionMode = 'Path'
keyFrame5195.FocalPointMode = 'Path'
keyFrame5195.ClosedFocalPath = 0
keyFrame5195.ClosedPositionPath = 0

# ====================================================================
keyFrame5196 = CameraKeyFrame()
keyFrame5196.KeyTime = 0.49
keyFrame5196.KeyValues = [0.0]
keyFrame5196.Position = [21.719168604069317, 20.0, 24.15866074188405]
keyFrame5196.FocalPoint = [20, 20, 20]
keyFrame5196.ViewUp = [0.4619809873227732, -0.866, -0.19098058829862286]
keyFrame5196.ViewAngle = 30.0
keyFrame5196.ParallelScale = 0.97681
keyFrame5196.PositionPathPoints = [21.719168604069317, 20.0, 24.15866074188405]
keyFrame5196.FocalPathPoints = [20, 20, 20]
keyFrame5196.PositionMode = 'Path'
keyFrame5196.FocalPointMode = 'Path'
keyFrame5196.ClosedFocalPath = 0
keyFrame5196.ClosedPositionPath = 0

# ====================================================================
keyFrame5197 = CameraKeyFrame()
keyFrame5197.KeyTime = 0.4925
keyFrame5197.KeyValues = [0.0]
keyFrame5197.Position = [21.72748248163774, 20.0, 24.155214089854006]
keyFrame5197.FocalPoint = [20, 20, 20]
keyFrame5197.ViewUp = [0.4615981021901982, -0.866, -0.19190416831073015]
keyFrame5197.ViewAngle = 30.0
keyFrame5197.ParallelScale = 0.97681
keyFrame5197.PositionPathPoints = [21.72748248163774, 20.0, 24.155214089854006]
keyFrame5197.FocalPathPoints = [20, 20, 20]
keyFrame5197.PositionMode = 'Path'
keyFrame5197.FocalPointMode = 'Path'
keyFrame5197.ClosedFocalPath = 0
keyFrame5197.ClosedPositionPath = 0

# ====================================================================
keyFrame5198 = CameraKeyFrame()
keyFrame5198.KeyTime = 0.495
keyFrame5198.KeyValues = [0.0]
keyFrame5198.Position = [21.73578944927706, 20.0, 24.1517508169875]
keyFrame5198.FocalPoint = [20, 20, 20]
keyFrame5198.ViewUp = [0.4612133706776364, -0.866, -0.1928269806697325]
keyFrame5198.ViewAngle = 30.0
keyFrame5198.ParallelScale = 0.97681
keyFrame5198.PositionPathPoints = [21.73578944927706, 20.0, 24.1517508169875]
keyFrame5198.FocalPathPoints = [20, 20, 20]
keyFrame5198.PositionMode = 'Path'
keyFrame5198.FocalPointMode = 'Path'
keyFrame5198.ClosedFocalPath = 0
keyFrame5198.ClosedPositionPath = 0

# ====================================================================
keyFrame5199 = CameraKeyFrame()
keyFrame5199.KeyTime = 0.4975
keyFrame5199.KeyValues = [0.0]
keyFrame5199.Position = [21.744089473759523, 20.0, 24.148270937137262]
keyFrame5199.FocalPoint = [20, 20, 20]
keyFrame5199.ViewUp = [0.4608267943261048, -0.866, -0.19374902167997082]
keyFrame5199.ViewAngle = 30.0
keyFrame5199.ParallelScale = 0.97681
keyFrame5199.PositionPathPoints = [21.744089473759523, 20.0, 24.148270937137262]
keyFrame5199.FocalPathPoints = [20, 20, 20]
keyFrame5199.PositionMode = 'Path'
keyFrame5199.FocalPointMode = 'Path'
keyFrame5199.ClosedFocalPath = 0
keyFrame5199.ClosedPositionPath = 0

# ====================================================================
keyFrame5200 = CameraKeyFrame()
keyFrame5200.KeyTime = 0.5
keyFrame5200.KeyValues = [0.0]
keyFrame5200.Position = [21.752382521885167, 20.0, 24.14477446422234]
keyFrame5200.FocalPoint = [20, 20, 20]
keyFrame5200.ViewUp = [0.4604383746840831, -0.866, -0.19467028764882033]
keyFrame5200.ViewAngle = 30.0
keyFrame5200.ParallelScale = 0.97681
keyFrame5200.PositionPathPoints = [21.752382521885167, 20.0, 24.14477446422234]
keyFrame5200.FocalPathPoints = [20, 20, 20]
keyFrame5200.PositionMode = 'Path'
keyFrame5200.FocalPointMode = 'Path'
keyFrame5200.ClosedFocalPath = 0
keyFrame5200.ClosedPositionPath = 0

# ====================================================================
keyFrame5201 = CameraKeyFrame()
keyFrame5201.KeyTime = 0.5025
keyFrame5201.KeyValues = [0.0]
keyFrame5201.Position = [21.76066856048194, 20.0, 24.141261412228047]
keyFrame5201.FocalPoint = [20, 20, 20]
keyFrame5201.ViewUp = [0.4600481133075087, -0.866, -0.19559077488671084]
keyFrame5201.ViewAngle = 30.0
keyFrame5201.ParallelScale = 0.97681
keyFrame5201.PositionPathPoints = [21.76066856048194, 20.0, 24.141261412228047]
keyFrame5201.FocalPathPoints = [20, 20, 20]
keyFrame5201.PositionMode = 'Path'
keyFrame5201.FocalPointMode = 'Path'
keyFrame5201.ClosedFocalPath = 0
keyFrame5201.ClosedPositionPath = 0

# ====================================================================
keyFrame5202 = CameraKeyFrame()
keyFrame5202.KeyTime = 0.505
keyFrame5202.KeyValues = [0.0]
keyFrame5202.Position = [21.768947556405838, 20.0, 24.13773179520588]
keyFrame5202.FocalPoint = [20, 20, 20]
keyFrame5202.ViewUp = [0.4596560117597712, -0.866, -0.196510479707147]
keyFrame5202.ViewAngle = 30.0
keyFrame5202.ParallelScale = 0.97681
keyFrame5202.PositionPathPoints = [21.768947556405838, 20.0, 24.13773179520588]
keyFrame5202.FocalPathPoints = [20, 20, 20]
keyFrame5202.PositionMode = 'Path'
keyFrame5202.FocalPointMode = 'Path'
keyFrame5202.ClosedFocalPath = 0
keyFrame5202.ClosedPositionPath = 0

# ====================================================================
keyFrame5203 = CameraKeyFrame()
keyFrame5203.KeyTime = 0.5075
keyFrame5203.KeyValues = [0.0]
keyFrame5203.Position = [21.77721947654105, 20.0, 24.13418562727346]
keyFrame5203.FocalPoint = [20, 20, 20]
keyFrame5203.ViewUp = [0.4592620716117074, -0.866, -0.19742939842672838]
keyFrame5203.ViewAngle = 30.0
keyFrame5203.ParallelScale = 0.97681
keyFrame5203.PositionPathPoints = [21.77721947654105, 20.0, 24.13418562727346]
keyFrame5203.FocalPathPoints = [20, 20, 20]
keyFrame5203.PositionMode = 'Path'
keyFrame5203.FocalPointMode = 'Path'
keyFrame5203.ClosedFocalPath = 0
keyFrame5203.ClosedPositionPath = 0

# ====================================================================
keyFrame5204 = CameraKeyFrame()
keyFrame5204.KeyTime = 0.51
keyFrame5204.KeyValues = [0.0]
keyFrame5204.Position = [21.785484287800074, 20.0, 24.130622922614485]
keyFrame5204.FocalPoint = [20, 20, 20]
keyFrame5204.ViewUp = [0.4588662944415962, -0.866, -0.1983475273651698]
keyFrame5204.ViewAngle = 30.0
keyFrame5204.ParallelScale = 0.97681
keyFrame5204.PositionPathPoints = [21.785484287800074, 20.0, 24.130622922614485]
keyFrame5204.FocalPathPoints = [20, 20, 20]
keyFrame5204.PositionMode = 'Path'
keyFrame5204.FocalPointMode = 'Path'
keyFrame5204.ClosedFocalPath = 0
keyFrame5204.ClosedPositionPath = 0

# ====================================================================
keyFrame5205 = CameraKeyFrame()
keyFrame5205.KeyTime = 0.5125
keyFrame5205.KeyValues = [0.0]
keyFrame5205.Position = [21.79374195712386, 20.0, 24.12704369547864]
keyFrame5205.FocalPoint = [20, 20, 20]
keyFrame5205.ViewUp = [0.4584686818351536, -0.866, -0.19926486284532155]
keyFrame5205.ViewAngle = 30.0
keyFrame5205.ParallelScale = 0.97681
keyFrame5205.PositionPathPoints = [21.79374195712386, 20.0, 24.12704369547864]
keyFrame5205.FocalPathPoints = [20, 20, 20]
keyFrame5205.PositionMode = 'Path'
keyFrame5205.FocalPointMode = 'Path'
keyFrame5205.ClosedFocalPath = 0
keyFrame5205.ClosedPositionPath = 0

# ====================================================================
keyFrame5206 = CameraKeyFrame()
keyFrame5206.KeyTime = 0.515
keyFrame5206.KeyValues = [0.0]
keyFrame5206.Position = [21.80199245148194, 20.0, 24.12344796018155]
keyFrame5206.FocalPoint = [20, 20, 20]
keyFrame5206.ViewUp = [0.4580692353855272, -0.866, -0.20018140119318945]
keyFrame5206.ViewAngle = 30.0
keyFrame5206.ParallelScale = 0.97681
keyFrame5206.PositionPathPoints = [21.80199245148194, 20.0, 24.12344796018155]
keyFrame5206.FocalPathPoints = [20, 20, 20]
keyFrame5206.PositionMode = 'Path'
keyFrame5206.FocalPointMode = 'Path'
keyFrame5206.ClosedFocalPath = 0
keyFrame5206.ClosedPositionPath = 0

# ====================================================================
keyFrame5207 = CameraKeyFrame()
keyFrame5207.KeyTime = 0.5175
keyFrame5207.KeyValues = [0.0]
keyFrame5207.Position = [21.810235737872567, 20.0, 24.119835731104715]
keyFrame5207.FocalPoint = [20, 20, 20]
keyFrame5207.ViewUp = [0.45766795669316107, -0.866, -0.20109713873811724]
keyFrame5207.ViewAngle = 30.0
keyFrame5207.ParallelScale = 0.97681
keyFrame5207.PositionPathPoints = [21.810235737872567, 20.0, 24.119835731104715]
keyFrame5207.FocalPathPoints = [20, 20, 20]
keyFrame5207.PositionMode = 'Path'
keyFrame5207.FocalPointMode = 'Path'
keyFrame5207.ClosedFocalPath = 0
keyFrame5207.ClosedPositionPath = 0

# ====================================================================
keyFrame5208 = CameraKeyFrame()
keyFrame5208.KeyTime = 0.52
keyFrame5208.KeyValues = [0.0]
keyFrame5208.Position = [21.818471783322835, 20.0, 24.116207022695423]
keyFrame5208.FocalPoint = [20, 20, 20]
keyFrame5208.ViewUp = [0.45726484734623607, -0.866, -0.2020120718370998]
keyFrame5208.ViewAngle = 30.0
keyFrame5208.ParallelScale = 0.97681
keyFrame5208.PositionPathPoints = [21.818471783322835, 20.0, 24.116207022695423]
keyFrame5208.FocalPathPoints = [20, 20, 20]
keyFrame5208.PositionMode = 'Path'
keyFrame5208.FocalPointMode = 'Path'
keyFrame5208.ClosedFocalPath = 0
keyFrame5208.ClosedPositionPath = 0

# ====================================================================
keyFrame5209 = CameraKeyFrame()
keyFrame5209.KeyTime = 0.5225
keyFrame5209.KeyValues = [0.0]
keyFrame5209.Position = [21.826700554888816, 20.0, 24.11256184946672]
keyFrame5209.FocalPoint = [20, 20, 20]
keyFrame5209.ViewUp = [0.4568599089439105, -0.866, -0.20292619684592444]
keyFrame5209.ViewAngle = 30.0
keyFrame5209.ParallelScale = 0.97681
keyFrame5209.PositionPathPoints = [21.826700554888816, 20.0, 24.11256184946672]
keyFrame5209.FocalPathPoints = [20, 20, 20]
keyFrame5209.PositionMode = 'Path'
keyFrame5209.FocalPointMode = 'Path'
keyFrame5209.ClosedFocalPath = 0
keyFrame5209.ClosedPositionPath = 0

# ====================================================================
keyFrame5210 = CameraKeyFrame()
keyFrame5210.KeyTime = 0.525
keyFrame5210.KeyValues = [0.0]
keyFrame5210.Position = [21.834922019655703, 20.0, 24.108900225997306]
keyFrame5210.FocalPoint = [20, 20, 20]
keyFrame5210.ViewUp = [0.456453143106023, -0.866, -0.20383951010713008]
keyFrame5210.ViewAngle = 30.0
keyFrame5210.ParallelScale = 0.97681
keyFrame5210.PositionPathPoints = [21.834922019655703, 20.0, 24.108900225997306]
keyFrame5210.FocalPathPoints = [20, 20, 20]
keyFrame5210.PositionMode = 'Path'
keyFrame5210.FocalPointMode = 'Path'
keyFrame5210.ClosedFocalPath = 0
keyFrame5210.ClosedPositionPath = 0

# ====================================================================
keyFrame5211 = CameraKeyFrame()
keyFrame5211.KeyTime = 0.5275
keyFrame5211.KeyValues = [0.0]
keyFrame5211.Position = [21.843136144737933, 20.0, 24.105222166931497]
keyFrame5211.FocalPoint = [20, 20, 20]
keyFrame5211.ViewUp = [0.4560445514597079, -0.866, -0.2047520079666491]
keyFrame5211.ViewAngle = 30.0
keyFrame5211.ParallelScale = 0.97681
keyFrame5211.PositionPathPoints = [21.843136144737933, 20.0, 24.105222166931497]
keyFrame5211.FocalPathPoints = [20, 20, 20]
keyFrame5211.PositionMode = 'Path'
keyFrame5211.FocalPointMode = 'Path'
keyFrame5211.ClosedFocalPath = 0
keyFrame5211.ClosedPositionPath = 0

# ====================================================================
keyFrame5212 = CameraKeyFrame()
keyFrame5212.KeyTime = 0.53
keyFrame5212.KeyValues = [0.0]
keyFrame5212.Position = [21.851342897279316, 20.0, 24.101527686979143]
keyFrame5212.FocalPoint = [20, 20, 20]
keyFrame5212.ViewUp = [0.45563413563938887, -0.866, -0.20566368677382996]
keyFrame5212.ViewAngle = 30.0
keyFrame5212.ParallelScale = 0.97681
keyFrame5212.PositionPathPoints = [21.851342897279316, 20.0, 24.101527686979143]
keyFrame5212.FocalPathPoints = [20, 20, 20]
keyFrame5212.PositionMode = 'Path'
keyFrame5212.FocalPointMode = 'Path'
keyFrame5212.ClosedFocalPath = 0
keyFrame5212.ClosedPositionPath = 0

# ====================================================================
keyFrame5213 = CameraKeyFrame()
keyFrame5213.KeyTime = 0.5325
keyFrame5213.KeyValues = [0.0]
keyFrame5213.Position = [21.85954224445318, 20.0, 24.097816800915556]
keyFrame5213.FocalPoint = [20, 20, 20]
keyFrame5213.ViewUp = [0.4552218972867717, -0.866, -0.20657454288145918]
keyFrame5213.ViewAngle = 30.0
keyFrame5213.ParallelScale = 0.97681
keyFrame5213.PositionPathPoints = [21.85954224445318, 20.0, 24.097816800915556]
keyFrame5213.FocalPathPoints = [20, 20, 20]
keyFrame5213.PositionMode = 'Path'
keyFrame5213.FocalPointMode = 'Path'
keyFrame5213.ClosedFocalPath = 0
keyFrame5213.ClosedPositionPath = 0

# ====================================================================
keyFrame5214 = CameraKeyFrame()
keyFrame5214.KeyTime = 0.535
keyFrame5214.KeyValues = [0.0]
keyFrame5214.Position = [21.867734153462482, 20.0, 24.09408952358146]
keyFrame5214.FocalPoint = [20, 20, 20]
keyFrame5214.ViewUp = [0.4548078380508377, -0.866, -0.2074845726457838]
keyFrame5214.ViewAngle = 30.0
keyFrame5214.ParallelScale = 0.97681
keyFrame5214.PositionPathPoints = [21.867734153462482, 20.0, 24.09408952358146]
keyFrame5214.FocalPathPoints = [20, 20, 20]
keyFrame5214.PositionMode = 'Path'
keyFrame5214.FocalPointMode = 'Path'
keyFrame5214.ClosedFocalPath = 0
keyFrame5214.ClosedPositionPath = 0

# ====================================================================
keyFrame5215 = CameraKeyFrame()
keyFrame5215.KeyTime = 0.5375
keyFrame5215.KeyValues = [0.0]
keyFrame5215.Position = [21.875918591539964, 20.0, 24.0903458698829]
keyFrame5215.FocalPoint = [20, 20, 20]
keyFrame5215.ViewUp = [0.4543919595878368, -0.866, -0.2083937724265335]
keyFrame5215.ViewAngle = 30.0
keyFrame5215.ParallelScale = 0.97681
keyFrame5215.PositionPathPoints = [21.875918591539964, 20.0, 24.0903458698829]
keyFrame5215.FocalPathPoints = [20, 20, 20]
keyFrame5215.PositionMode = 'Path'
keyFrame5215.FocalPointMode = 'Path'
keyFrame5215.ClosedFocalPath = 0
keyFrame5215.ClosedPositionPath = 0

# ====================================================================
keyFrame5216 = CameraKeyFrame()
keyFrame5216.KeyTime = 0.54
keyFrame5216.KeyValues = [0.0]
keyFrame5216.Position = [21.884095525948275, 20.0, 24.086585854791192]
keyFrame5216.FocalPoint = [20, 20, 20]
keyFrame5216.ViewUp = [0.453974263561281, -0.866, -0.20930213858694297]
keyFrame5216.ViewAngle = 30.0
keyFrame5216.ParallelScale = 0.97681
keyFrame5216.PositionPathPoints = [21.884095525948275, 20.0, 24.086585854791192]
keyFrame5216.FocalPathPoints = [20, 20, 20]
keyFrame5216.PositionMode = 'Path'
keyFrame5216.FocalPointMode = 'Path'
keyFrame5216.ClosedFocalPath = 0
keyFrame5216.ClosedPositionPath = 0

# ====================================================================
keyFrame5217 = CameraKeyFrame()
keyFrame5217.KeyTime = 0.5425
keyFrame5217.KeyValues = [0.0]
keyFrame5217.Position = [21.89226492398009, 20.0, 24.082809493342843]
keyFrame5217.FocalPoint = [20, 20, 20]
keyFrame5217.ViewUp = [0.45355475164193726, -0.866, -0.21020966749377412]
keyFrame5217.ViewAngle = 30.0
keyFrame5217.ParallelScale = 0.97681
keyFrame5217.PositionPathPoints = [21.89226492398009, 20.0, 24.082809493342843]
keyFrame5217.FocalPathPoints = [20, 20, 20]
keyFrame5217.PositionMode = 'Path'
keyFrame5217.FocalPointMode = 'Path'
keyFrame5217.ClosedFocalPath = 0
keyFrame5217.ClosedPositionPath = 0

# ====================================================================
keyFrame5218 = CameraKeyFrame()
keyFrame5218.KeyTime = 0.545
keyFrame5218.KeyValues = [0.0]
keyFrame5218.Position = [21.90042675295827, 20.0, 24.07901680063948]
keyFrame5218.FocalPoint = [20, 20, 20]
keyFrame5218.ViewUp = [0.45313342550782093, -0.866, -0.21111635551733832]
keyFrame5218.ViewAngle = 30.0
keyFrame5218.ParallelScale = 0.97681
keyFrame5218.PositionPathPoints = [21.90042675295827, 20.0, 24.07901680063948]
keyFrame5218.FocalPathPoints = [20, 20, 20]
keyFrame5218.PositionMode = 'Path'
keyFrame5218.FocalPointMode = 'Path'
keyFrame5218.ClosedFocalPath = 0
keyFrame5218.ClosedPositionPath = 0

# ====================================================================
keyFrame5219 = CameraKeyFrame()
keyFrame5219.KeyTime = 0.5475
keyFrame5219.KeyValues = [0.0]
keyFrame5219.Position = [21.908580980235964, 20.0, 24.075207791847788]
keyFrame5219.FocalPoint = [20, 20, 20]
keyFrame5219.ViewUp = [0.45271028684418885, -0.866, -0.2120221990315187]
keyFrame5219.ViewAngle = 30.0
keyFrame5219.ParallelScale = 0.97681
keyFrame5219.PositionPathPoints = [21.908580980235964, 20.0, 24.075207791847788]
keyFrame5219.FocalPathPoints = [20, 20, 20]
keyFrame5219.PositionMode = 'Path'
keyFrame5219.FocalPointMode = 'Path'
keyFrame5219.ClosedFocalPath = 0
keyFrame5219.ClosedPositionPath = 0

# ====================================================================
keyFrame5220 = CameraKeyFrame()
keyFrame5220.KeyTime = 0.55
keyFrame5220.KeyValues = [0.0]
keyFrame5220.Position = [21.91672757319676, 20.0, 24.071382482199432]
keyFrame5220.FocalPoint = [20, 20, 20]
keyFrame5220.ViewUp = [0.4522853373435326, -0.866, -0.21292719441379246]
keyFrame5220.ViewAngle = 30.0
keyFrame5220.ParallelScale = 0.97681
keyFrame5220.PositionPathPoints = [21.91672757319676, 20.0, 24.071382482199432]
keyFrame5220.FocalPathPoints = [20, 20, 20]
keyFrame5220.PositionMode = 'Path'
keyFrame5220.FocalPointMode = 'Path'
keyFrame5220.ClosedFocalPath = 0
keyFrame5220.ClosedPositionPath = 0

# ====================================================================
keyFrame5221 = CameraKeyFrame()
keyFrame5221.KeyTime = 0.5525
keyFrame5221.KeyValues = [0.0]
keyFrame5221.Position = [21.92486649925481, 20.0, 24.06754088699099]
keyFrame5221.FocalPoint = [20, 20, 20]
keyFrame5221.ViewUp = [0.4518585787055718, -0.866, -0.21383133804525298]
keyFrame5221.ViewAngle = 30.0
keyFrame5221.ParallelScale = 0.97681
keyFrame5221.PositionPathPoints = [21.92486649925481, 20.0, 24.06754088699099]
keyFrame5221.FocalPathPoints = [20, 20, 20]
keyFrame5221.PositionMode = 'Path'
keyFrame5221.FocalPointMode = 'Path'
keyFrame5221.ClosedFocalPath = 0
keyFrame5221.ClosedPositionPath = 0

# ====================================================================
keyFrame5222 = CameraKeyFrame()
keyFrame5222.KeyTime = 0.555
keyFrame5222.KeyValues = [0.0]
keyFrame5222.Position = [21.93299772585496, 20.0, 24.06368302158387]
keyFrame5222.FocalPoint = [20, 20, 20]
keyFrame5222.ViewUp = [0.451430012637247, -0.866, -0.21473462631063228]
keyFrame5222.ViewAngle = 30.0
keyFrame5222.ParallelScale = 0.97681
keyFrame5222.PositionPathPoints = [21.93299772585496, 20.0, 24.06368302158387]
keyFrame5222.FocalPathPoints = [20, 20, 20]
keyFrame5222.PositionMode = 'Path'
keyFrame5222.FocalPointMode = 'Path'
keyFrame5222.ClosedFocalPath = 0
keyFrame5222.ClosedPositionPath = 0

# ====================================================================
keyFrame5223 = CameraKeyFrame()
keyFrame5223.KeyTime = 0.5575
keyFrame5223.KeyValues = [0.0]
keyFrame5223.Position = [21.941121220472883, 20.0, 24.059808901404256]
keyFrame5223.FocalPoint = [20, 20, 20]
keyFrame5223.ViewUp = [0.45099964085271343, -0.866, -0.21563705559832314]
keyFrame5223.ViewAngle = 30.0
keyFrame5223.ParallelScale = 0.97681
keyFrame5223.PositionPathPoints = [21.941121220472883, 20.0, 24.059808901404256]
keyFrame5223.FocalPathPoints = [20, 20, 20]
keyFrame5223.PositionMode = 'Path'
keyFrame5223.FocalPointMode = 'Path'
keyFrame5223.ClosedFocalPath = 0
keyFrame5223.ClosedPositionPath = 0

# ====================================================================
keyFrame5224 = CameraKeyFrame()
keyFrame5224.KeyTime = 0.56
keyFrame5224.KeyValues = [0.0]
keyFrame5224.Position = [21.949236950615145, 20.0, 24.055918541943655]
keyFrame5224.FocalPoint = [20, 20, 20]
keyFrame5224.ViewUp = [0.4505674650733336, -0.866, -0.21653862230040133]
keyFrame5224.ViewAngle = 30.0
keyFrame5224.ParallelScale = 0.97681
keyFrame5224.PositionPathPoints = [21.949236950615145, 20.0, 24.055918541943655]
keyFrame5224.FocalPathPoints = [20, 20, 20]
keyFrame5224.PositionMode = 'Path'
keyFrame5224.FocalPointMode = 'Path'
keyFrame5224.ClosedFocalPath = 0
keyFrame5224.ClosedPositionPath = 0

# ====================================================================
keyFrame5225 = CameraKeyFrame()
keyFrame5225.KeyTime = 0.5625
keyFrame5225.KeyValues = [0.0]
keyFrame5225.Position = [21.95734488381487, 20.0, 24.05201195880099]
keyFrame5225.FocalPoint = [20, 20, 20]
keyFrame5225.ViewUp = [0.450133487027671, -0.866, -0.2174393228126481]
keyFrame5225.ViewAngle = 30.0
keyFrame5225.ParallelScale = 0.97681
keyFrame5225.PositionPathPoints = [21.95734488381487, 20.0, 24.05201195880099]
keyFrame5225.FocalPathPoints = [20, 20, 20]
keyFrame5225.PositionMode = 'Path'
keyFrame5225.FocalPointMode = 'Path'
keyFrame5225.ClosedFocalPath = 0
keyFrame5225.ClosedPositionPath = 0

# ====================================================================
keyFrame5226 = CameraKeyFrame()
keyFrame5226.KeyTime = 0.565
keyFrame5226.KeyValues = [0.0]
keyFrame5226.Position = [21.96544498763768, 20.0, 24.04808916762766]
keyFrame5226.FocalPoint = [20, 20, 20]
keyFrame5226.ViewUp = [0.44969770845148294, -0.866, -0.21833915353457214]
keyFrame5226.ViewAngle = 30.0
keyFrame5226.ParallelScale = 0.97681
keyFrame5226.PositionPathPoints = [21.96544498763768, 20.0, 24.04808916762766]
keyFrame5226.FocalPathPoints = [20, 20, 20]
keyFrame5226.PositionMode = 'Path'
keyFrame5226.FocalPointMode = 'Path'
keyFrame5226.ClosedFocalPath = 0
keyFrame5226.ClosedPositionPath = 0

# ====================================================================
keyFrame5227 = CameraKeyFrame()
keyFrame5227.KeyTime = 0.5675
keyFrame5227.KeyValues = [0.0]
keyFrame5227.Position = [21.973537229683124, 20.0, 24.044150184115242]
keyFrame5227.FocalPoint = [20, 20, 20]
keyFrame5227.ViewUp = [0.4492601310877141, -0.866, -0.21923811086943212]
keyFrame5227.ViewAngle = 30.0
keyFrame5227.ParallelScale = 0.97681
keyFrame5227.PositionPathPoints = [21.973537229683124, 20.0, 24.044150184115242]
keyFrame5227.FocalPathPoints = [20, 20, 20]
keyFrame5227.PositionMode = 'Path'
keyFrame5227.FocalPointMode = 'Path'
keyFrame5227.ClosedFocalPath = 0
keyFrame5227.ClosedPositionPath = 0

# ====================================================================
keyFrame5228 = CameraKeyFrame()
keyFrame5228.KeyTime = 0.57
keyFrame5228.KeyValues = [0.0]
keyFrame5228.Position = [21.981621577582192, 20.0, 24.040195024020054]
keyFrame5228.FocalPoint = [20, 20, 20]
keyFrame5228.ViewUp = [0.44882075668648946, -0.866, -0.2201361912242587]
keyFrame5228.ViewAngle = 30.0
keyFrame5228.ParallelScale = 0.97681
keyFrame5228.PositionPathPoints = [21.981621577582192, 20.0, 24.040195024020054]
keyFrame5228.FocalPathPoints = [20, 20, 20]
keyFrame5228.PositionMode = 'Path'
keyFrame5228.FocalPointMode = 'Path'
keyFrame5228.ClosedFocalPath = 0
keyFrame5228.ClosedPositionPath = 0

# ====================================================================
keyFrame5229 = CameraKeyFrame()
keyFrame5229.KeyTime = 0.5725
keyFrame5229.KeyValues = [0.0]
keyFrame5229.Position = [21.98969799899745, 20.0, 24.036223703163078]
keyFrame5229.FocalPoint = [20, 20, 20]
keyFrame5229.ViewUp = [0.4483795870051076, -0.866, -0.22103339100987704]
keyFrame5229.ViewAngle = 30.0
keyFrame5229.ParallelScale = 0.97681
keyFrame5229.PositionPathPoints = [21.98969799899745, 20.0, 24.036223703163078]
keyFrame5229.FocalPathPoints = [20, 20, 20]
keyFrame5229.PositionMode = 'Path'
keyFrame5229.FocalPointMode = 'Path'
keyFrame5229.ClosedFocalPath = 0
keyFrame5229.ClosedPositionPath = 0

# ====================================================================
keyFrame5230 = CameraKeyFrame()
keyFrame5230.KeyTime = 0.575
keyFrame5230.KeyValues = [0.0]
keyFrame5230.Position = [21.997766461623176, 20.0, 24.0322362374299]
keyFrame5230.FocalPoint = [20, 20, 20]
keyFrame5230.ViewUp = [0.447936623808034, -0.866, -0.22192970664092884]
keyFrame5230.ViewAngle = 30.0
keyFrame5230.ParallelScale = 0.97681
keyFrame5230.PositionPathPoints = [21.997766461623176, 20.0, 24.0322362374299]
keyFrame5230.FocalPathPoints = [20, 20, 20]
keyFrame5230.PositionMode = 'Path'
keyFrame5230.FocalPointMode = 'Path'
keyFrame5230.ClosedFocalPath = 0
keyFrame5230.ClosedPositionPath = 0

# ====================================================================
keyFrame5231 = CameraKeyFrame()
keyFrame5231.KeyTime = 0.5775
keyFrame5231.KeyValues = [0.0]
keyFrame5231.Position = [22.005826933185478, 20.0, 24.02823264277064]
keyFrame5231.FocalPoint = [20, 20, 20]
keyFrame5231.ViewUp = [0.44749186886689407, -0.866, -0.22282513453589475]
keyFrame5231.ViewAngle = 30.0
keyFrame5231.ParallelScale = 0.97681
keyFrame5231.PositionPathPoints = [22.005826933185478, 20.0, 24.02823264277064]
keyFrame5231.FocalPathPoints = [20, 20, 20]
keyFrame5231.PositionMode = 'Path'
keyFrame5231.FocalPointMode = 'Path'
keyFrame5231.ClosedFocalPath = 0
keyFrame5231.ClosedPositionPath = 0

# ====================================================================
keyFrame5232 = CameraKeyFrame()
keyFrame5232.KeyTime = 0.58
keyFrame5232.KeyValues = [0.0]
keyFrame5232.Position = [22.013879381442436, 20.0, 24.024212935199884]
keyFrame5232.FocalPoint = [20, 20, 20]
keyFrame5232.ViewUp = [0.4470453239604666, -0.866, -0.22371967111711658]
keyFrame5232.ViewAngle = 30.0
keyFrame5232.ParallelScale = 0.97681
keyFrame5232.PositionPathPoints = [22.013879381442436, 20.0, 24.024212935199884]
keyFrame5232.FocalPathPoints = [20, 20, 20]
keyFrame5232.PositionMode = 'Path'
keyFrame5232.FocalPointMode = 'Path'
keyFrame5232.ClosedFocalPath = 0
keyFrame5232.ClosedPositionPath = 0

# ====================================================================
keyFrame5233 = CameraKeyFrame()
keyFrame5233.KeyTime = 0.5825
keyFrame5233.KeyValues = [0.0]
keyFrame5233.Position = [22.02192377418422, 20.0, 24.020177130796625]
keyFrame5233.FocalPoint = [20, 20, 20]
keyFrame5233.ViewUp = [0.4465969908746767, -0.866, -0.22461331281081956]
keyFrame5233.ViewAngle = 30.0
keyFrame5233.ParallelScale = 0.97681
keyFrame5233.PositionPathPoints = [22.02192377418422, 20.0, 24.020177130796625]
keyFrame5233.FocalPathPoints = [20, 20, 20]
keyFrame5233.PositionMode = 'Path'
keyFrame5233.FocalPointMode = 'Path'
keyFrame5233.ClosedFocalPath = 0
keyFrame5233.ClosedPositionPath = 0

# ====================================================================
keyFrame5234 = CameraKeyFrame()
keyFrame5234.KeyTime = 0.585
keyFrame5234.KeyValues = [0.0]
keyFrame5234.Position = [22.029960079233224, 20.0, 24.016125245704185]
keyFrame5234.FocalPoint = [20, 20, 20]
keyFrame5234.ViewUp = [0.4461468714025892, -0.866, -0.2255060560471346]
keyFrame5234.ViewAngle = 30.0
keyFrame5234.ParallelScale = 0.97681
keyFrame5234.PositionPathPoints = [22.029960079233224, 20.0, 24.016125245704185]
keyFrame5234.FocalPathPoints = [20, 20, 20]
keyFrame5234.PositionMode = 'Path'
keyFrame5234.FocalPointMode = 'Path'
keyFrame5234.ClosedFocalPath = 0
keyFrame5234.ClosedPositionPath = 0

# ====================================================================
keyFrame5235 = CameraKeyFrame()
keyFrame5235.KeyTime = 0.5875
keyFrame5235.KeyValues = [0.0]
keyFrame5235.Position = [22.037988264444195, 20.0, 24.012057296130152]
keyFrame5235.FocalPoint = [20, 20, 20]
keyFrame5235.ViewUp = [0.4456949673444018, -0.866, -0.2263978972601206]
keyFrame5235.ViewAngle = 30.0
keyFrame5235.ParallelScale = 0.97681
keyFrame5235.PositionPathPoints = [22.037988264444195, 20.0, 24.012057296130152]
keyFrame5235.FocalPathPoints = [20, 20, 20]
keyFrame5235.PositionMode = 'Path'
keyFrame5235.FocalPointMode = 'Path'
keyFrame5235.ClosedFocalPath = 0
keyFrame5235.ClosedPositionPath = 0

# ====================================================================
keyFrame5236 = CameraKeyFrame()
keyFrame5236.KeyTime = 0.59
keyFrame5236.KeyValues = [0.0]
keyFrame5236.Position = [22.046008297704365, 20.0, 24.00797329834631]
keyFrame5236.FocalPoint = [20, 20, 20]
keyFrame5236.ViewUp = [0.44524128050743816, -0.866, -0.22728883288778665]
keyFrame5236.ViewAngle = 30.0
keyFrame5236.ParallelScale = 0.97681
keyFrame5236.PositionPathPoints = [22.046008297704365, 20.0, 24.00797329834631]
keyFrame5236.FocalPathPoints = [20, 20, 20]
keyFrame5236.PositionMode = 'Path'
keyFrame5236.FocalPointMode = 'Path'
keyFrame5236.ClosedFocalPath = 0
keyFrame5236.ClosedPositionPath = 0

# ====================================================================
keyFrame5237 = CameraKeyFrame()
keyFrame5237.KeyTime = 0.5925
keyFrame5237.KeyValues = [0.0]
keyFrame5237.Position = [22.054020146933578, 20.0, 24.003873268688572]
keyFrame5237.FocalPoint = [20, 20, 20]
keyFrame5237.ViewUp = [0.4447858127061414, -0.866, -0.2281788593721143]
keyFrame5237.ViewAngle = 30.0
keyFrame5237.ParallelScale = 0.97681
keyFrame5237.PositionPathPoints = [22.054020146933578, 20.0, 24.003873268688572]
keyFrame5237.FocalPathPoints = [20, 20, 20]
keyFrame5237.PositionMode = 'Path'
keyFrame5237.FocalPointMode = 'Path'
keyFrame5237.ClosedFocalPath = 0
keyFrame5237.ClosedPositionPath = 0

# ====================================================================
keyFrame5238 = CameraKeyFrame()
keyFrame5238.KeyTime = 0.595
keyFrame5238.KeyValues = [0.0]
keyFrame5238.Position = [22.062023780084413, 20.0, 23.99975722355691]
keyFrame5238.FocalPoint = [20, 20, 20]
keyFrame5238.ViewUp = [0.4443285657620671, -0.866, -0.2290679731590798]
keyFrame5238.ViewAngle = 30.0
keyFrame5238.ParallelScale = 0.97681
keyFrame5238.PositionPathPoints = [22.062023780084413, 20.0, 23.99975722355691]
keyFrame5238.FocalPathPoints = [20, 20, 20]
keyFrame5238.PositionMode = 'Path'
keyFrame5238.FocalPointMode = 'Path'
keyFrame5238.ClosedFocalPath = 0
keyFrame5238.ClosedPositionPath = 0

# ====================================================================
keyFrame5239 = CameraKeyFrame()
keyFrame5239.KeyTime = 0.5975
keyFrame5239.KeyValues = [0.0]
keyFrame5239.Position = [22.070019165142323, 20.0, 23.995625179415274]
keyFrame5239.FocalPoint = [20, 20, 20]
keyFrame5239.ViewUp = [0.44386954150387636, -0.866, -0.22995617069867658]
keyFrame5239.ViewAngle = 30.0
keyFrame5239.ParallelScale = 0.97681
keyFrame5239.PositionPathPoints = [22.070019165142323, 20.0, 23.995625179415274]
keyFrame5239.FocalPathPoints = [20, 20, 20]
keyFrame5239.PositionMode = 'Path'
keyFrame5239.FocalPointMode = 'Path'
keyFrame5239.ClosedFocalPath = 0
keyFrame5239.ClosedPositionPath = 0

# ====================================================================
keyFrame5240 = CameraKeyFrame()
keyFrame5240.KeyTime = 0.6
keyFrame5240.KeyValues = [0.0]
keyFrame5240.Position = [22.07800627012576, 20.0, 23.99147715279155]
keyFrame5240.FocalPoint = [20, 20, 20]
keyFrame5240.ViewUp = [0.4434087417673295, -0.866, -0.2308434484449371]
keyFrame5240.ViewAngle = 30.0
keyFrame5240.ParallelScale = 0.97681
keyFrame5240.PositionPathPoints = [22.07800627012576, 20.0, 23.99147715279155]
keyFrame5240.FocalPathPoints = [20, 20, 20]
keyFrame5240.PositionMode = 'Path'
keyFrame5240.FocalPointMode = 'Path'
keyFrame5240.ClosedFocalPath = 0
keyFrame5240.ClosedPositionPath = 0

# ====================================================================
keyFrame5241 = CameraKeyFrame()
keyFrame5241.KeyTime = 0.6025
keyFrame5241.KeyValues = [0.0]
keyFrame5241.Position = [22.085985063086294, 20.0, 23.987313160277463]
keyFrame5241.FocalPoint = [20, 20, 20]
keyFrame5241.ViewUp = [0.44294616839527856, -0.866, -0.23172980285595549]
keyFrame5241.ViewAngle = 30.0
keyFrame5241.ParallelScale = 0.97681
keyFrame5241.PositionPathPoints = [22.085985063086294, 20.0, 23.987313160277463]
keyFrame5241.FocalPathPoints = [20, 20, 20]
keyFrame5241.PositionMode = 'Path'
keyFrame5241.FocalPointMode = 'Path'
keyFrame5241.ClosedFocalPath = 0
keyFrame5241.ClosedPositionPath = 0

# ====================================================================
keyFrame5242 = CameraKeyFrame()
keyFrame5242.KeyTime = 0.605
keyFrame5242.KeyValues = [0.0]
keyFrame5242.Position = [22.093955512108764, 20.0, 23.98313321852852]
keyFrame5242.FocalPoint = [20, 20, 20]
keyFrame5242.ViewUp = [0.4424818232376612, -0.866, -0.2326152303939097]
keyFrame5242.ViewAngle = 30.0
keyFrame5242.ParallelScale = 0.97681
keyFrame5242.PositionPathPoints = [22.093955512108764, 20.0, 23.98313321852852]
keyFrame5242.FocalPathPoints = [20, 20, 20]
keyFrame5242.PositionMode = 'Path'
keyFrame5242.FocalPointMode = 'Path'
keyFrame5242.ClosedFocalPath = 0
keyFrame5242.ClosedPositionPath = 0

# ====================================================================
keyFrame5243 = CameraKeyFrame()
keyFrame5243.KeyTime = 0.6075
keyFrame5243.KeyValues = [0.0]
keyFrame5243.Position = [22.101917585311377, 20.0, 23.97893734426393]
keyFrame5243.FocalPoint = [20, 20, 20]
keyFrame5243.ViewUp = [0.44201570815149366, -0.866, -0.23349972752508358]
keyFrame5243.ViewAngle = 30.0
keyFrame5243.ParallelScale = 0.97681
keyFrame5243.PositionPathPoints = [22.101917585311377, 20.0, 23.97893734426393]
keyFrame5243.FocalPathPoints = [20, 20, 20]
keyFrame5243.PositionMode = 'Path'
keyFrame5243.FocalPointMode = 'Path'
keyFrame5243.ClosedFocalPath = 0
keyFrame5243.ClosedPositionPath = 0

# ====================================================================
keyFrame5244 = CameraKeyFrame()
keyFrame5244.KeyTime = 0.61
keyFrame5244.KeyValues = [0.0]
keyFrame5244.Position = [22.109871250845863, 20.0, 23.974725554266545]
keyFrame5244.FocalPoint = [20, 20, 20]
keyFrame5244.ViewUp = [0.4415478250008636, -0.866, -0.23438329071988942]
keyFrame5244.ViewAngle = 30.0
keyFrame5244.ParallelScale = 0.97681
keyFrame5244.PositionPathPoints = [22.109871250845863, 20.0, 23.974725554266545]
keyFrame5244.FocalPathPoints = [20, 20, 20]
keyFrame5244.PositionMode = 'Path'
keyFrame5244.FocalPointMode = 'Path'
keyFrame5244.ClosedFocalPath = 0
keyFrame5244.ClosedPositionPath = 0

# ====================================================================
keyFrame5245 = CameraKeyFrame()
keyFrame5245.KeyTime = 0.6125
keyFrame5245.KeyValues = [0.0]
keyFrame5245.Position = [22.117816476897584, 20.0, 23.97049786538278]
keyFrame5245.FocalPoint = [20, 20, 20]
keyFrame5245.ViewUp = [0.441078175656924, -0.866, -0.23526591645289005]
keyFrame5245.ViewAngle = 30.0
keyFrame5245.ParallelScale = 0.97681
keyFrame5245.PositionPathPoints = [22.117816476897584, 20.0, 23.97049786538278]
keyFrame5245.FocalPathPoints = [20, 20, 20]
keyFrame5245.PositionMode = 'Path'
keyFrame5245.FocalPointMode = 'Path'
keyFrame5245.ClosedFocalPath = 0
keyFrame5245.ClosedPositionPath = 0

# ====================================================================
keyFrame5246 = CameraKeyFrame()
keyFrame5246.KeyTime = 0.615
keyFrame5246.KeyValues = [0.0]
keyFrame5246.Position = [22.125753231685678, 20.0, 23.96625429452254]
keyFrame5246.FocalPoint = [20, 20, 20]
keyFrame5246.ViewUp = [0.44060676199788573, -0.866, -0.23614760120282116]
keyFrame5246.ViewAngle = 30.0
keyFrame5246.ParallelScale = 0.97681
keyFrame5246.PositionPathPoints = [22.125753231685678, 20.0, 23.96625429452254]
keyFrame5246.FocalPathPoints = [20, 20, 20]
keyFrame5246.PositionMode = 'Path'
keyFrame5246.FocalPointMode = 'Path'
keyFrame5246.ClosedFocalPath = 0
keyFrame5246.ClosedPositionPath = 0

# ====================================================================
keyFrame5247 = CameraKeyFrame()
keyFrame5247.KeyTime = 0.6175
keyFrame5247.KeyValues = [0.0]
keyFrame5247.Position = [22.133681483463167, 20.0, 23.961994858659157]
keyFrame5247.FocalPoint = [20, 20, 20]
keyFrame5247.ViewUp = [0.44013358590901114, -0.866, -0.23702834145261348]
keyFrame5247.ViewAngle = 30.0
keyFrame5247.ParallelScale = 0.97681
keyFrame5247.PositionPathPoints = [22.133681483463167, 20.0, 23.961994858659157]
keyFrame5247.FocalPathPoints = [20, 20, 20]
keyFrame5247.PositionMode = 'Path'
keyFrame5247.FocalPointMode = 'Path'
keyFrame5247.ClosedFocalPath = 0
keyFrame5247.ClosedPositionPath = 0

# ====================================================================
keyFrame5248 = CameraKeyFrame()
keyFrame5248.KeyTime = 0.62
keyFrame5248.KeyValues = [0.0]
keyFrame5248.Position = [22.141601200517115, 20.0, 23.957719574829305]
keyFrame5248.FocalPoint = [20, 20, 20]
keyFrame5248.ViewUp = [0.4396586492826072, -0.866, -0.23790813368941519]
keyFrame5248.ViewAngle = 30.0
keyFrame5248.ParallelScale = 0.97681
keyFrame5248.PositionPathPoints = [22.141601200517115, 20.0, 23.957719574829305]
keyFrame5248.FocalPathPoints = [20, 20, 20]
keyFrame5248.PositionMode = 'Path'
keyFrame5248.FocalPointMode = 'Path'
keyFrame5248.ClosedFocalPath = 0
keyFrame5248.ClosedPositionPath = 0

# ====================================================================
keyFrame5249 = CameraKeyFrame()
keyFrame5249.KeyTime = 0.6225
keyFrame5249.KeyValues = [0.0]
keyFrame5249.Position = [22.149512351168717, 20.0, 23.95342846013294]
keyFrame5249.FocalPoint = [20, 20, 20]
keyFrame5249.ViewUp = [0.4391819540180185, -0.866, -0.238786974404614]
keyFrame5249.ViewAngle = 30.0
keyFrame5249.ParallelScale = 0.97681
keyFrame5249.PositionPathPoints = [22.149512351168717, 20.0, 23.95342846013294]
keyFrame5249.FocalPathPoints = [20, 20, 20]
keyFrame5249.PositionMode = 'Path'
keyFrame5249.FocalPointMode = 'Path'
keyFrame5249.ClosedFocalPath = 0
keyFrame5249.ClosedPositionPath = 0

# ====================================================================
keyFrame5250 = CameraKeyFrame()
keyFrame5250.KeyTime = 0.625
keyFrame5250.KeyValues = [0.0]
keyFrame5250.Position = [22.157414903773464, 20.0, 23.949121531733212]
keyFrame5250.FocalPoint = [20, 20, 20]
keyFrame5250.ViewUp = [0.4387035020216209, -0.866, -0.23966486009385962]
keyFrame5250.ViewAngle = 30.0
keyFrame5250.ParallelScale = 0.97681
keyFrame5250.PositionPathPoints = [22.157414903773464, 20.0, 23.949121531733212]
keyFrame5250.FocalPathPoints = [20, 20, 20]
keyFrame5250.PositionMode = 'Path'
keyFrame5250.FocalPointMode = 'Path'
keyFrame5250.ClosedFocalPath = 0
keyFrame5250.ClosedPositionPath = 0

# ====================================================================
keyFrame5251 = CameraKeyFrame()
keyFrame5251.KeyTime = 0.6275
keyFrame5251.KeyValues = [0.0]
keyFrame5251.Position = [22.165308826721244, 20.0, 23.94479880685641]
keyFrame5251.FocalPoint = [20, 20, 20]
keyFrame5251.ViewUp = [0.43822329520813413, -0.866, -0.2405417871991468]
keyFrame5251.ViewAngle = 30.0
keyFrame5251.ParallelScale = 0.97681
keyFrame5251.PositionPathPoints = [22.165308826721244, 20.0, 23.94479880685641]
keyFrame5251.FocalPathPoints = [20, 20, 20]
keyFrame5251.PositionMode = 'Path'
keyFrame5251.FocalPointMode = 'Path'
keyFrame5251.ClosedFocalPath = 0
keyFrame5251.ClosedPositionPath = 0

# ====================================================================
keyFrame5252 = CameraKeyFrame()
keyFrame5252.KeyTime = 0.63
keyFrame5252.KeyValues = [0.0]
keyFrame5252.Position = [22.173194088436478, 20.0, 23.94046030279187]
keyFrame5252.FocalPoint = [20, 20, 20]
keyFrame5252.ViewUp = [0.4377413354995338, -0.866, -0.24141775215632771]
keyFrame5252.ViewAngle = 30.0
keyFrame5252.ParallelScale = 0.97681
keyFrame5252.PositionPathPoints = [22.173194088436478, 20.0, 23.94046030279187]
keyFrame5252.FocalPathPoints = [20, 20, 20]
keyFrame5252.PositionMode = 'Path'
keyFrame5252.FocalPointMode = 'Path'
keyFrame5252.ClosedFocalPath = 0
keyFrame5252.ClosedPositionPath = 0

# ====================================================================
keyFrame5253 = CameraKeyFrame()
keyFrame5253.KeyTime = 0.6325
keyFrame5253.KeyValues = [0.0]
keyFrame5253.Position = [22.18107065737826, 20.0, 23.936106036891914]
keyFrame5253.FocalPoint = [20, 20, 20]
keyFrame5253.ViewUp = [0.437257624823535, -0.866, -0.24229275146136334]
keyFrame5253.ViewAngle = 30.0
keyFrame5253.ParallelScale = 0.97681
keyFrame5253.PositionPathPoints = [22.18107065737826, 20.0, 23.936106036891914]
keyFrame5253.FocalPathPoints = [20, 20, 20]
keyFrame5253.PositionMode = 'Path'
keyFrame5253.FocalPointMode = 'Path'
keyFrame5253.ClosedFocalPath = 0
keyFrame5253.ClosedPositionPath = 0

# ====================================================================
keyFrame5254 = CameraKeyFrame()
keyFrame5254.KeyTime = 0.635
keyFrame5254.KeyValues = [0.0]
keyFrame5254.Position = [22.18893850204046, 20.0, 23.931736026571762]
keyFrame5254.FocalPoint = [20, 20, 20]
keyFrame5254.ViewUp = [0.4367721651148694, -0.866, -0.24316678161400954]
keyFrame5254.ViewAngle = 30.0
keyFrame5254.ParallelScale = 0.97681
keyFrame5254.PositionPathPoints = [22.18893850204046, 20.0, 23.931736026571762]
keyFrame5254.FocalPathPoints = [20, 20, 20]
keyFrame5254.PositionMode = 'Path'
keyFrame5254.FocalPointMode = 'Path'
keyFrame5254.ClosedFocalPath = 0
keyFrame5254.ClosedPositionPath = 0

# ====================================================================
keyFrame5255 = CameraKeyFrame()
keyFrame5255.KeyTime = 0.6375
keyFrame5255.KeyValues = [0.0]
keyFrame5255.Position = [22.196797590951874, 20.0, 23.92735028930948]
keyFrame5255.FocalPoint = [20, 20, 20]
keyFrame5255.ViewUp = [0.4362849583152787, -0.866, -0.2440398391178234]
keyFrame5255.ViewAngle = 30.0
keyFrame5255.ParallelScale = 0.97681
keyFrame5255.PositionPathPoints = [22.196797590951874, 20.0, 23.92735028930948]
keyFrame5255.FocalPathPoints = [20, 20, 20]
keyFrame5255.PositionMode = 'Path'
keyFrame5255.FocalPointMode = 'Path'
keyFrame5255.ClosedFocalPath = 0
keyFrame5255.ClosedPositionPath = 0

# ====================================================================
keyFrame5256 = CameraKeyFrame()
keyFrame5256.KeyTime = 0.64
keyFrame5256.KeyValues = [0.0]
keyFrame5256.Position = [22.204647892676334, 20.0, 23.922948842645877]
keyFrame5256.FocalPoint = [20, 20, 20]
keyFrame5256.ViewUp = [0.4357960063735082, -0.866, -0.24491192048017513]
keyFrame5256.ViewAngle = 30.0
keyFrame5256.ParallelScale = 0.97681
keyFrame5256.PositionPathPoints = [22.204647892676334, 20.0, 23.922948842645877]
keyFrame5256.FocalPathPoints = [20, 20, 20]
keyFrame5256.PositionMode = 'Path'
keyFrame5256.FocalPointMode = 'Path'
keyFrame5256.ClosedFocalPath = 0
keyFrame5256.ClosedPositionPath = 0

# ====================================================================
keyFrame5257 = CameraKeyFrame()
keyFrame5257.KeyTime = 0.6425
keyFrame5257.KeyValues = [0.0]
keyFrame5257.Position = [22.21248937581285, 20.0, 23.918531704184446]
keyFrame5257.FocalPoint = [20, 20, 20]
keyFrame5257.ViewUp = [0.43530531124530014, -0.866, -0.2457830222122604]
keyFrame5257.ViewAngle = 30.0
keyFrame5257.ParallelScale = 0.97681
keyFrame5257.PositionPathPoints = [22.21248937581285, 20.0, 23.918531704184446]
keyFrame5257.FocalPathPoints = [20, 20, 20]
keyFrame5257.PositionMode = 'Path'
keyFrame5257.FocalPointMode = 'Path'
keyFrame5257.ClosedFocalPath = 0
keyFrame5257.ClosedPositionPath = 0

# ====================================================================
keyFrame5258 = CameraKeyFrame()
keyFrame5258.KeyTime = 0.645
keyFrame5258.KeyValues = [0.0]
keyFrame5258.Position = [22.22032200899572, 20.0, 23.914098891591287]
keyFrame5258.FocalPoint = [20, 20, 20]
keyFrame5258.ViewUp = [0.4348128748933871, -0.866, -0.24665314082911213]
keyFrame5258.ViewAngle = 30.0
keyFrame5258.ParallelScale = 0.97681
keyFrame5258.PositionPathPoints = [22.22032200899572, 20.0, 23.914098891591287]
keyFrame5258.FocalPathPoints = [20, 20, 20]
keyFrame5258.PositionMode = 'Path'
keyFrame5258.FocalPointMode = 'Path'
keyFrame5258.ClosedFocalPath = 0
keyFrame5258.ClosedPositionPath = 0

# ====================================================================
keyFrame5259 = CameraKeyFrame()
keyFrame5259.KeyTime = 0.6475
keyFrame5259.KeyValues = [0.0]
keyFrame5259.Position = [22.22814576089467, 20.0, 23.909650422595035]
keyFrame5259.FocalPoint = [20, 20, 20]
keyFrame5259.ViewUp = [0.4343186992874855, -0.866, -0.24752227284961303]
keyFrame5259.ViewAngle = 30.0
keyFrame5259.ParallelScale = 0.97681
keyFrame5259.PositionPathPoints = [22.22814576089467, 20.0, 23.909650422595035]
keyFrame5259.FocalPathPoints = [20, 20, 20]
keyFrame5259.PositionMode = 'Path'
keyFrame5259.FocalPointMode = 'Path'
keyFrame5259.ClosedFocalPath = 0
keyFrame5259.ClosedPositionPath = 0

# ====================================================================
keyFrame5260 = CameraKeyFrame()
keyFrame5260.KeyTime = 0.65
keyFrame5260.KeyValues = [0.0]
keyFrame5260.Position = [22.235960600214973, 20.0, 23.90518631498676]
keyFrame5260.FocalPoint = [20, 20, 20]
keyFrame5260.ViewUp = [0.43382278640428906, -0.866, -0.24839041479650728]
keyFrame5260.ViewAngle = 30.0
keyFrame5260.ParallelScale = 0.97681
keyFrame5260.PositionPathPoints = [22.235960600214973, 20.0, 23.90518631498676]
keyFrame5260.FocalPathPoints = [20, 20, 20]
keyFrame5260.PositionMode = 'Path'
keyFrame5260.FocalPointMode = 'Path'
keyFrame5260.ClosedFocalPath = 0
keyFrame5260.ClosedPositionPath = 0

# ====================================================================
keyFrame5261 = CameraKeyFrame()
keyFrame5261.KeyTime = 0.6525
keyFrame5261.KeyValues = [0.0]
keyFrame5261.Position = [22.243766495697592, 20.0, 23.900706586619926]
keyFrame5261.FocalPoint = [20, 20, 20]
keyFrame5261.ViewUp = [0.43332513822746216, -0.866, -0.249257563196413]
keyFrame5261.ViewAngle = 30.0
keyFrame5261.ParallelScale = 0.97681
keyFrame5261.PositionPathPoints = [22.243766495697592, 20.0, 23.900706586619926]
keyFrame5261.FocalPathPoints = [20, 20, 20]
keyFrame5261.PositionMode = 'Path'
keyFrame5261.FocalPointMode = 'Path'
keyFrame5261.ClosedFocalPath = 0
keyFrame5261.ClosedPositionPath = 0

# ====================================================================
keyFrame5262 = CameraKeyFrame()
keyFrame5262.KeyTime = 0.655
keyFrame5262.KeyValues = [0.0]
keyFrame5262.Position = [22.251563416119275, 20.0, 23.89621125541028]
keyFrame5262.FocalPoint = [20, 20, 20]
keyFrame5262.ViewUp = [0.43282575674763335, -0.866, -0.2501237145798341]
keyFrame5262.ViewAngle = 30.0
keyFrame5262.ParallelScale = 0.97681
keyFrame5262.PositionPathPoints = [22.251563416119275, 20.0, 23.89621125541028]
keyFrame5262.FocalPathPoints = [20, 20, 20]
keyFrame5262.PositionMode = 'Path'
keyFrame5262.FocalPointMode = 'Path'
keyFrame5262.ClosedFocalPath = 0
keyFrame5262.ClosedPositionPath = 0

# ====================================================================
keyFrame5263 = CameraKeyFrame()
keyFrame5263.KeyTime = 0.6575
keyFrame5263.KeyValues = [0.0]
keyFrame5263.Position = [22.259351330292713, 20.0, 23.891700339335795]
keyFrame5263.FocalPoint = [20, 20, 20]
keyFrame5263.ViewUp = [0.43232464396238884, -0.866, -0.25098886548117266]
keyFrame5263.ViewAngle = 30.0
keyFrame5263.ParallelScale = 0.97681
keyFrame5263.PositionPathPoints = [22.259351330292713, 20.0, 23.891700339335795]
keyFrame5263.FocalPathPoints = [20, 20, 20]
keyFrame5263.PositionMode = 'Path'
keyFrame5263.FocalPointMode = 'Path'
keyFrame5263.ClosedFocalPath = 0
keyFrame5263.ClosedPositionPath = 0

# ====================================================================
keyFrame5264 = CameraKeyFrame()
keyFrame5264.KeyTime = 0.66
keyFrame5264.KeyValues = [0.0]
keyFrame5264.Position = [22.26713020706665, 20.0, 23.887173856436597]
keyFrame5264.FocalPoint = [20, 20, 20]
keyFrame5264.ViewUp = [0.4318218018762658, -0.866, -0.25185301243874064]
keyFrame5264.ViewAngle = 30.0
keyFrame5264.ParallelScale = 0.97681
keyFrame5264.PositionPathPoints = [22.26713020706665, 20.0, 23.887173856436597]
keyFrame5264.FocalPathPoints = [20, 20, 20]
keyFrame5264.PositionMode = 'Path'
keyFrame5264.FocalPointMode = 'Path'
keyFrame5264.ClosedFocalPath = 0
keyFrame5264.ClosedPositionPath = 0

# ====================================================================
keyFrame5265 = CameraKeyFrame()
keyFrame5265.KeyTime = 0.6625
keyFrame5265.KeyValues = [0.0]
keyFrame5265.Position = [22.274900015326004, 20.0, 23.882631824814855]
keyFrame5265.FocalPoint = [20, 20, 20]
keyFrame5265.ViewUp = [0.4313172325007458, -0.866, -0.2527161519947725]
keyFrame5265.ViewAngle = 30.0
keyFrame5265.ParallelScale = 0.97681
keyFrame5265.PositionPathPoints = [22.274900015326004, 20.0, 23.882631824814855]
keyFrame5265.FocalPathPoints = [20, 20, 20]
keyFrame5265.PositionMode = 'Path'
keyFrame5265.FocalPointMode = 'Path'
keyFrame5265.ClosedFocalPath = 0
keyFrame5265.ClosedPositionPath = 0

# ====================================================================
keyFrame5266 = CameraKeyFrame()
keyFrame5266.KeyTime = 0.665
keyFrame5266.KeyValues = [0.0]
keyFrame5266.Position = [22.282660723992013, 20.0, 23.878074262634744]
keyFrame5266.FocalPoint = [20, 20, 20]
keyFrame5266.ViewUp = [0.43081093785424845, -0.866, -0.2535782806954369]
keyFrame5266.ViewAngle = 30.0
keyFrame5266.ParallelScale = 0.97681
keyFrame5266.PositionPathPoints = [22.282660723992013, 20.0, 23.878074262634744]
keyFrame5266.FocalPathPoints = [20, 20, 20]
keyFrame5266.PositionMode = 'Path'
keyFrame5266.FocalPointMode = 'Path'
keyFrame5266.ClosedFocalPath = 0
keyFrame5266.ClosedPositionPath = 0

# ====================================================================
keyFrame5267 = CameraKeyFrame()
keyFrame5267.KeyTime = 0.6675
keyFrame5267.KeyValues = [0.0]
keyFrame5267.Position = [22.290412302022347, 20.0, 23.873501188122336]
keyFrame5267.FocalPoint = [20, 20, 20]
keyFrame5267.ViewUp = [0.4303029199621247, -0.866, -0.25443939509084906]
keyFrame5267.ViewAngle = 30.0
keyFrame5267.ParallelScale = 0.97681
keyFrame5267.PositionPathPoints = [22.290412302022347, 20.0, 23.873501188122336]
keyFrame5267.FocalPathPoints = [20, 20, 20]
keyFrame5267.PositionMode = 'Path'
keyFrame5267.FocalPointMode = 'Path'
keyFrame5267.ClosedFocalPath = 0
keyFrame5267.ClosedPositionPath = 0

# ====================================================================
keyFrame5268 = CameraKeyFrame()
keyFrame5268.KeyTime = 0.67
keyFrame5268.KeyValues = [0.0]
keyFrame5268.Position = [22.298154718408206, 20.0, 23.868912619585487]
keyFrame5268.FocalPoint = [20, 20, 20]
keyFrame5268.ViewUp = [0.4297931808566502, -0.866, -0.2552994917350827]
keyFrame5268.ViewAngle = 30.0
keyFrame5268.ParallelScale = 0.97681
keyFrame5268.PositionPathPoints = [22.298154718408206, 20.0, 23.868912619585487]
keyFrame5268.FocalPathPoints = [20, 20, 20]
keyFrame5268.PositionMode = 'Path'
keyFrame5268.FocalPointMode = 'Path'
keyFrame5268.ClosedFocalPath = 0
keyFrame5268.ClosedPositionPath = 0

# ====================================================================
keyFrame5269 = CameraKeyFrame()
keyFrame5269.KeyTime = 0.6725
keyFrame5269.KeyValues = [0.0]
keyFrame5269.Position = [22.305887942175705, 20.0, 23.864308575405634]
keyFrame5269.FocalPoint = [20, 20, 20]
keyFrame5269.ViewUp = [0.4292817225770189, -0.866, -0.25615856718618235]
keyFrame5269.ViewAngle = 30.0
keyFrame5269.ParallelScale = 0.97681
keyFrame5269.PositionPathPoints = [22.305887942175705, 20.0, 23.864308575405634]
keyFrame5269.FocalPathPoints = [20, 20, 20]
keyFrame5269.PositionMode = 'Path'
keyFrame5269.FocalPointMode = 'Path'
keyFrame5269.ClosedFocalPath = 0
keyFrame5269.ClosedPositionPath = 0

# ====================================================================
keyFrame5270 = CameraKeyFrame()
keyFrame5270.KeyTime = 0.675
keyFrame5270.KeyValues = [0.0]
keyFrame5270.Position = [22.313611942391788, 20.0, 23.85968907399924]
keyFrame5270.FocalPoint = [20, 20, 20]
keyFrame5270.ViewUp = [0.4287685471693364, -0.866, -0.25701661800617526]
keyFrame5270.ViewAngle = 30.0
keyFrame5270.ParallelScale = 0.97681
keyFrame5270.PositionPathPoints = [22.313611942391788, 20.0, 23.85968907399924]
keyFrame5270.FocalPathPoints = [20, 20, 20]
keyFrame5270.PositionMode = 'Path'
keyFrame5270.FocalPointMode = 'Path'
keyFrame5270.ClosedFocalPath = 0
keyFrame5270.ClosedPositionPath = 0

# ====================================================================
keyFrame5271 = CameraKeyFrame()
keyFrame5271.KeyTime = 0.6775
keyFrame5271.KeyValues = [0.0]
keyFrame5271.Position = [22.321326688160333, 20.0, 23.85505413384437]
keyFrame5271.FocalPoint = [20, 20, 20]
keyFrame5271.ViewUp = [0.42825365668661336, -0.866, -0.2578736407610836]
keyFrame5271.ViewAngle = 30.0
keyFrame5271.ParallelScale = 0.97681
keyFrame5271.PositionPathPoints = [22.321326688160333, 20.0, 23.85505413384437]
keyFrame5271.FocalPathPoints = [20, 20, 20]
keyFrame5271.PositionMode = 'Path'
keyFrame5271.FocalPointMode = 'Path'
keyFrame5271.ClosedFocalPath = 0
keyFrame5271.ClosedPositionPath = 0

# ====================================================================
keyFrame5272 = CameraKeyFrame()
keyFrame5272.KeyTime = 0.68
keyFrame5272.KeyValues = [0.0]
keyFrame5272.Position = [22.32903214862225, 20.0, 23.850403773480828]
keyFrame5272.FocalPoint = [20, 20, 20]
keyFrame5272.ViewUp = [0.42773705318875904, -0.866, -0.2587296320209367]
keyFrame5272.ViewAngle = 30.0
keyFrame5272.ParallelScale = 0.97681
keyFrame5272.PositionPathPoints = [22.32903214862225, 20.0, 23.850403773480828]
keyFrame5272.FocalPathPoints = [20, 20, 20]
keyFrame5272.PositionMode = 'Path'
keyFrame5272.FocalPointMode = 'Path'
keyFrame5272.ClosedFocalPath = 0
keyFrame5272.ClosedPositionPath = 0

# ====================================================================
keyFrame5273 = CameraKeyFrame()
keyFrame5273.KeyTime = 0.6825
keyFrame5273.KeyValues = [0.0]
keyFrame5273.Position = [22.3367282929556, 20.0, 23.845738011510093]
keyFrame5273.FocalPoint = [20, 20, 20]
keyFrame5273.ViewUp = [0.4272187387425747, -0.866, -0.25958458835978293]
keyFrame5273.ViewAngle = 30.0
keyFrame5273.ParallelScale = 0.97681
keyFrame5273.PositionPathPoints = [22.3367282929556, 20.0, 23.845738011510093]
keyFrame5273.FocalPathPoints = [20, 20, 20]
keyFrame5273.PositionMode = 'Path'
keyFrame5273.FocalPointMode = 'Path'
keyFrame5273.ClosedFocalPath = 0
keyFrame5273.ClosedPositionPath = 0

# ====================================================================
keyFrame5274 = CameraKeyFrame()
keyFrame5274.KeyTime = 0.685
keyFrame5274.KeyValues = [0.0]
keyFrame5274.Position = [22.34441509037571, 20.0, 23.841056866595245]
keyFrame5274.FocalPoint = [20, 20, 20]
keyFrame5274.ViewUp = [0.426698715421747, -0.866, -0.2604385063557019]
keyFrame5274.ViewAngle = 30.0
keyFrame5274.ParallelScale = 0.97681
keyFrame5274.PositionPathPoints = [22.34441509037571, 20.0, 23.841056866595245]
keyFrame5274.FocalPathPoints = [20, 20, 20]
keyFrame5274.PositionMode = 'Path'
keyFrame5274.FocalPointMode = 'Path'
keyFrame5274.ClosedFocalPath = 0
keyFrame5274.ClosedPositionPath = 0

# ====================================================================
keyFrame5275 = CameraKeyFrame()
keyFrame5275.KeyTime = 0.6875
keyFrame5275.KeyValues = [0.0]
keyFrame5275.Position = [22.352092510135314, 20.0, 23.836360357460883]
keyFrame5275.FocalPoint = [20, 20, 20]
keyFrame5275.ViewUp = [0.42617698530684145, -0.866, -0.26129138259081686]
keyFrame5275.ViewAngle = 30.0
keyFrame5275.ParallelScale = 0.97681
keyFrame5275.PositionPathPoints = [22.352092510135314, 20.0, 23.836360357460883]
keyFrame5275.FocalPathPoints = [20, 20, 20]
keyFrame5275.PositionMode = 'Path'
keyFrame5275.FocalPointMode = 'Path'
keyFrame5275.ClosedFocalPath = 0
keyFrame5275.ClosedPositionPath = 0

# ====================================================================
keyFrame5276 = CameraKeyFrame()
keyFrame5276.KeyTime = 0.69
keyFrame5276.KeyValues = [0.0]
keyFrame5276.Position = [22.35976052152467, 20.0, 23.831648502893064]
keyFrame5276.FocalPoint = [20, 20, 20]
keyFrame5276.ViewUp = [0.42565355048529596, -0.866, -0.26214321365130616]
keyFrame5276.ViewAngle = 30.0
keyFrame5276.ParallelScale = 0.97681
keyFrame5276.PositionPathPoints = [22.35976052152467, 20.0, 23.831648502893064]
keyFrame5276.FocalPathPoints = [20, 20, 20]
keyFrame5276.PositionMode = 'Path'
keyFrame5276.FocalPointMode = 'Path'
keyFrame5276.ClosedFocalPath = 0
keyFrame5276.ClosedPositionPath = 0

# ====================================================================
keyFrame5277 = CameraKeyFrame()
keyFrame5277.KeyTime = 0.6925
keyFrame5277.KeyValues = [0.0]
keyFrame5277.Position = [22.367419093871675, 20.0, 23.826921321739203]
keyFrame5277.FocalPoint = [20, 20, 20]
keyFrame5277.ViewUp = [0.425128413051414, -0.866, -0.2629939961274161]
keyFrame5277.ViewAngle = 30.0
keyFrame5277.ParallelScale = 0.97681
keyFrame5277.PositionPathPoints = [22.367419093871675, 20.0, 23.826921321739203]
keyFrame5277.FocalPathPoints = [20, 20, 20]
keyFrame5277.PositionMode = 'Path'
keyFrame5277.FocalPointMode = 'Path'
keyFrame5277.ClosedFocalPath = 0
keyFrame5277.ClosedPositionPath = 0

# ====================================================================
keyFrame5278 = CameraKeyFrame()
keyFrame5278.KeyTime = 0.695
keyFrame5278.KeyValues = [0.0]
keyFrame5278.Position = [22.375068196542003, 20.0, 23.82217883290802]
keyFrame5278.FocalPoint = [20, 20, 20]
keyFrame5278.ViewUp = [0.4246015751063585, -0.866, -0.26384372661347255]
keyFrame5278.ViewAngle = 30.0
keyFrame5278.ParallelScale = 0.97681
keyFrame5278.PositionPathPoints = [22.375068196542003, 20.0, 23.82217883290802]
keyFrame5278.FocalPathPoints = [20, 20, 20]
keyFrame5278.PositionMode = 'Path'
keyFrame5278.FocalPointMode = 'Path'
keyFrame5278.ClosedFocalPath = 0
keyFrame5278.ClosedPositionPath = 0

# ====================================================================
keyFrame5279 = CameraKeyFrame()
keyFrame5279.KeyTime = 0.6975
keyFrame5279.KeyValues = [0.0]
keyFrame5279.Position = [22.382707798939215, 20.0, 23.817421055369447]
keyFrame5279.FocalPoint = [20, 20, 20]
keyFrame5279.ViewUp = [0.4240730387581447, -0.866, -0.2646924017078932]
keyFrame5279.ViewAngle = 30.0
keyFrame5279.ParallelScale = 0.97681
keyFrame5279.PositionPathPoints = [22.382707798939215, 20.0, 23.817421055369447]
keyFrame5279.FocalPathPoints = [20, 20, 20]
keyFrame5279.PositionMode = 'Path'
keyFrame5279.FocalPointMode = 'Path'
keyFrame5279.ClosedFocalPath = 0
keyFrame5279.ClosedPositionPath = 0

# ====================================================================
keyFrame5280 = CameraKeyFrame()
keyFrame5280.KeyTime = 0.7
keyFrame5280.KeyValues = [0.0]
keyFrame5280.Position = [22.3903378705049, 20.0, 23.812648008154568]
keyFrame5280.FocalPoint = [20, 20, 20]
keyFrame5280.ViewUp = [0.42354280612163425, -0.866, -0.26554001801319976]
keyFrame5280.ViewAngle = 30.0
keyFrame5280.ParallelScale = 0.97681
keyFrame5280.PositionPathPoints = [22.3903378705049, 20.0, 23.812648008154568]
keyFrame5280.FocalPathPoints = [20, 20, 20]
keyFrame5280.PositionMode = 'Path'
keyFrame5280.FocalPointMode = 'Path'
keyFrame5280.ClosedFocalPath = 0
keyFrame5280.ClosedPositionPath = 0

# ====================================================================
keyFrame5281 = CameraKeyFrame()
keyFrame5281.KeyTime = 0.7025
keyFrame5281.KeyValues = [0.0]
keyFrame5281.Position = [22.397958380718787, 20.0, 23.807859710355523]
keyFrame5281.FocalPoint = [20, 20, 20]
keyFrame5281.ViewUp = [0.42301087931852793, -0.866, -0.26638657213603006]
keyFrame5281.ViewAngle = 30.0
keyFrame5281.ParallelScale = 0.97681
keyFrame5281.PositionPathPoints = [22.397958380718787, 20.0, 23.807859710355523]
keyFrame5281.FocalPathPoints = [20, 20, 20]
keyFrame5281.PositionMode = 'Path'
keyFrame5281.FocalPointMode = 'Path'
keyFrame5281.ClosedFocalPath = 0
keyFrame5281.ClosedPositionPath = 0

# ====================================================================
keyFrame5282 = CameraKeyFrame()
keyFrame5282.KeyTime = 0.705
keyFrame5282.KeyValues = [0.0]
keyFrame5282.Position = [22.405569299098858, 20.0, 23.80305618112545]
keyFrame5282.FocalPoint = [20, 20, 20]
keyFrame5282.ViewUp = [0.4224772604773598, -0.866, -0.26723206068714994]
keyFrame5282.ViewAngle = 30.0
keyFrame5282.ParallelScale = 0.97681
keyFrame5282.PositionPathPoints = [22.405569299098858, 20.0, 23.80305618112545]
keyFrame5282.FocalPathPoints = [20, 20, 20]
keyFrame5282.PositionMode = 'Path'
keyFrame5282.FocalPointMode = 'Path'
keyFrame5282.ClosedFocalPath = 0
keyFrame5282.ClosedPositionPath = 0

# ====================================================================
keyFrame5283 = CameraKeyFrame()
keyFrame5283.KeyTime = 0.7075
keyFrame5283.KeyValues = [0.0]
keyFrame5283.Position = [22.413170595201496, 20.0, 23.79823743967839]
keyFrame5283.FocalPoint = [20, 20, 20]
keyFrame5283.ViewUp = [0.42194195173349003, -0.866, -0.26807648028146575]
keyFrame5283.ViewAngle = 30.0
keyFrame5283.ParallelScale = 0.97681
keyFrame5283.PositionPathPoints = [22.413170595201496, 20.0, 23.79823743967839]
keyFrame5283.FocalPathPoints = [20, 20, 20]
keyFrame5283.PositionMode = 'Path'
keyFrame5283.FocalPointMode = 'Path'
keyFrame5283.ClosedFocalPath = 0
keyFrame5283.ClosedPositionPath = 0

# ====================================================================
keyFrame5284 = CameraKeyFrame()
keyFrame5284.KeyTime = 0.71
keyFrame5284.KeyValues = [0.0]
keyFrame5284.Position = [22.42076223862159, 20.0, 23.793403505289213]
keyFrame5284.FocalPoint = [20, 20, 20]
keyFrame5284.ViewUp = [0.4214049552290989, -0.866, -0.268919827538036]
keyFrame5284.ViewAngle = 30.0
keyFrame5284.ParallelScale = 0.97681
keyFrame5284.PositionPathPoints = [22.42076223862159, 20.0, 23.793403505289213]
keyFrame5284.FocalPathPoints = [20, 20, 20]
keyFrame5284.PositionMode = 'Path'
keyFrame5284.FocalPointMode = 'Path'
keyFrame5284.ClosedFocalPath = 0
keyFrame5284.ClosedPositionPath = 0

# ====================================================================
keyFrame5285 = CameraKeyFrame()
keyFrame5285.KeyTime = 0.7125
keyFrame5285.KeyValues = [0.0]
keyFrame5285.Position = [22.42834419899267, 20.0, 23.788554397293566]
keyFrame5285.FocalPoint = [20, 20, 20]
keyFrame5285.ViewUp = [0.4208662731131797, -0.866, -0.2697620990800839]
keyFrame5285.ViewAngle = 30.0
keyFrame5285.ParallelScale = 0.97681
keyFrame5285.PositionPathPoints = [22.42834419899267, 20.0, 23.788554397293566]
keyFrame5285.FocalPathPoints = [20, 20, 20]
keyFrame5285.PositionMode = 'Path'
keyFrame5285.FocalPointMode = 'Path'
keyFrame5285.ClosedFocalPath = 0
keyFrame5285.ClosedPositionPath = 0

# ====================================================================
keyFrame5286 = CameraKeyFrame()
keyFrame5286.KeyTime = 0.715
keyFrame5286.KeyValues = [0.0]
keyFrame5286.Position = [22.435916445987004, 20.0, 23.783690135087745]
keyFrame5286.FocalPoint = [20, 20, 20]
keyFrame5286.ViewUp = [0.4203259075405478, -0.866, -0.27060329153778473]
keyFrame5286.ViewAngle = 30.0
keyFrame5286.ParallelScale = 0.97681
keyFrame5286.PositionPathPoints = [22.435916445987004, 20.0, 23.783690135087745]
keyFrame5286.FocalPathPoints = [20, 20, 20]
keyFrame5286.PositionMode = 'Path'
keyFrame5286.FocalPointMode = 'Path'
keyFrame5286.ClosedFocalPath = 0
keyFrame5286.ClosedPositionPath = 0

# ====================================================================
keyFrame5287 = CameraKeyFrame()
keyFrame5287.KeyTime = 0.7175
keyFrame5287.KeyValues = [0.0]
keyFrame5287.Position = [22.443478949315764, 20.0, 23.77881073812867]
keyFrame5287.FocalPoint = [20, 20, 20]
keyFrame5287.ViewUp = [0.4197838606643379, -0.866, -0.27144340156940444]
keyFrame5287.ViewAngle = 30.0
keyFrame5287.ParallelScale = 0.97681
keyFrame5287.PositionPathPoints = [22.443478949315764, 20.0, 23.77881073812867]
keyFrame5287.FocalPathPoints = [20, 20, 20]
keyFrame5287.PositionMode = 'Path'
keyFrame5287.FocalPointMode = 'Path'
keyFrame5287.ClosedFocalPath = 0
keyFrame5287.ClosedPositionPath = 0

# ====================================================================
keyFrame5288 = CameraKeyFrame()
keyFrame5288.KeyTime = 0.72
keyFrame5288.KeyValues = [0.0]
keyFrame5288.Position = [22.451031678729112, 20.0, 23.77391622593376]
keyFrame5288.FocalPoint = [20, 20, 20]
keyFrame5288.ViewUp = [0.41924013465053284, -0.866, -0.27228242582034606]
keyFrame5288.ViewAngle = 30.0
keyFrame5288.ParallelScale = 0.97681
keyFrame5288.PositionPathPoints = [22.451031678729112, 20.0, 23.77391622593376]
keyFrame5288.FocalPathPoints = [20, 20, 20]
keyFrame5288.PositionMode = 'Path'
keyFrame5288.FocalPointMode = 'Path'
keyFrame5288.ClosedFocalPath = 0
keyFrame5288.ClosedPositionPath = 0

# ====================================================================
keyFrame5289 = CameraKeyFrame()
keyFrame5289.KeyTime = 0.7225
keyFrame5289.KeyValues = [0.0]
keyFrame5289.Position = [22.458574604016334, 20.0, 23.76900661808089]
keyFrame5289.FocalPoint = [20, 20, 20]
keyFrame5289.ViewUp = [0.4186947316739603, -0.866, -0.27312036093442543]
keyFrame5289.ViewAngle = 30.0
keyFrame5289.ParallelScale = 0.97681
keyFrame5289.PositionPathPoints = [22.458574604016334, 20.0, 23.76900661808089]
keyFrame5289.FocalPathPoints = [20, 20, 20]
keyFrame5289.PositionMode = 'Path'
keyFrame5289.FocalPointMode = 'Path'
keyFrame5289.ClosedFocalPath = 0
keyFrame5289.ClosedPositionPath = 0

# ====================================================================
keyFrame5290 = CameraKeyFrame()
keyFrame5290.KeyTime = 0.725
keyFrame5290.KeyValues = [0.0]
keyFrame5290.Position = [22.466107695005974, 20.0, 23.76408193420829]
keyFrame5290.FocalPoint = [20, 20, 20]
keyFrame5290.ViewUp = [0.41814765391616876, -0.866, -0.27395720355985204]
keyFrame5290.ViewAngle = 30.0
keyFrame5290.ParallelScale = 0.97681
keyFrame5290.PositionPathPoints = [22.466107695005974, 20.0, 23.76408193420829]
keyFrame5290.FocalPathPoints = [20, 20, 20]
keyFrame5290.PositionMode = 'Path'
keyFrame5290.FocalPointMode = 'Path'
keyFrame5290.ClosedFocalPath = 0
keyFrame5290.ClosedPositionPath = 0

# ====================================================================
keyFrame5291 = CameraKeyFrame()
keyFrame5291.KeyTime = 0.7275
keyFrame5291.KeyValues = [0.0]
keyFrame5291.Position = [22.473630921565938, 20.0, 23.759142194014466]
keyFrame5291.FocalPoint = [20, 20, 20]
keyFrame5291.ViewUp = [0.41759890356541995, -0.866, -0.27479295034924356]
keyFrame5291.ViewAngle = 30.0
keyFrame5291.ParallelScale = 0.97681
keyFrame5291.PositionPathPoints = [22.473630921565938, 20.0, 23.759142194014466]
keyFrame5291.FocalPathPoints = [20, 20, 20]
keyFrame5291.PositionMode = 'Path'
keyFrame5291.FocalPointMode = 'Path'
keyFrame5291.ClosedFocalPath = 0
keyFrame5291.ClosedPositionPath = 0

# ====================================================================
keyFrame5292 = CameraKeyFrame()
keyFrame5292.KeyTime = 0.73
keyFrame5292.KeyValues = [0.0]
keyFrame5292.Position = [22.48114425360362, 20.0, 23.754187417258137]
keyFrame5292.FocalPoint = [20, 20, 20]
keyFrame5292.ViewUp = [0.417048482816681, -0.866, -0.27562759795964126]
keyFrame5292.ViewAngle = 30.0
keyFrame5292.ParallelScale = 0.97681
keyFrame5292.PositionPathPoints = [22.48114425360362, 20.0, 23.754187417258137]
keyFrame5292.FocalPathPoints = [20, 20, 20]
keyFrame5292.PositionMode = 'Path'
keyFrame5292.FocalPointMode = 'Path'
keyFrame5292.ClosedFocalPath = 0
keyFrame5292.ClosedPositionPath = 0

# ====================================================================
keyFrame5293 = CameraKeyFrame()
keyFrame5293.KeyTime = 0.7325
keyFrame5293.KeyValues = [0.0]
keyFrame5293.Position = [22.488647661066043, 20.0, 23.74921762375814]
keyFrame5293.FocalPoint = [20, 20, 20]
keyFrame5293.ViewUp = [0.4164963938716169, -0.866, -0.27646114305252534]
keyFrame5293.ViewAngle = 30.0
keyFrame5293.ParallelScale = 0.97681
keyFrame5293.PositionPathPoints = [22.488647661066043, 20.0, 23.74921762375814]
keyFrame5293.FocalPathPoints = [20, 20, 20]
keyFrame5293.PositionMode = 'Path'
keyFrame5293.FocalPointMode = 'Path'
keyFrame5293.ClosedFocalPath = 0
keyFrame5293.ClosedPositionPath = 0

# ====================================================================
keyFrame5294 = CameraKeyFrame()
keyFrame5294.KeyTime = 0.735
keyFrame5294.KeyValues = [0.0]
keyFrame5294.Position = [22.496141113939956, 20.0, 23.744232833393344]
keyFrame5294.FocalPoint = [20, 20, 20]
keyFrame5294.ViewUp = [0.4159426389385831, -0.866, -0.2772935822938297]
keyFrame5294.ViewAngle = 30.0
keyFrame5294.ParallelScale = 0.97681
keyFrame5294.PositionPathPoints = [22.496141113939956, 20.0, 23.744232833393344]
keyFrame5294.FocalPathPoints = [20, 20, 20]
keyFrame5294.PositionMode = 'Path'
keyFrame5294.FocalPointMode = 'Path'
keyFrame5294.ClosedFocalPath = 0
keyFrame5294.ClosedPositionPath = 0

# ====================================================================
keyFrame5295 = CameraKeyFrame()
keyFrame5295.KeyTime = 0.7375
keyFrame5295.KeyValues = [0.0]
keyFrame5295.Position = [22.503624582251966, 20.0, 23.7392330661026]
keyFrame5295.FocalPoint = [20, 20, 20]
keyFrame5295.ViewUp = [0.4153872202326173, -0.866, -0.2781249123539573]
keyFrame5295.ViewAngle = 30.0
keyFrame5295.ParallelScale = 0.97681
keyFrame5295.PositionPathPoints = [22.503624582251966, 20.0, 23.7392330661026]
keyFrame5295.FocalPathPoints = [20, 20, 20]
keyFrame5295.PositionMode = 'Path'
keyFrame5295.FocalPointMode = 'Path'
keyFrame5295.ClosedFocalPath = 0
keyFrame5295.ClosedPositionPath = 0

# ====================================================================
keyFrame5296 = CameraKeyFrame()
keyFrame5296.KeyTime = 0.74
keyFrame5296.KeyValues = [0.0]
keyFrame5296.Position = [22.511098036068667, 20.0, 23.734218341884617]
keyFrame5296.FocalPoint = [20, 20, 20]
keyFrame5296.ViewUp = [0.4148301399754325, -0.866, -0.2789551299077952]
keyFrame5296.ViewAngle = 30.0
keyFrame5296.ParallelScale = 0.97681
keyFrame5296.PositionPathPoints = [22.511098036068667, 20.0, 23.734218341884617]
keyFrame5296.FocalPathPoints = [20, 20, 20]
keyFrame5296.PositionMode = 'Path'
keyFrame5296.FocalPointMode = 'Path'
keyFrame5296.ClosedFocalPath = 0
keyFrame5296.ClosedPositionPath = 0

# ====================================================================
keyFrame5297 = CameraKeyFrame()
keyFrame5297.KeyTime = 0.7425
keyFrame5297.KeyValues = [0.0]
keyFrame5297.Position = [22.518561445496747, 20.0, 23.729188680797915]
keyFrame5297.FocalPoint = [20, 20, 20]
keyFrame5297.ViewUp = [0.41427140039540894, -0.866, -0.2797842316347297]
keyFrame5297.ViewAngle = 30.0
keyFrame5297.ParallelScale = 0.97681
keyFrame5297.PositionPathPoints = [22.518561445496747, 20.0, 23.729188680797915]
keyFrame5297.FocalPathPoints = [20, 20, 20]
keyFrame5297.PositionMode = 'Path'
keyFrame5297.FocalPointMode = 'Path'
keyFrame5297.ClosedFocalPath = 0
keyFrame5297.ClosedPositionPath = 0

# ====================================================================
keyFrame5298 = CameraKeyFrame()
keyFrame5298.KeyTime = 0.745
keyFrame5298.KeyValues = [0.0]
keyFrame5298.Position = [22.52601478068313, 20.0, 23.72414410296073]
keyFrame5298.FocalPoint = [20, 20, 20]
keyFrame5298.ViewUp = [0.41371100372758657, -0.866, -0.28061221421866145]
keyFrame5298.ViewAngle = 30.0
keyFrame5298.ParallelScale = 0.97681
keyFrame5298.PositionPathPoints = [22.52601478068313, 20.0, 23.72414410296073]
keyFrame5298.FocalPathPoints = [20, 20, 20]
keyFrame5298.PositionMode = 'Path'
keyFrame5298.FocalPointMode = 'Path'
keyFrame5298.ClosedFocalPath = 0
keyFrame5298.ClosedPositionPath = 0

# ====================================================================
keyFrame5299 = CameraKeyFrame()
keyFrame5299.KeyTime = 0.7475
keyFrame5299.KeyValues = [0.0]
keyFrame5299.Position = [22.533458011815075, 20.0, 23.719084628550927]
keyFrame5299.FocalPoint = [20, 20, 20]
keyFrame5299.ViewUp = [0.41314895221365744, -0.866, -0.2814390743480207]
keyFrame5299.ViewAngle = 30.0
keyFrame5299.ParallelScale = 0.97681
keyFrame5299.PositionPathPoints = [22.533458011815075, 20.0, 23.719084628550927]
keyFrame5299.FocalPathPoints = [20, 20, 20]
keyFrame5299.PositionMode = 'Path'
keyFrame5299.FocalPointMode = 'Path'
keyFrame5299.ClosedFocalPath = 0
keyFrame5299.ClosedPositionPath = 0

# ====================================================================
keyFrame5300 = CameraKeyFrame()
keyFrame5300.KeyTime = 0.75
keyFrame5300.KeyValues = [0.0]
keyFrame5300.Position = [22.540891109120306, 20.0, 23.714010277805933]
keyFrame5300.FocalPoint = [20, 20, 20]
keyFrame5300.ViewUp = [0.4125852481019581, -0.866, -0.2822648087157822]
keyFrame5300.ViewAngle = 30.0
keyFrame5300.ParallelScale = 0.97681
keyFrame5300.PositionPathPoints = [22.540891109120306, 20.0, 23.714010277805933]
keyFrame5300.FocalPathPoints = [20, 20, 20]
keyFrame5300.PositionMode = 'Path'
keyFrame5300.FocalPointMode = 'Path'
keyFrame5300.ClosedFocalPath = 0
keyFrame5300.ClosedPositionPath = 0

# ====================================================================
keyFrame5301 = CameraKeyFrame()
keyFrame5301.KeyTime = 0.7525
keyFrame5301.KeyValues = [0.0]
keyFrame5301.Position = [22.548314042867144, 20.0, 23.70892107102264]
keyFrame5301.FocalPoint = [20, 20, 20]
keyFrame5301.ViewUp = [0.41201989364746194, -0.866, -0.2830894140194807]
keyFrame5301.ViewAngle = 30.0
keyFrame5301.ParallelScale = 0.97681
keyFrame5301.PositionPathPoints = [22.548314042867144, 20.0, 23.70892107102264]
keyFrame5301.FocalPathPoints = [20, 20, 20]
keyFrame5301.PositionMode = 'Path'
keyFrame5301.FocalPointMode = 'Path'
keyFrame5301.ClosedFocalPath = 0
keyFrame5301.ClosedPositionPath = 0

# ====================================================================
keyFrame5302 = CameraKeyFrame()
keyFrame5302.KeyTime = 0.755
keyFrame5302.KeyValues = [0.0]
keyFrame5302.Position = [22.555726783364612, 20.0, 23.70381702855733]
keyFrame5302.FocalPoint = [20, 20, 20]
keyFrame5302.ViewUp = [0.4114528911117715, -0.866, -0.2839128869612255]
keyFrame5302.ViewAngle = 30.0
keyFrame5302.ParallelScale = 0.97681
keyFrame5302.PositionPathPoints = [22.555726783364612, 20.0, 23.70381702855733]
keyFrame5302.FocalPathPoints = [20, 20, 20]
keyFrame5302.PositionMode = 'Path'
keyFrame5302.FocalPointMode = 'Path'
keyFrame5302.ClosedFocalPath = 0
keyFrame5302.ClosedPositionPath = 0

# ====================================================================
keyFrame5303 = CameraKeyFrame()
keyFrame5303.KeyTime = 0.7575
keyFrame5303.KeyValues = [0.0]
keyFrame5303.Position = [22.563129300962565, 20.0, 23.698698170825597]
keyFrame5303.FocalPoint = [20, 20, 20]
keyFrame5303.ViewUp = [0.4108842427631109, -0.866, -0.28473522424771636]
keyFrame5303.ViewAngle = 30.0
keyFrame5303.ParallelScale = 0.97681
keyFrame5303.PositionPathPoints = [22.563129300962565, 20.0, 23.698698170825597]
keyFrame5303.FocalPathPoints = [20, 20, 20]
keyFrame5303.PositionMode = 'Path'
keyFrame5303.FocalPointMode = 'Path'
keyFrame5303.ClosedFocalPath = 0
keyFrame5303.ClosedPositionPath = 0

# ====================================================================
keyFrame5304 = CameraKeyFrame()
keyFrame5304.KeyTime = 0.76
keyFrame5304.KeyValues = [0.0]
keyFrame5304.Position = [22.570521566051806, 20.0, 23.693564518302253]
keyFrame5304.FocalPoint = [20, 20, 20]
keyFrame5304.ViewUp = [0.4103139508763182, -0.866, -0.2855564225902579]
keyFrame5304.ViewAngle = 30.0
keyFrame5304.ParallelScale = 0.97681
keyFrame5304.PositionPathPoints = [22.570521566051806, 20.0, 23.693564518302253]
keyFrame5304.FocalPathPoints = [20, 20, 20]
keyFrame5304.PositionMode = 'Path'
keyFrame5304.FocalPointMode = 'Path'
keyFrame5304.ClosedFocalPath = 0
keyFrame5304.ClosedPositionPath = 0

# ====================================================================
keyFrame5305 = CameraKeyFrame()
keyFrame5305.KeyTime = 0.7625
keyFrame5305.KeyValues = [0.0]
keyFrame5305.Position = [22.577903549064217, 20.0, 23.68841609152124]
keyFrame5305.FocalPoint = [20, 20, 20]
keyFrame5305.ViewUp = [0.4097420177328379, -0.866, -0.28637647870477495]
keyFrame5305.ViewAngle = 30.0
keyFrame5305.ParallelScale = 0.97681
keyFrame5305.PositionPathPoints = [22.577903549064217, 20.0, 23.68841609152124]
keyFrame5305.FocalPathPoints = [20, 20, 20]
keyFrame5305.PositionMode = 'Path'
keyFrame5305.FocalPointMode = 'Path'
keyFrame5305.ClosedFocalPath = 0
keyFrame5305.ClosedPositionPath = 0

# ====================================================================
keyFrame5306 = CameraKeyFrame()
keyFrame5306.KeyTime = 0.765
keyFrame5306.KeyValues = [0.0]
keyFrame5306.Position = [22.585275220472862, 20.0, 23.683252911075577]
keyFrame5306.FocalPoint = [20, 20, 20]
keyFrame5306.ViewUp = [0.409168445620713, -0.866, -0.28719538931182814]
keyFrame5306.ViewAngle = 30.0
keyFrame5306.ParallelScale = 0.97681
keyFrame5306.PositionPathPoints = [22.585275220472862, 20.0, 23.683252911075577]
keyFrame5306.FocalPathPoints = [20, 20, 20]
keyFrame5306.PositionMode = 'Path'
keyFrame5306.FocalPointMode = 'Path'
keyFrame5306.ClosedFocalPath = 0
keyFrame5306.ClosedPositionPath = 0

# ====================================================================
keyFrame5307 = CameraKeyFrame()
keyFrame5307.KeyTime = 0.7675
keyFrame5307.KeyValues = [0.0]
keyFrame5307.Position = [22.59263655079213, 20.0, 23.678074997617237]
keyFrame5307.FocalPoint = [20, 20, 20]
keyFrame5307.ViewUp = [0.4085932368345776, -0.866, -0.2880131511366283]
keyFrame5307.ViewAngle = 30.0
keyFrame5307.ParallelScale = 0.97681
keyFrame5307.PositionPathPoints = [22.59263655079213, 20.0, 23.678074997617237]
keyFrame5307.FocalPathPoints = [20, 20, 20]
keyFrame5307.PositionMode = 'Path'
keyFrame5307.FocalPointMode = 'Path'
keyFrame5307.ClosedFocalPath = 0
keyFrame5307.ClosedPositionPath = 0

# ====================================================================
keyFrame5308 = CameraKeyFrame()
keyFrame5308.KeyTime = 0.77
keyFrame5308.KeyValues = [0.0]
keyFrame5308.Position = [22.59998751057783, 20.0, 23.672882371857085]
keyFrame5308.FocalPoint = [20, 20, 20]
keyFrame5308.ViewUp = [0.4080163936756493, -0.866, -0.28882976090905205]
keyFrame5308.ViewAngle = 30.0
keyFrame5308.ParallelScale = 0.97681
keyFrame5308.PositionPathPoints = [22.59998751057783, 20.0, 23.672882371857085]
keyFrame5308.FocalPathPoints = [20, 20, 20]
keyFrame5308.PositionMode = 'Path'
keyFrame5308.FocalPointMode = 'Path'
keyFrame5308.ClosedFocalPath = 0
keyFrame5308.ClosedPositionPath = 0

# ====================================================================
keyFrame5309 = CameraKeyFrame()
keyFrame5309.KeyTime = 0.7725
keyFrame5309.KeyValues = [0.0]
keyFrame5309.Position = [22.607328070427336, 20.0, 23.6676750545648]
keyFrame5309.FocalPoint = [20, 20, 20]
keyFrame5309.ViewUp = [0.40743791845172145, -0.866, -0.2896452153636569]
keyFrame5309.ViewAngle = 30.0
keyFrame5309.ParallelScale = 0.97681
keyFrame5309.PositionPathPoints = [22.607328070427336, 20.0, 23.6676750545648]
keyFrame5309.FocalPathPoints = [20, 20, 20]
keyFrame5309.PositionMode = 'Path'
keyFrame5309.FocalPointMode = 'Path'
keyFrame5309.ClosedFocalPath = 0
keyFrame5309.ClosedPositionPath = 0

# ====================================================================
keyFrame5310 = CameraKeyFrame()
keyFrame5310.KeyTime = 0.775
keyFrame5310.KeyValues = [0.0]
keyFrame5310.Position = [22.61465820097969, 20.0, 23.662453066568766]
keyFrame5310.FocalPoint = [20, 20, 20]
keyFrame5310.ViewUp = [0.40685781347715555, -0.866, -0.2904595112396962]
keyFrame5310.ViewAngle = 30.0
keyFrame5310.ParallelScale = 0.97681
keyFrame5310.PositionPathPoints = [22.61465820097969, 20.0, 23.662453066568766]
keyFrame5310.FocalPathPoints = [20, 20, 20]
keyFrame5310.PositionMode = 'Path'
keyFrame5310.FocalPointMode = 'Path'
keyFrame5310.ClosedFocalPath = 0
keyFrame5310.ClosedPositionPath = 0

# ====================================================================
keyFrame5311 = CameraKeyFrame()
keyFrame5311.KeyTime = 0.7775
keyFrame5311.KeyValues = [0.0]
keyFrame5311.Position = [22.621977872912087, 20.0, 23.65721642875842]
keyFrame5311.FocalPoint = [20, 20, 20]
keyFrame5311.ViewUp = [0.4062760810728736, -0.866, -0.2912726452811344]
keyFrame5311.ViewAngle = 30.0
keyFrame5311.ParallelScale = 0.97681
keyFrame5311.PositionPathPoints = [22.621977872912087, 20.0, 23.65721642875842]
keyFrame5311.FocalPathPoints = [20, 20, 20]
keyFrame5311.PositionMode = 'Path'
keyFrame5311.FocalPointMode = 'Path'
keyFrame5311.ClosedFocalPath = 0
keyFrame5311.ClosedPositionPath = 0

# ====================================================================
keyFrame5312 = CameraKeyFrame()
keyFrame5312.KeyTime = 0.78
keyFrame5312.KeyValues = [0.0]
keyFrame5312.Position = [22.629287056934714, 20.0, 23.651965162087645]
keyFrame5312.FocalPoint = [20, 20, 20]
keyFrame5312.ViewUp = [0.40569272356635055, -0.866, -0.29208461423666215]
keyFrame5312.ViewAngle = 30.0
keyFrame5312.ParallelScale = 0.97681
keyFrame5312.PositionPathPoints = [22.629287056934714, 20.0, 23.651965162087645]
keyFrame5312.FocalPathPoints = [20, 20, 20]
keyFrame5312.PositionMode = 'Path'
keyFrame5312.FocalPointMode = 'Path'
keyFrame5312.ClosedFocalPath = 0
keyFrame5312.ClosedPositionPath = 0

# ====================================================================
keyFrame5313 = CameraKeyFrame()
keyFrame5313.KeyTime = 0.7825
keyFrame5313.KeyValues = [0.0]
keyFrame5313.Position = [22.636585723809855, 20.0, 23.646699287562143]
keyFrame5313.FocalPoint = [20, 20, 20]
keyFrame5313.ViewUp = [0.4051077432916066, -0.866, -0.2928954148597115]
keyFrame5313.ViewAngle = 30.0
keyFrame5313.ParallelScale = 0.97681
keyFrame5313.PositionPathPoints = [22.636585723809855, 20.0, 23.646699287562143]
keyFrame5313.FocalPathPoints = [20, 20, 20]
keyFrame5313.PositionMode = 'Path'
keyFrame5313.FocalPointMode = 'Path'
keyFrame5313.ClosedFocalPath = 0
keyFrame5313.ClosedPositionPath = 0

# ====================================================================
keyFrame5314 = CameraKeyFrame()
keyFrame5314.KeyTime = 0.785
keyFrame5314.KeyValues = [0.0]
keyFrame5314.Position = [22.643873844342732, 20.0, 23.641418826245456]
keyFrame5314.FocalPoint = [20, 20, 20]
keyFrame5314.ViewUp = [0.40452114258919963, -0.866, -0.29370504390847074]
keyFrame5314.ViewAngle = 30.0
keyFrame5314.ParallelScale = 0.97681
keyFrame5314.PositionPathPoints = [22.643873844342732, 20.0, 23.641418826245456]
keyFrame5314.FocalPathPoints = [20, 20, 20]
keyFrame5314.PositionMode = 'Path'
keyFrame5314.FocalPointMode = 'Path'
keyFrame5314.ClosedFocalPath = 0
keyFrame5314.ClosedPositionPath = 0

# ====================================================================
keyFrame5315 = CameraKeyFrame()
keyFrame5315.KeyTime = 0.7875
keyFrame5315.KeyValues = [0.0]
keyFrame5315.Position = [22.65115138938076, 20.0, 23.636123799259476]
keyFrame5315.FocalPoint = [20, 20, 20]
keyFrame5315.ViewUp = [0.4039329238062175, -0.866, -0.29451349814590005]
keyFrame5315.ViewAngle = 30.0
keyFrame5315.ParallelScale = 0.97681
keyFrame5315.PositionPathPoints = [22.65115138938076, 20.0, 23.636123799259476]
keyFrame5315.FocalPathPoints = [20, 20, 20]
keyFrame5315.PositionMode = 'Path'
keyFrame5315.FocalPointMode = 'Path'
keyFrame5315.ClosedFocalPath = 0
keyFrame5315.ClosedPositionPath = 0

# ====================================================================
keyFrame5316 = CameraKeyFrame()
keyFrame5316.KeyTime = 0.79
keyFrame5316.KeyValues = [0.0]
keyFrame5316.Position = [22.65841832981368, 20.0, 23.630814227784356]
keyFrame5316.FocalPoint = [20, 20, 20]
keyFrame5316.ViewUp = [0.4033430892962704, -0.866, -0.29532077433974613]
keyFrame5316.ViewAngle = 30.0
keyFrame5316.ParallelScale = 0.97681
keyFrame5316.PositionPathPoints = [22.65841832981368, 20.0, 23.630814227784356]
keyFrame5316.FocalPathPoints = [20, 20, 20]
keyFrame5316.PositionMode = 'Path'
keyFrame5316.FocalPointMode = 'Path'
keyFrame5316.ClosedFocalPath = 0
keyFrame5316.ClosedPositionPath = 0

# ====================================================================
keyFrame5317 = CameraKeyFrame()
keyFrame5317.KeyTime = 0.7925
keyFrame5317.KeyValues = [0.0]
keyFrame5317.Position = [22.665674636573645, 20.0, 23.625490133058417]
keyFrame5317.FocalPoint = [20, 20, 20]
keyFrame5317.ViewUp = [0.4027516414194833, -0.866, -0.29612686926255755]
keyFrame5317.ViewAngle = 30.0
keyFrame5317.ParallelScale = 0.97681
keyFrame5317.PositionPathPoints = [22.665674636573645, 20.0, 23.625490133058417]
keyFrame5317.FocalPathPoints = [20, 20, 20]
keyFrame5317.PositionMode = 'Path'
keyFrame5317.FocalPointMode = 'Path'
keyFrame5317.ClosedFocalPath = 0
keyFrame5317.ClosedPositionPath = 0

# ====================================================================
keyFrame5318 = CameraKeyFrame()
keyFrame5318.KeyTime = 0.795
keyFrame5318.KeyValues = [0.0]
keyFrame5318.Position = [22.67292028063536, 20.0, 23.620151536378078]
keyFrame5318.FocalPoint = [20, 20, 20]
keyFrame5318.ViewUp = [0.4021585825424883, -0.866, -0.29693177969169987]
keyFrame5318.ViewAngle = 30.0
keyFrame5318.ParallelScale = 0.97681
keyFrame5318.PositionPathPoints = [22.67292028063536, 20.0, 23.620151536378078]
keyFrame5318.FocalPathPoints = [20, 20, 20]
keyFrame5318.PositionMode = 'Path'
keyFrame5318.FocalPointMode = 'Path'
keyFrame5318.ClosedFocalPath = 0
keyFrame5318.ClosedPositionPath = 0

# ====================================================================
keyFrame5319 = CameraKeyFrame()
keyFrame5319.KeyTime = 0.7975
keyFrame5319.KeyValues = [0.0]
keyFrame5319.Position = [22.680155233016187, 20.0, 23.614798459097752]
keyFrame5319.FocalPoint = [20, 20, 20]
keyFrame5319.ViewUp = [0.40156391503841704, -0.866, -0.29773550240937086]
keyFrame5319.ViewAngle = 30.0
keyFrame5319.ParallelScale = 0.97681
keyFrame5319.PositionPathPoints = [22.680155233016187, 20.0, 23.614798459097752]
keyFrame5319.FocalPathPoints = [20, 20, 20]
keyFrame5319.PositionMode = 'Path'
keyFrame5319.FocalPointMode = 'Path'
keyFrame5319.ClosedFocalPath = 0
keyFrame5319.ClosedPositionPath = 0

# ====================================================================
keyFrame5320 = CameraKeyFrame()
keyFrame5320.KeyTime = 0.8
keyFrame5320.KeyValues = [0.0]
keyFrame5320.Position = [22.687379464776278, 20.0, 23.609430922629777]
keyFrame5320.FocalPoint = [20, 20, 20]
keyFrame5320.ViewUp = [0.40096764128689294, -0.866, -0.29853803420261543]
keyFrame5320.ViewAngle = 30.0
keyFrame5320.ParallelScale = 0.97681
keyFrame5320.PositionPathPoints = [22.687379464776278, 20.0, 23.609430922629777]
keyFrame5320.FocalPathPoints = [20, 20, 20]
keyFrame5320.PositionMode = 'Path'
keyFrame5320.FocalPointMode = 'Path'
keyFrame5320.ClosedFocalPath = 0
keyFrame5320.ClosedPositionPath = 0

# ====================================================================
keyFrame5321 = CameraKeyFrame()
keyFrame5321.KeyTime = 0.8025
keyFrame5321.KeyValues = [0.0]
keyFrame5321.Position = [22.694592947018666, 20.0, 23.604048948444323]
keyFrame5321.FocalPoint = [20, 20, 20]
keyFrame5321.ViewUp = [0.40036976367402366, -0.866, -0.2993393718633408]
keyFrame5321.ViewAngle = 30.0
keyFrame5321.ParallelScale = 0.97681
keyFrame5321.PositionPathPoints = [22.694592947018666, 20.0, 23.604048948444323]
keyFrame5321.FocalPathPoints = [20, 20, 20]
keyFrame5321.PositionMode = 'Path'
keyFrame5321.FocalPointMode = 'Path'
keyFrame5321.ClosedFocalPath = 0
keyFrame5321.ClosedPositionPath = 0

# ====================================================================
keyFrame5322 = CameraKeyFrame()
keyFrame5322.KeyTime = 0.805
keyFrame5322.KeyValues = [0.0]
keyFrame5322.Position = [22.70179565088941, 20.0, 23.598652558069297]
keyFrame5322.FocalPoint = [20, 20, 20]
keyFrame5322.ViewUp = [0.3997702845883811, -0.866, -0.3001395121808841]
keyFrame5322.ViewAngle = 30.0
keyFrame5322.ParallelScale = 0.97681
keyFrame5322.PositionPathPoints = [22.70179565088941, 20.0, 23.598652558069297]
keyFrame5322.FocalPathPoints = [20, 20, 20]
keyFrame5322.PositionMode = 'Path'
keyFrame5322.FocalPointMode = 'Path'
keyFrame5322.ClosedFocalPath = 0
keyFrame5322.ClosedPositionPath = 0

# ====================================================================
keyFrame5323 = CameraKeyFrame()
keyFrame5323.KeyTime = 0.8075
keyFrame5323.KeyValues = [0.0]
keyFrame5323.Position = [22.708987547577692, 20.0, 23.59324177309027]
keyFrame5323.FocalPoint = [20, 20, 20]
keyFrame5323.ViewUp = [0.3991692064204149, -0.866, -0.3009384519409532]
keyFrame5323.ViewAngle = 30.0
keyFrame5323.ParallelScale = 0.97681
keyFrame5323.PositionPathPoints = [22.708987547577692, 20.0, 23.59324177309027]
keyFrame5323.FocalPathPoints = [20, 20, 20]
keyFrame5323.PositionMode = 'Path'
keyFrame5323.FocalPointMode = 'Path'
keyFrame5323.ClosedFocalPath = 0
keyFrame5323.ClosedPositionPath = 0

# ====================================================================
keyFrame5324 = CameraKeyFrame()
keyFrame5324.KeyTime = 0.81
keyFrame5324.KeyValues = [0.0]
keyFrame5324.Position = [22.716168608315936, 20.0, 23.587816615150388]
keyFrame5324.FocalPoint = [20, 20, 20]
keyFrame5324.ViewUp = [0.3985665315741434, -0.866, -0.3017361879473559]
keyFrame5324.ViewAngle = 30.0
keyFrame5324.ParallelScale = 0.97681
keyFrame5324.PositionPathPoints = [22.716168608315936, 20.0, 23.587816615150388]
keyFrame5324.FocalPathPoints = [20, 20, 20]
keyFrame5324.PositionMode = 'Path'
keyFrame5324.FocalPointMode = 'Path'
keyFrame5324.ClosedFocalPath = 0
keyFrame5324.ClosedPositionPath = 0

# ====================================================================
keyFrame5325 = CameraKeyFrame()
keyFrame5325.KeyTime = 0.8125
keyFrame5325.KeyValues = [0.0]
keyFrame5325.Position = [22.72333880437994, 20.0, 23.582377105950272]
keyFrame5325.FocalPoint = [20, 20, 20]
keyFrame5325.ViewUp = [0.3979622624601859, -0.866, -0.3025327170090964]
keyFrame5325.ViewAngle = 30.0
keyFrame5325.ParallelScale = 0.97681
keyFrame5325.PositionPathPoints = [22.72333880437994, 20.0, 23.582377105950272]
keyFrame5325.FocalPathPoints = [20, 20, 20]
keyFrame5325.PositionMode = 'Path'
keyFrame5325.FocalPointMode = 'Path'
keyFrame5325.ClosedFocalPath = 0
keyFrame5325.ClosedPositionPath = 0

# ====================================================================
keyFrame5326 = CameraKeyFrame()
keyFrame5326.KeyTime = 0.815
keyFrame5326.KeyValues = [0.0]
keyFrame5326.Position = [22.730498107088966, 20.0, 23.576923267247945]
keyFrame5326.FocalPoint = [20, 20, 20]
keyFrame5326.ViewUp = [0.3973564014955489, -0.866, -0.30332803594000746]
keyFrame5326.ViewAngle = 30.0
keyFrame5326.ParallelScale = 0.97681
keyFrame5326.PositionPathPoints = [22.730498107088966, 20.0, 23.576923267247945]
keyFrame5326.FocalPathPoints = [20, 20, 20]
keyFrame5326.PositionMode = 'Path'
keyFrame5326.FocalPointMode = 'Path'
keyFrame5326.ClosedFocalPath = 0
keyFrame5326.ClosedPositionPath = 0

# ====================================================================
keyFrame5327 = CameraKeyFrame()
keyFrame5327.KeyTime = 0.8175
keyFrame5327.KeyValues = [0.0]
keyFrame5327.Position = [22.73764648780588, 20.0, 23.571455120858737]
keyFrame5327.FocalPoint = [20, 20, 20]
keyFrame5327.ViewUp = [0.39674895110361735, -0.866, -0.3041221415587639]
keyFrame5327.ViewAngle = 30.0
keyFrame5327.ParallelScale = 0.97681
keyFrame5327.PositionPathPoints = [22.73764648780588, 20.0, 23.571455120858737]
keyFrame5327.FocalPathPoints = [20, 20, 20]
keyFrame5327.PositionMode = 'Path'
keyFrame5327.FocalPointMode = 'Path'
keyFrame5327.ClosedFocalPath = 0
keyFrame5327.ClosedPositionPath = 0

# ====================================================================
keyFrame5328 = CameraKeyFrame()
keyFrame5328.KeyTime = 0.82
keyFrame5328.KeyValues = [0.0]
keyFrame5328.Position = [22.74478391793725, 20.0, 23.565972688655204]
keyFrame5328.FocalPoint = [20, 20, 20]
keyFrame5328.ViewUp = [0.39613991371414614, -0.866, -0.3049150306888956]
keyFrame5328.ViewAngle = 30.0
keyFrame5328.ParallelScale = 0.97681
keyFrame5328.PositionPathPoints = [22.74478391793725, 20.0, 23.565972688655204]
keyFrame5328.FocalPathPoints = [20, 20, 20]
keyFrame5328.PositionMode = 'Path'
keyFrame5328.FocalPointMode = 'Path'
keyFrame5328.ClosedFocalPath = 0
keyFrame5328.ClosedPositionPath = 0

# ====================================================================
keyFrame5329 = CameraKeyFrame()
keyFrame5329.KeyTime = 0.8225
keyFrame5329.KeyValues = [0.0]
keyFrame5329.Position = [22.75191036893348, 20.0, 23.56047599256703]
keyFrame5329.FocalPoint = [20, 20, 20]
keyFrame5329.ViewUp = [0.39552929176325125, -0.866, -0.3057067001588006]
keyFrame5329.ViewAngle = 30.0
keyFrame5329.ParallelScale = 0.97681
keyFrame5329.PositionPathPoints = [22.75191036893348, 20.0, 23.56047599256703]
keyFrame5329.FocalPathPoints = [20, 20, 20]
keyFrame5329.PositionMode = 'Path'
keyFrame5329.FocalPointMode = 'Path'
keyFrame5329.ClosedFocalPath = 0
keyFrame5329.ClosedPositionPath = 0

# ====================================================================
keyFrame5330 = CameraKeyFrame()
keyFrame5330.KeyTime = 0.825
keyFrame5330.KeyValues = [0.0]
keyFrame5330.Position = [22.759025812288904, 20.0, 23.554965054580947]
keyFrame5330.FocalPoint = [20, 20, 20]
keyFrame5330.ViewUp = [0.39491708769340106, -0.866, -0.30649714680175844]
keyFrame5330.ViewAngle = 30.0
keyFrame5330.ParallelScale = 0.97681
keyFrame5330.PositionPathPoints = [22.759025812288904, 20.0, 23.554965054580947]
keyFrame5330.FocalPathPoints = [20, 20, 20]
keyFrame5330.PositionMode = 'Path'
keyFrame5330.FocalPointMode = 'Path'
keyFrame5330.ClosedFocalPath = 0
keyFrame5330.ClosedPositionPath = 0

# ====================================================================
keyFrame5331 = CameraKeyFrame()
keyFrame5331.KeyTime = 0.8275
keyFrame5331.KeyValues = [0.0]
keyFrame5331.Position = [22.76613021954192, 20.0, 23.549439896740637]
keyFrame5331.FocalPoint = [20, 20, 20]
keyFrame5331.ViewUp = [0.39430330395340785, -0.866, -0.3072863674559434]
keyFrame5331.ViewAngle = 30.0
keyFrame5331.ParallelScale = 0.97681
keyFrame5331.PositionPathPoints = [22.76613021954192, 20.0, 23.549439896740637]
keyFrame5331.FocalPathPoints = [20, 20, 20]
keyFrame5331.PositionMode = 'Path'
keyFrame5331.FocalPointMode = 'Path'
keyFrame5331.ClosedFocalPath = 0
keyFrame5331.ClosedPositionPath = 0

# ====================================================================
keyFrame5332 = CameraKeyFrame()
keyFrame5332.KeyTime = 0.83
keyFrame5332.KeyValues = [0.0]
keyFrame5332.Position = [22.773223562275103, 20.0, 23.54390054114665]
keyFrame5332.FocalPoint = [20, 20, 20]
keyFrame5332.ViewUp = [0.3936879429984191, -0.866, -0.30807435896443747]
keyFrame5332.ViewAngle = 30.0
keyFrame5332.ParallelScale = 0.97681
keyFrame5332.PositionPathPoints = [22.773223562275103, 20.0, 23.54390054114665]
keyFrame5332.FocalPathPoints = [20, 20, 20]
keyFrame5332.PositionMode = 'Path'
keyFrame5332.FocalPointMode = 'Path'
keyFrame5332.ClosedFocalPath = 0
keyFrame5332.ClosedPositionPath = 0

# ====================================================================
keyFrame5333 = CameraKeyFrame()
keyFrame5333.KeyTime = 0.8325
keyFrame5333.KeyValues = [0.0]
keyFrame5333.Position = [22.780305812115294, 20.0, 23.538347009956325]
keyFrame5333.FocalPoint = [20, 20, 20]
keyFrame5333.ViewUp = [0.3930710072899084, -0.866, -0.3088611181752436]
keyFrame5333.ViewAngle = 30.0
keyFrame5333.ParallelScale = 0.97681
keyFrame5333.PositionPathPoints = [22.780305812115294, 20.0, 23.538347009956325]
keyFrame5333.FocalPathPoints = [20, 20, 20]
keyFrame5333.PositionMode = 'Path'
keyFrame5333.FocalPointMode = 'Path'
keyFrame5333.ClosedFocalPath = 0
keyFrame5333.ClosedPositionPath = 0

# ====================================================================
keyFrame5334 = CameraKeyFrame()
keyFrame5334.KeyTime = 0.835
keyFrame5334.KeyValues = [0.0]
keyFrame5334.Position = [22.787376940733765, 20.0, 23.53277932538367]
keyFrame5334.FocalPoint = [20, 20, 20]
keyFrame5334.ViewUp = [0.3924524992956675, -0.866, -0.3096466419412991]
keyFrame5334.ViewAngle = 30.0
keyFrame5334.ParallelScale = 0.97681
keyFrame5334.PositionPathPoints = [22.787376940733765, 20.0, 23.53277932538367]
keyFrame5334.FocalPathPoints = [20, 20, 20]
keyFrame5334.PositionMode = 'Path'
keyFrame5334.FocalPointMode = 'Path'
keyFrame5334.ClosedFocalPath = 0
keyFrame5334.ClosedPositionPath = 0

# ====================================================================
keyFrame5335 = CameraKeyFrame()
keyFrame5335.KeyTime = 0.8375
keyFrame5335.KeyValues = [0.0]
keyFrame5335.Position = [22.79443691984628, 20.0, 23.52719750969931]
keyFrame5335.FocalPoint = [20, 20, 20]
keyFrame5335.ViewUp = [0.39183242148979697, -0.866, -0.3104309271204884]
keyFrame5335.ViewAngle = 30.0
keyFrame5335.ParallelScale = 0.97681
keyFrame5335.PositionPathPoints = [22.79443691984628, 20.0, 23.52719750969931]
keyFrame5335.FocalPathPoints = [20, 20, 20]
keyFrame5335.PositionMode = 'Path'
keyFrame5335.FocalPointMode = 'Path'
keyFrame5335.ClosedFocalPath = 0
keyFrame5335.ClosedPositionPath = 0

# ====================================================================
keyFrame5336 = CameraKeyFrame()
keyFrame5336.KeyTime = 0.84
keyFrame5336.KeyValues = [0.0]
keyFrame5336.Position = [22.801485721213254, 20.0, 23.52160158523036]
keyFrame5336.FocalPoint = [20, 20, 20]
keyFrame5336.ViewUp = [0.39121077635269785, -0.866, -0.3112139705756568]
keyFrame5336.ViewAngle = 30.0
keyFrame5336.ParallelScale = 0.97681
keyFrame5336.PositionPathPoints = [22.801485721213254, 20.0, 23.52160158523036]
keyFrame5336.FocalPathPoints = [20, 20, 20]
keyFrame5336.PositionMode = 'Path'
keyFrame5336.FocalPointMode = 'Path'
keyFrame5336.ClosedFocalPath = 0
keyFrame5336.ClosedPositionPath = 0

# ====================================================================
keyFrame5337 = CameraKeyFrame()
keyFrame5337.KeyTime = 0.8425
keyFrame5337.KeyValues = [0.0]
keyFrame5337.Position = [22.808523316639835, 20.0, 23.51599157436037]
keyFrame5337.FocalPoint = [20, 20, 20]
keyFrame5337.ViewUp = [0.39058756637106296, -0.866, -0.3119957691746231]
keyFrame5337.ViewAngle = 30.0
keyFrame5337.ParallelScale = 0.97681
keyFrame5337.PositionPathPoints = [22.808523316639835, 20.0, 23.51599157436037]
keyFrame5337.FocalPathPoints = [20, 20, 20]
keyFrame5337.PositionMode = 'Path'
keyFrame5337.FocalPointMode = 'Path'
keyFrame5337.ClosedFocalPath = 0
keyFrame5337.ClosedPositionPath = 0

# ====================================================================
keyFrame5338 = CameraKeyFrame()
keyFrame5338.KeyTime = 0.845
keyFrame5338.KeyValues = [0.0]
keyFrame5338.Position = [22.815549677976044, 20.0, 23.510367499529213]
keyFrame5338.FocalPoint = [20, 20, 20]
keyFrame5338.ViewUp = [0.38996279403786804, -0.866, -0.31277631979019316]
keyFrame5338.ViewAngle = 30.0
keyFrame5338.ParallelScale = 0.97681
keyFrame5338.PositionPathPoints = [22.815549677976044, 20.0, 23.510367499529213]
keyFrame5338.FocalPathPoints = [20, 20, 20]
keyFrame5338.PositionMode = 'Path'
keyFrame5338.FocalPointMode = 'Path'
keyFrame5338.ClosedFocalPath = 0
keyFrame5338.ClosedPositionPath = 0

# ====================================================================
keyFrame5339 = CameraKeyFrame()
keyFrame5339.KeyTime = 0.8475
keyFrame5339.KeyValues = [0.0]
keyFrame5339.Position = [22.822564777116863, 20.0, 23.504729383232988]
keyFrame5339.FocalPoint = [20, 20, 20]
keyFrame5339.ViewUp = [0.3893364618523633, -0.866, -0.31355561930017284]
keyFrame5339.ViewAngle = 30.0
keyFrame5339.ParallelScale = 0.97681
keyFrame5339.PositionPathPoints = [22.822564777116863, 20.0, 23.504729383232988]
keyFrame5339.FocalPathPoints = [20, 20, 20]
keyFrame5339.PositionMode = 'Path'
keyFrame5339.FocalPointMode = 'Path'
keyFrame5339.ClosedFocalPath = 0
keyFrame5339.ClosedPositionPath = 0

# ====================================================================
keyFrame5340 = CameraKeyFrame()
keyFrame5340.KeyTime = 0.85
keyFrame5340.KeyValues = [0.0]
keyFrame5340.Position = [22.82956858600238, 20.0, 23.499077248023955]
keyFrame5340.FocalPoint = [20, 20, 20]
keyFrame5340.ViewUp = [0.38870857232006467, -0.866, -0.3143336645873814]
keyFrame5340.ViewAngle = 30.0
keyFrame5340.ParallelScale = 0.97681
keyFrame5340.PositionPathPoints = [22.82956858600238, 20.0, 23.499077248023955]
keyFrame5340.FocalPathPoints = [20, 20, 20]
keyFrame5340.PositionMode = 'Path'
keyFrame5340.FocalPointMode = 'Path'
keyFrame5340.ClosedFocalPath = 0
keyFrame5340.ClosedPositionPath = 0

# ====================================================================
keyFrame5341 = CameraKeyFrame()
keyFrame5341.KeyTime = 0.8525
keyFrame5341.KeyValues = [0.0]
keyFrame5341.Position = [22.83656107661788, 20.0, 23.493411116510423]
keyFrame5341.FocalPoint = [20, 20, 20]
keyFrame5341.ViewUp = [0.388079127952745, -0.866, -0.3151104525396645]
keyFrame5341.ViewAngle = 30.0
keyFrame5341.ParallelScale = 0.97681
keyFrame5341.PositionPathPoints = [22.83656107661788, 20.0, 23.493411116510423]
keyFrame5341.FocalPathPoints = [20, 20, 20]
keyFrame5341.PositionMode = 'Path'
keyFrame5341.FocalPointMode = 'Path'
keyFrame5341.ClosedFocalPath = 0
keyFrame5341.ClosedPositionPath = 0

# ====================================================================
keyFrame5342 = CameraKeyFrame()
keyFrame5342.KeyTime = 0.855
keyFrame5342.KeyValues = [0.0]
keyFrame5342.Position = [22.84354222099396, 20.0, 23.487731011356658]
keyFrame5342.FocalPoint = [20, 20, 20]
keyFrame5342.ViewUp = [0.3874481312684256, -0.866, -0.31588598004990764]
keyFrame5342.ViewAngle = 30.0
keyFrame5342.ParallelScale = 0.97681
keyFrame5342.PositionPathPoints = [22.84354222099396, 20.0, 23.487731011356658]
keyFrame5342.FocalPathPoints = [20, 20, 20]
keyFrame5342.PositionMode = 'Path'
keyFrame5342.FocalPointMode = 'Path'
keyFrame5342.ClosedFocalPath = 0
keyFrame5342.ClosedPositionPath = 0

# ====================================================================
keyFrame5343 = CameraKeyFrame()
keyFrame5343.KeyTime = 0.8575
keyFrame5343.KeyValues = [0.0]
keyFrame5343.Position = [22.850511991206655, 20.0, 23.48203695528281]
keyFrame5343.FocalPoint = [20, 20, 20]
keyFrame5343.ViewUp = [0.3868155847913672, -0.866, -0.3166602440160489]
keyFrame5343.ViewAngle = 30.0
keyFrame5343.ParallelScale = 0.97681
keyFrame5343.PositionPathPoints = [22.850511991206655, 20.0, 23.48203695528281]
keyFrame5343.FocalPathPoints = [20, 20, 20]
keyFrame5343.PositionMode = 'Path'
keyFrame5343.FocalPointMode = 'Path'
keyFrame5343.ClosedFocalPath = 0
keyFrame5343.ClosedPositionPath = 0

# ====================================================================
keyFrame5344 = CameraKeyFrame()
keyFrame5344.KeyTime = 0.86
keyFrame5344.KeyValues = [0.0]
keyFrame5344.Position = [22.857470359377547, 20.0, 23.476328971064795]
keyFrame5344.FocalPoint = [20, 20, 20]
keyFrame5344.ViewUp = [0.38618149105206173, -0.866, -0.31743324134109263]
keyFrame5344.ViewAngle = 30.0
keyFrame5344.ParallelScale = 0.97681
keyFrame5344.PositionPathPoints = [22.857470359377547, 20.0, 23.476328971064795]
keyFrame5344.FocalPathPoints = [20, 20, 20]
keyFrame5344.PositionMode = 'Path'
keyFrame5344.FocalPointMode = 'Path'
keyFrame5344.ClosedFocalPath = 0
keyFrame5344.ClosedPositionPath = 0

# ====================================================================
keyFrame5345 = CameraKeyFrame()
keyFrame5345.KeyTime = 0.8625
keyFrame5345.KeyValues = [0.0]
keyFrame5345.Position = [22.864417297673874, 20.0, 23.470607081534233]
keyFrame5345.FocalPoint = [20, 20, 20]
keyFrame5345.ViewUp = [0.38554585258722335, -0.866, -0.3182049689331223]
keyFrame5345.ViewAngle = 30.0
keyFrame5345.ParallelScale = 0.97681
keyFrame5345.PositionPathPoints = [22.864417297673874, 20.0, 23.470607081534233]
keyFrame5345.FocalPathPoints = [20, 20, 20]
keyFrame5345.PositionMode = 'Path'
keyFrame5345.FocalPointMode = 'Path'
keyFrame5345.ClosedFocalPath = 0
keyFrame5345.ClosedPositionPath = 0

# ====================================================================
keyFrame5346 = CameraKeyFrame()
keyFrame5346.KeyTime = 0.865
keyFrame5346.KeyValues = [0.0]
keyFrame5346.Position = [22.871352778308648, 20.0, 23.46487130957832]
keyFrame5346.FocalPoint = [20, 20, 20]
keyFrame5346.ViewUp = [0.38490867193977985, -0.866, -0.3189754237053138]
keyFrame5346.ViewAngle = 30.0
keyFrame5346.ParallelScale = 0.97681
keyFrame5346.PositionPathPoints = [22.871352778308648, 20.0, 23.46487130957832]
keyFrame5346.FocalPathPoints = [20, 20, 20]
keyFrame5346.PositionMode = 'Path'
keyFrame5346.FocalPointMode = 'Path'
keyFrame5346.ClosedFocalPath = 0
keyFrame5346.ClosedPositionPath = 0

# ====================================================================
keyFrame5347 = CameraKeyFrame()
keyFrame5347.KeyTime = 0.8675
keyFrame5347.KeyValues = [0.0]
keyFrame5347.Position = [22.878276773540765, 20.0, 23.459121678139773]
keyFrame5347.FocalPoint = [20, 20, 20]
keyFrame5347.ViewUp = [0.38426995165886385, -0.866, -0.31974460257594856]
keyFrame5347.ViewAngle = 30.0
keyFrame5347.ParallelScale = 0.97681
keyFrame5347.PositionPathPoints = [22.878276773540765, 20.0, 23.459121678139773]
keyFrame5347.FocalPathPoints = [20, 20, 20]
keyFrame5347.PositionMode = 'Path'
keyFrame5347.FocalPointMode = 'Path'
keyFrame5347.ClosedFocalPath = 0
keyFrame5347.ClosedPositionPath = 0

# ====================================================================
keyFrame5348 = CameraKeyFrame()
keyFrame5348.KeyTime = 0.87
keyFrame5348.KeyValues = [0.0]
keyFrame5348.Position = [22.88518925567512, 20.0, 23.4533582102167]
keyFrame5348.FocalPoint = [20, 20, 20]
keyFrame5348.ViewUp = [0.3836296942998045, -0.866, -0.32051250246842694]
keyFrame5348.ViewAngle = 30.0
keyFrame5348.ParallelScale = 0.97681
keyFrame5348.PositionPathPoints = [22.88518925567512, 20.0, 23.4533582102167]
keyFrame5348.FocalPathPoints = [20, 20, 20]
keyFrame5348.PositionMode = 'Path'
keyFrame5348.FocalPointMode = 'Path'
keyFrame5348.ClosedFocalPath = 0
keyFrame5348.ClosedPositionPath = 0

# ====================================================================
keyFrame5349 = CameraKeyFrame()
keyFrame5349.KeyTime = 0.8725
keyFrame5349.KeyValues = [0.0]
keyFrame5349.Position = [22.89209019706272, 20.0, 23.447580928862536]
keyFrame5349.FocalPoint = [20, 20, 20]
keyFrame5349.ViewUp = [0.38298790242411823, -0.866, -0.32127912031128114]
keyFrame5349.ViewAngle = 30.0
keyFrame5349.ParallelScale = 0.97681
keyFrame5349.PositionPathPoints = [22.89209019706272, 20.0, 23.447580928862536]
keyFrame5349.FocalPathPoints = [20, 20, 20]
keyFrame5349.PositionMode = 'Path'
keyFrame5349.FocalPointMode = 'Path'
keyFrame5349.ClosedFocalPath = 0
keyFrame5349.ClosedPositionPath = 0

# ====================================================================
keyFrame5350 = CameraKeyFrame()
keyFrame5350.KeyTime = 0.875
keyFrame5350.KeyValues = [0.0]
keyFrame5350.Position = [22.898979570100803, 20.0, 23.441789857185938]
keyFrame5350.FocalPoint = [20, 20, 20]
keyFrame5350.ViewUp = [0.38234457859950055, -0.866, -0.3220444530381885]
keyFrame5350.ViewAngle = 30.0
keyFrame5350.ParallelScale = 0.97681
keyFrame5350.PositionPathPoints = [22.898979570100803, 20.0, 23.441789857185938]
keyFrame5350.FocalPathPoints = [20, 20, 20]
keyFrame5350.PositionMode = 'Path'
keyFrame5350.FocalPointMode = 'Path'
keyFrame5350.ClosedFocalPath = 0
keyFrame5350.ClosedPositionPath = 0

# ====================================================================
keyFrame5351 = CameraKeyFrame()
keyFrame5351.KeyTime = 0.8775
keyFrame5351.KeyValues = [0.0]
keyFrame5351.Position = [22.905857347232935, 20.0, 23.43598501835069]
keyFrame5351.FocalPoint = [20, 20, 20]
keyFrame5351.ViewUp = [0.38169972539981717, -0.866, -0.3228084975879848]
keyFrame5351.ViewAngle = 30.0
keyFrame5351.ParallelScale = 0.97681
keyFrame5351.PositionPathPoints = [22.905857347232935, 20.0, 23.43598501835069]
keyFrame5351.FocalPathPoints = [20, 20, 20]
keyFrame5351.PositionMode = 'Path'
keyFrame5351.FocalPointMode = 'Path'
keyFrame5351.ClosedFocalPath = 0
keyFrame5351.ClosedPositionPath = 0

# ====================================================================
keyFrame5352 = CameraKeyFrame()
keyFrame5352.KeyTime = 0.88
keyFrame5352.KeyValues = [0.0]
keyFrame5352.Position = [22.912723500949138, 20.0, 23.430166435575607]
keyFrame5352.FocalPoint = [20, 20, 20]
keyFrame5352.ViewUp = [0.38105334540509533, -0.866, -0.3235712509046771]
keyFrame5352.ViewAngle = 30.0
keyFrame5352.ParallelScale = 0.97681
keyFrame5352.PositionPathPoints = [22.912723500949138, 20.0, 23.430166435575607]
keyFrame5352.FocalPathPoints = [20, 20, 20]
keyFrame5352.PositionMode = 'Path'
keyFrame5352.FocalPointMode = 'Path'
keyFrame5352.ClosedFocalPath = 0
keyFrame5352.ClosedPositionPath = 0

# ====================================================================
keyFrame5353 = CameraKeyFrame()
keyFrame5353.KeyTime = 0.8825
keyFrame5353.KeyValues = [0.0]
keyFrame5353.Position = [22.919578003785993, 20.0, 23.424334132134447]
keyFrame5353.FocalPoint = [20, 20, 20]
keyFrame5353.ViewUp = [0.3804054412015152, -0.866, -0.3243327099374575]
keyFrame5353.ViewAngle = 30.0
keyFrame5353.ParallelScale = 0.97681
keyFrame5353.PositionPathPoints = [22.919578003785993, 20.0, 23.424334132134447]
keyFrame5353.FocalPathPoints = [20, 20, 20]
keyFrame5353.PositionMode = 'Path'
keyFrame5353.FocalPointMode = 'Path'
keyFrame5353.ClosedFocalPath = 0
keyFrame5353.ClosedPositionPath = 0

# ====================================================================
keyFrame5354 = CameraKeyFrame()
keyFrame5354.KeyTime = 0.885
keyFrame5354.KeyValues = [0.0]
keyFrame5354.Position = [22.926420828325327, 20.0, 23.418488131356543]
keyFrame5354.FocalPoint = [20, 20, 20]
keyFrame5354.ViewUp = [0.3797560153814011, -0.866, -0.3250928716407157]
keyFrame5354.ViewAngle = 30.0
keyFrame5354.ParallelScale = 0.97681
keyFrame5354.PositionPathPoints = [22.926420828325327, 20.0, 23.418488131356543]
keyFrame5354.FocalPathPoints = [20, 20, 20]
keyFrame5354.PositionMode = 'Path'
keyFrame5354.FocalPointMode = 'Path'
keyFrame5354.ClosedFocalPath = 0
keyFrame5354.ClosedPositionPath = 0

# ====================================================================
keyFrame5355 = CameraKeyFrame()
keyFrame5355.KeyTime = 0.8875
keyFrame5355.KeyValues = [0.0]
keyFrame5355.Position = [22.93325194718525, 20.0, 23.41262845663125]
keyFrame5355.FocalPoint = [20, 20, 20]
keyFrame5355.ViewUp = [0.37910507054321274, -0.866, -0.3258517329740527]
keyFrame5355.ViewAngle = 30.0
keyFrame5355.ParallelScale = 0.97681
keyFrame5355.PositionPathPoints = [22.93325194718525, 20.0, 23.41262845663125]
keyFrame5355.FocalPathPoints = [20, 20, 20]
keyFrame5355.PositionMode = 'Path'
keyFrame5355.FocalPointMode = 'Path'
keyFrame5355.ClosedFocalPath = 0
keyFrame5355.ClosedPositionPath = 0

# ====================================================================
keyFrame5356 = CameraKeyFrame()
keyFrame5356.KeyTime = 0.89
keyFrame5356.KeyValues = [0.0]
keyFrame5356.Position = [22.94007133303881, 20.0, 23.406755131398548]
keyFrame5356.FocalPoint = [20, 20, 20]
keyFrame5356.ViewUp = [0.37845260929153696, -0.866, -0.32660929090229346]
keyFrame5356.ViewAngle = 30.0
keyFrame5356.ParallelScale = 0.97681
keyFrame5356.PositionPathPoints = [22.94007133303881, 20.0, 23.406755131398548]
keyFrame5356.FocalPathPoints = [20, 20, 20]
keyFrame5356.PositionMode = 'Path'
keyFrame5356.FocalPointMode = 'Path'
keyFrame5356.ClosedFocalPath = 0
keyFrame5356.ClosedPositionPath = 0

# ====================================================================
keyFrame5357 = CameraKeyFrame()
keyFrame5357.KeyTime = 0.8925
keyFrame5357.KeyValues = [0.0]
keyFrame5357.Position = [22.94687895860836, 20.0, 23.400868179151814]
keyFrame5357.FocalPoint = [20, 20, 20]
keyFrame5357.ViewUp = [0.3777986342368258, -0.866, -0.3273655423954022]
keyFrame5357.ViewAngle = 30.0
keyFrame5357.ParallelScale = 0.97681
keyFrame5357.PositionPathPoints = [22.94687895860836, 20.0, 23.400868179151814]
keyFrame5357.FocalPathPoints = [20, 20, 20]
keyFrame5357.PositionMode = 'Path'
keyFrame5357.FocalPointMode = 'Path'
keyFrame5357.ClosedFocalPath = 0
keyFrame5357.ClosedPositionPath = 0

# ====================================================================
keyFrame5358 = CameraKeyFrame()
keyFrame5358.KeyTime = 0.895
keyFrame5358.KeyValues = [0.0]
keyFrame5358.Position = [22.953674796663307, 20.0, 23.394967623438923]
keyFrame5358.FocalPoint = [20, 20, 20]
keyFrame5358.ViewUp = [0.3771431479888792, -0.866, -0.32812048442595926]
keyFrame5358.ViewAngle = 30.0
keyFrame5358.ParallelScale = 0.97681
keyFrame5358.PositionPathPoints = [22.953674796663307, 20.0, 23.394967623438923]
keyFrame5358.FocalPathPoints = [20, 20, 20]
keyFrame5358.PositionMode = 'Path'
keyFrame5358.FocalPointMode = 'Path'
keyFrame5358.ClosedFocalPath = 0
keyFrame5358.ClosedPositionPath = 0

# ====================================================================
keyFrame5359 = CameraKeyFrame()
keyFrame5359.KeyTime = 0.8975
keyFrame5359.KeyValues = [0.0]
keyFrame5359.Position = [22.96045882002022, 20.0, 23.389053487862167]
keyFrame5359.FocalPoint = [20, 20, 20]
keyFrame5359.ViewUp = [0.37648615316664386, -0.866, -0.3288741139729954]
keyFrame5359.ViewAngle = 30.0
keyFrame5359.ParallelScale = 0.97681
keyFrame5359.PositionPathPoints = [22.96045882002022, 20.0, 23.389053487862167]
keyFrame5359.FocalPathPoints = [20, 20, 20]
keyFrame5359.PositionMode = 'Path'
keyFrame5359.FocalPointMode = 'Path'
keyFrame5359.ClosedFocalPath = 0
keyFrame5359.ClosedPositionPath = 0

# ====================================================================
keyFrame5360 = CameraKeyFrame()
keyFrame5360.KeyTime = 0.9
keyFrame5360.KeyValues = [0.0]
keyFrame5360.Position = [22.967231001542938, 20.0, 23.383125796078147]
keyFrame5360.FocalPoint = [20, 20, 20]
keyFrame5360.ViewUp = [0.37582765239801996, -0.866, -0.32962642802193326]
keyFrame5360.ViewAngle = 30.0
keyFrame5360.ParallelScale = 0.97681
keyFrame5360.PositionPathPoints = [22.967231001542938, 20.0, 23.383125796078147]
keyFrame5360.FocalPathPoints = [20, 20, 20]
keyFrame5360.PositionMode = 'Path'
keyFrame5360.FocalPointMode = 'Path'
keyFrame5360.ClosedFocalPath = 0
keyFrame5360.ClosedPositionPath = 0

# ====================================================================
keyFrame5361 = CameraKeyFrame()
keyFrame5361.KeyTime = 0.9025
keyFrame5361.KeyValues = [0.0]
keyFrame5361.Position = [22.973991314142662, 20.0, 23.37718457179768]
keyFrame5361.FocalPoint = [20, 20, 20]
keyFrame5361.ViewUp = [0.37516764831694227, -0.866, -0.3303774235634668]
keyFrame5361.ViewAngle = 30.0
keyFrame5361.ParallelScale = 0.97681
keyFrame5361.PositionPathPoints = [22.973991314142662, 20.0, 23.37718457179768]
keyFrame5361.FocalPathPoints = [20, 20, 20]
keyFrame5361.PositionMode = 'Path'
keyFrame5361.FocalPointMode = 'Path'
keyFrame5361.ClosedFocalPath = 0
keyFrame5361.ClosedPositionPath = 0

# ====================================================================
keyFrame5362 = CameraKeyFrame()
keyFrame5362.KeyTime = 0.905
keyFrame5362.KeyValues = [0.0]
keyFrame5362.Position = [22.980739730778087, 20.0, 23.37122983878571]
keyFrame5362.FocalPoint = [20, 20, 20]
keyFrame5362.ViewUp = [0.3745061435633703, -0.866, -0.3311270975935735]
keyFrame5362.ViewAngle = 30.0
keyFrame5362.ParallelScale = 0.97681
keyFrame5362.PositionPathPoints = [22.980739730778087, 20.0, 23.37122983878571]
keyFrame5362.FocalPathPoints = [20, 20, 20]
keyFrame5362.PositionMode = 'Path'
keyFrame5362.FocalPointMode = 'Path'
keyFrame5362.ClosedFocalPath = 0
keyFrame5362.ClosedPositionPath = 0

# ====================================================================
keyFrame5363 = CameraKeyFrame()
keyFrame5363.KeyTime = 0.9075
keyFrame5363.KeyValues = [0.0]
keyFrame5363.Position = [22.98747622445551, 20.0, 23.3652616208612]
keyFrame5363.FocalPoint = [20, 20, 20]
keyFrame5363.ViewUp = [0.37384314078327885, -0.866, -0.33187544711352807]
keyFrame5363.ViewAngle = 30.0
keyFrame5363.ParallelScale = 0.97681
keyFrame5363.PositionPathPoints = [22.98747622445551, 20.0, 23.3652616208612]
keyFrame5363.FocalPathPoints = [20, 20, 20]
keyFrame5363.PositionMode = 'Path'
keyFrame5363.FocalPointMode = 'Path'
keyFrame5363.ClosedFocalPath = 0
keyFrame5363.ClosedPositionPath = 0

# ====================================================================
keyFrame5364 = CameraKeyFrame()
keyFrame5364.KeyTime = 0.91
keyFrame5364.KeyValues = [0.0]
keyFrame5364.Position = [22.994200768228914, 20.0, 23.359279941897057]
keyFrame5364.FocalPoint = [20, 20, 20]
keyFrame5364.ViewUp = [0.37317864262864836, -0.866, -0.33262246912991433]
keyFrame5364.ViewAngle = 30.0
keyFrame5364.ParallelScale = 0.97681
keyFrame5364.PositionPathPoints = [22.994200768228914, 20.0, 23.359279941897057]
keyFrame5364.FocalPathPoints = [20, 20, 20]
keyFrame5364.PositionMode = 'Path'
keyFrame5364.FocalPointMode = 'Path'
keyFrame5364.ClosedFocalPath = 0
keyFrame5364.ClosedPositionPath = 0

# ====================================================================
keyFrame5365 = CameraKeyFrame()
keyFrame5365.KeyTime = 0.9125
keyFrame5365.KeyValues = [0.0]
keyFrame5365.Position = [23.000913335200117, 20.0, 23.353284825820012]
keyFrame5365.FocalPoint = [20, 20, 20]
keyFrame5365.ViewUp = [0.3725126517574555, -0.866, -0.33336816065463887]
keyFrame5365.ViewAngle = 30.0
keyFrame5365.ParallelScale = 0.97681
keyFrame5365.PositionPathPoints = [23.000913335200117, 20.0, 23.353284825820012]
keyFrame5365.FocalPathPoints = [20, 20, 20]
keyFrame5365.PositionMode = 'Path'
keyFrame5365.FocalPointMode = 'Path'
keyFrame5365.ClosedFocalPath = 0
keyFrame5365.ClosedPositionPath = 0

# ====================================================================
keyFrame5366 = CameraKeyFrame()
keyFrame5366.KeyTime = 0.915
keyFrame5366.KeyValues = [0.0]
keyFrame5366.Position = [23.007613898518837, 20.0, 23.347276296610538]
keyFrame5366.FocalPoint = [20, 20, 20]
keyFrame5366.ViewUp = [0.37184517083366353, -0.866, -0.33411251870494335]
keyFrame5366.ViewAngle = 30.0
keyFrame5366.ParallelScale = 0.97681
keyFrame5366.PositionPathPoints = [23.007613898518837, 20.0, 23.347276296610538]
keyFrame5366.FocalPathPoints = [20, 20, 20]
keyFrame5366.PositionMode = 'Path'
keyFrame5366.FocalPointMode = 'Path'
keyFrame5366.ClosedFocalPath = 0
keyFrame5366.ClosedPositionPath = 0

# ====================================================================
keyFrame5367 = CameraKeyFrame()
keyFrame5367.KeyTime = 0.9175
keyFrame5367.KeyValues = [0.0]
keyFrame5367.Position = [23.014302431382838, 20.0, 23.341254378302743]
keyFrame5367.FocalPoint = [20, 20, 20]
keyFrame5367.ViewUp = [0.3711762025272127, -0.866, -0.3348555403034177]
keyFrame5367.ViewAngle = 30.0
keyFrame5367.ParallelScale = 0.97681
keyFrame5367.PositionPathPoints = [23.014302431382838, 20.0, 23.341254378302743]
keyFrame5367.FocalPathPoints = [20, 20, 20]
keyFrame5367.PositionMode = 'Path'
keyFrame5367.FocalPointMode = 'Path'
keyFrame5367.ClosedFocalPath = 0
keyFrame5367.ClosedPositionPath = 0

# ====================================================================
keyFrame5368 = CameraKeyFrame()
keyFrame5368.KeyTime = 0.92
keyFrame5368.KeyValues = [0.0]
keyFrame5368.Position = [23.020978907038014, 20.0, 23.335219094984293]
keyFrame5368.FocalPoint = [20, 20, 20]
keyFrame5368.ViewUp = [0.3705057495140106, -0.866, -0.33559722247801266]
keyFrame5368.ViewAngle = 30.0
keyFrame5368.ParallelScale = 0.97681
keyFrame5368.PositionPathPoints = [23.020978907038014, 20.0, 23.335219094984293]
keyFrame5368.FocalPathPoints = [20, 20, 20]
keyFrame5368.PositionMode = 'Path'
keyFrame5368.FocalPointMode = 'Path'
keyFrame5368.ClosedFocalPath = 0
keyFrame5368.ClosedPositionPath = 0

# ====================================================================
keyFrame5369 = CameraKeyFrame()
keyFrame5369.KeyTime = 0.9225
keyFrame5369.KeyValues = [0.0]
keyFrame5369.Position = [23.02764329877851, 20.0, 23.329170470796285]
keyFrame5369.FocalPoint = [20, 20, 20]
keyFrame5369.ViewUp = [0.36983381447592295, -0.866, -0.33633756226205286]
keyFrame5369.ViewAngle = 30.0
keyFrame5369.ParallelScale = 0.97681
keyFrame5369.PositionPathPoints = [23.02764329877851, 20.0, 23.329170470796285]
keyFrame5369.FocalPathPoints = [20, 20, 20]
keyFrame5369.PositionMode = 'Path'
keyFrame5369.FocalPointMode = 'Path'
keyFrame5369.ClosedFocalPath = 0
keyFrame5369.ClosedPositionPath = 0

# ====================================================================
keyFrame5370 = CameraKeyFrame()
keyFrame5370.KeyTime = 0.925
keyFrame5370.KeyValues = [0.0]
keyFrame5370.Position = [23.034295579946818, 20.0, 23.323108529933183]
keyFrame5370.FocalPoint = [20, 20, 20]
keyFrame5370.ViewUp = [0.3691604001007637, -0.866, -0.3370765566942495]
keyFrame5370.ViewAngle = 30.0
keyFrame5370.ParallelScale = 0.97681
keyFrame5370.PositionPathPoints = [23.034295579946818, 20.0, 23.323108529933183]
keyFrame5370.FocalPathPoints = [20, 20, 20]
keyFrame5370.PositionMode = 'Path'
keyFrame5370.FocalPointMode = 'Path'
keyFrame5370.ClosedFocalPath = 0
keyFrame5370.ClosedPositionPath = 0

# ====================================================================
keyFrame5371 = CameraKeyFrame()
keyFrame5371.KeyTime = 0.9275
keyFrame5371.KeyValues = [0.0]
keyFrame5371.Position = [23.040935723933895, 20.0, 23.317033296642684]
keyFrame5371.FocalPoint = [20, 20, 20]
keyFrame5371.ViewUp = [0.3684855090822855, -0.866, -0.3378142028187133]
keyFrame5371.ViewAngle = 30.0
keyFrame5371.ParallelScale = 0.97681
keyFrame5371.PositionPathPoints = [23.040935723933895, 20.0, 23.317033296642684]
keyFrame5371.FocalPathPoints = [20, 20, 20]
keyFrame5371.PositionMode = 'Path'
keyFrame5371.FocalPointMode = 'Path'
keyFrame5371.ClosedFocalPath = 0
keyFrame5371.ClosedPositionPath = 0

# ====================================================================
keyFrame5372 = CameraKeyFrame()
keyFrame5372.KeyTime = 0.93
keyFrame5372.KeyValues = [0.0]
keyFrame5372.Position = [23.047563704179275, 20.0, 23.310944795225655]
keyFrame5372.FocalPoint = [20, 20, 20]
keyFrame5372.ViewUp = [0.36780914412017035, -0.866, -0.3385504976849673]
keyFrame5372.ViewAngle = 30.0
keyFrame5372.ParallelScale = 0.97681
keyFrame5372.PositionPathPoints = [23.047563704179275, 20.0, 23.310944795225655]
keyFrame5372.FocalPathPoints = [20, 20, 20]
keyFrame5372.PositionMode = 'Path'
keyFrame5372.FocalPointMode = 'Path'
keyFrame5372.ClosedFocalPath = 0
keyFrame5372.ClosedPositionPath = 0

# ====================================================================
keyFrame5373 = CameraKeyFrame()
keyFrame5373.KeyTime = 0.9325
keyFrame5373.KeyValues = [0.0]
keyFrame5373.Position = [23.054179494171162, 20.0, 23.30484305003601]
keyFrame5373.FocalPoint = [20, 20, 20]
keyFrame5373.ViewUp = [0.3671313079200199, -0.866, -0.3392854383479597]
keyFrame5373.ViewAngle = 30.0
keyFrame5373.ParallelScale = 0.97681
keyFrame5373.PositionPathPoints = [23.054179494171162, 20.0, 23.30484305003601]
keyFrame5373.FocalPathPoints = [20, 20, 20]
keyFrame5373.PositionMode = 'Path'
keyFrame5373.FocalPointMode = 'Path'
keyFrame5373.ClosedFocalPath = 0
keyFrame5373.ClosedPositionPath = 0

# ====================================================================
keyFrame5374 = CameraKeyFrame()
keyFrame5374.KeyTime = 0.935
keyFrame5374.KeyValues = [0.0]
keyFrame5374.Position = [23.060783067446547, 20.0, 23.298728085480622]
keyFrame5374.FocalPoint = [20, 20, 20]
keyFrame5374.ViewUp = [0.3664520031933458, -0.866, -0.34001902186807664]
keyFrame5374.ViewAngle = 30.0
keyFrame5374.ParallelScale = 0.97681
keyFrame5374.PositionPathPoints = [23.060783067446547, 20.0, 23.298728085480622]
keyFrame5374.FocalPathPoints = [20, 20, 20]
keyFrame5374.PositionMode = 'Path'
keyFrame5374.FocalPointMode = 'Path'
keyFrame5374.ClosedFocalPath = 0
keyFrame5374.ClosedPositionPath = 0

# ====================================================================
keyFrame5375 = CameraKeyFrame()
keyFrame5375.KeyTime = 0.9375
keyFrame5375.KeyValues = [0.0]
keyFrame5375.Position = [23.06737439759131, 20.0, 23.29259992601923]
keyFrame5375.FocalPoint = [20, 20, 20]
keyFrame5375.ViewUp = [0.3657712326575604, -0.866, -0.3407512453111552]
keyFrame5375.ViewAngle = 30.0
keyFrame5375.ParallelScale = 0.97681
keyFrame5375.PositionPathPoints = [23.06737439759131, 20.0, 23.29259992601923]
keyFrame5375.FocalPathPoints = [20, 20, 20]
keyFrame5375.PositionMode = 'Path'
keyFrame5375.FocalPointMode = 'Path'
keyFrame5375.ClosedFocalPath = 0
keyFrame5375.ClosedPositionPath = 0

# ====================================================================
keyFrame5376 = CameraKeyFrame()
keyFrame5376.KeyTime = 0.94
keyFrame5376.KeyValues = [0.0]
keyFrame5376.Position = [23.073953458240332, 20.0, 23.28645859616432]
keyFrame5376.FocalPoint = [20, 20, 20]
keyFrame5376.ViewUp = [0.3650889990359668, -0.866, -0.341482105748496]
keyFrame5376.ViewAngle = 30.0
keyFrame5376.ParallelScale = 0.97681
keyFrame5376.PositionPathPoints = [23.073953458240332, 20.0, 23.28645859616432]
keyFrame5376.FocalPathPoints = [20, 20, 20]
keyFrame5376.PositionMode = 'Path'
keyFrame5376.FocalPointMode = 'Path'
keyFrame5376.ClosedFocalPath = 0
keyFrame5376.ClosedPositionPath = 0

# ====================================================================
keyFrame5377 = CameraKeyFrame()
keyFrame5377.KeyTime = 0.9425
keyFrame5377.KeyValues = [0.0]
keyFrame5377.Position = [23.080520223077606, 20.0, 23.28030412048105]
keyFrame5377.FocalPoint = [20, 20, 20]
keyFrame5377.ViewUp = [0.36440530505774976, -0.866, -0.3422116002568764]
keyFrame5377.ViewAngle = 30.0
keyFrame5377.ParallelScale = 0.97681
keyFrame5377.PositionPathPoints = [23.080520223077606, 20.0, 23.28030412048105]
keyFrame5377.FocalPathPoints = [20, 20, 20]
keyFrame5377.PositionMode = 'Path'
keyFrame5377.FocalPointMode = 'Path'
keyFrame5377.ClosedFocalPath = 0
keyFrame5377.ClosedPositionPath = 0

# ====================================================================
keyFrame5378 = CameraKeyFrame()
keyFrame5378.KeyTime = 0.945
keyFrame5378.KeyValues = [0.0]
keyFrame5378.Position = [23.087074665836326, 20.0, 23.274136523587128]
keyFrame5378.FocalPoint = [20, 20, 20]
keyFrame5378.ViewUp = [0.36372015345796577, -0.866, -0.3429397259185629]
keyFrame5378.ViewAngle = 30.0
keyFrame5378.ParallelScale = 0.97681
keyFrame5378.PositionPathPoints = [23.087074665836326, 20.0, 23.274136523587128]
keyFrame5378.FocalPathPoints = [20, 20, 20]
keyFrame5378.PositionMode = 'Path'
keyFrame5378.FocalPointMode = 'Path'
keyFrame5378.ClosedFocalPath = 0
keyFrame5378.ClosedPositionPath = 0

# ====================================================================
keyFrame5379 = CameraKeyFrame()
keyFrame5379.KeyTime = 0.9475
keyFrame5379.KeyValues = [0.0]
keyFrame5379.Position = [23.093616760299017, 20.0, 23.26795583015274]
keyFrame5379.FocalPoint = [20, 20, 20]
keyFrame5379.ViewUp = [0.36303354697753354, -0.866, -0.3436664798213243]
keyFrame5379.ViewAngle = 30.0
keyFrame5379.ParallelScale = 0.97681
keyFrame5379.PositionPathPoints = [23.093616760299017, 20.0, 23.26795583015274]
keyFrame5379.FocalPathPoints = [20, 20, 20]
keyFrame5379.PositionMode = 'Path'
keyFrame5379.FocalPointMode = 'Path'
keyFrame5379.ClosedFocalPath = 0
keyFrame5379.ClosedPositionPath = 0

# ====================================================================
keyFrame5380 = CameraKeyFrame()
keyFrame5380.KeyTime = 0.95
keyFrame5380.KeyValues = [0.0]
keyFrame5380.Position = [23.10014648029762, 20.0, 23.26176206490042]
keyFrame5380.FocalPoint = [20, 20, 20]
keyFrame5380.ViewUp = [0.3623454883632247, -0.866, -0.3443918590584445]
keyFrame5380.ViewAngle = 30.0
keyFrame5380.ParallelScale = 0.97681
keyFrame5380.PositionPathPoints = [23.10014648029762, 20.0, 23.26176206490042]
keyFrame5380.FocalPathPoints = [20, 20, 20]
keyFrame5380.PositionMode = 'Path'
keyFrame5380.FocalPointMode = 'Path'
keyFrame5380.ClosedFocalPath = 0
keyFrame5380.ClosedPositionPath = 0

# ====================================================================
keyFrame5381 = CameraKeyFrame()
keyFrame5381.KeyTime = 0.9525
keyFrame5381.KeyValues = [0.0]
keyFrame5381.Position = [23.106663799713616, 20.0, 23.255555252604967]
keyFrame5381.FocalPoint = [20, 20, 20]
keyFrame5381.ViewUp = [0.361655980367654, -0.866, -0.34511586072873524]
keyFrame5381.ViewAngle = 30.0
keyFrame5381.ParallelScale = 0.97681
keyFrame5381.PositionPathPoints = [23.106663799713616, 20.0, 23.255555252604967]
keyFrame5381.FocalPathPoints = [20, 20, 20]
keyFrame5381.PositionMode = 'Path'
keyFrame5381.FocalPointMode = 'Path'
keyFrame5381.ClosedFocalPath = 0
keyFrame5381.ClosedPositionPath = 0

# ====================================================================
keyFrame5382 = CameraKeyFrame()
keyFrame5382.KeyTime = 0.955
keyFrame5382.KeyValues = [0.0]
keyFrame5382.Position = [23.11316869247812, 20.0, 23.249335418093345]
keyFrame5382.FocalPoint = [20, 20, 20]
keyFrame5382.ViewUp = [0.3609650257492697, -0.866, -0.34583848193654887]
keyFrame5382.ViewAngle = 30.0
keyFrame5382.ParallelScale = 0.97681
keyFrame5382.PositionPathPoints = [23.11316869247812, 20.0, 23.249335418093345]
keyFrame5382.FocalPathPoints = [20, 20, 20]
keyFrame5382.PositionMode = 'Path'
keyFrame5382.FocalPointMode = 'Path'
keyFrame5382.ClosedFocalPath = 0
keyFrame5382.ClosedPositionPath = 0

# ====================================================================
keyFrame5383 = CameraKeyFrame()
keyFrame5383.KeyTime = 0.9575
keyFrame5383.KeyValues = [0.0]
keyFrame5383.Position = [23.119661132571988, 20.0, 23.24310258624458]
keyFrame5383.FocalPoint = [20, 20, 20]
keyFrame5383.ViewUp = [0.3602726272723442, -0.866, -0.34655971979179157]
keyFrame5383.ViewAngle = 30.0
keyFrame5383.ParallelScale = 0.97681
keyFrame5383.PositionPathPoints = [23.119661132571988, 20.0, 23.24310258624458]
keyFrame5383.FocalPathPoints = [20, 20, 20]
keyFrame5383.PositionMode = 'Path'
keyFrame5383.FocalPointMode = 'Path'
keyFrame5383.ClosedFocalPath = 0
keyFrame5383.ClosedPositionPath = 0

# ====================================================================
keyFrame5384 = CameraKeyFrame()
keyFrame5384.KeyTime = 0.96
keyFrame5384.KeyValues = [0.0]
keyFrame5384.Position = [23.126141094025932, 20.0, 23.236856781989644]
keyFrame5384.FocalPoint = [20, 20, 20]
keyFrame5384.ViewUp = [0.3595787877069644, -0.866, -0.3472795714099357]
keyFrame5384.ViewAngle = 30.0
keyFrame5384.ParallelScale = 0.97681
keyFrame5384.PositionPathPoints = [23.126141094025932, 20.0, 23.236856781989644]
keyFrame5384.FocalPathPoints = [20, 20, 20]
keyFrame5384.PositionMode = 'Path'
keyFrame5384.FocalPointMode = 'Path'
keyFrame5384.ClosedFocalPath = 0
keyFrame5384.ClosedPositionPath = 0

# ====================================================================
keyFrame5385 = CameraKeyFrame()
keyFrame5385.KeyTime = 0.9625
keyFrame5385.KeyValues = [0.0]
keyFrame5385.Position = [23.13260855092062, 20.0, 23.230598030311388]
keyFrame5385.FocalPoint = [20, 20, 20]
keyFrame5385.ViewUp = [0.35888350982902206, -0.866, -0.347998033912033]
keyFrame5385.ViewAngle = 30.0
keyFrame5385.ParallelScale = 0.97681
keyFrame5385.PositionPathPoints = [23.13260855092062, 20.0, 23.230598030311388]
keyFrame5385.FocalPathPoints = [20, 20, 20]
keyFrame5385.PositionMode = 'Path'
keyFrame5385.FocalPointMode = 'Path'
keyFrame5385.ClosedFocalPath = 0
keyFrame5385.ClosedPositionPath = 0

# ====================================================================
keyFrame5386 = CameraKeyFrame()
keyFrame5386.KeyTime = 0.965
keyFrame5386.KeyValues = [0.0]
keyFrame5386.Position = [23.139063477386774, 20.0, 23.224326356244404]
keyFrame5386.FocalPoint = [20, 20, 20]
keyFrame5386.ViewUp = [0.35818679642020446, -0.866, -0.3487151044247272]
keyFrame5386.ViewAngle = 30.0
keyFrame5386.ParallelScale = 0.97681
keyFrame5386.PositionPathPoints = [23.139063477386774, 20.0, 23.224326356244404]
keyFrame5386.FocalPathPoints = [20, 20, 20]
keyFrame5386.PositionMode = 'Path'
keyFrame5386.FocalPointMode = 'Path'
keyFrame5386.ClosedFocalPath = 0
keyFrame5386.ClosedPositionPath = 0

# ====================================================================
keyFrame5387 = CameraKeyFrame()
keyFrame5387.KeyTime = 0.9675
keyFrame5387.KeyValues = [0.0]
keyFrame5387.Position = [23.14550584760529, 20.0, 23.218041784874956]
keyFrame5387.FocalPoint = [20, 20, 20]
keyFrame5387.ViewUp = [0.3574886502679845, -0.866, -0.349430780080267]
keyFrame5387.ViewAngle = 30.0
keyFrame5387.ParallelScale = 0.97681
keyFrame5387.PositionPathPoints = [23.14550584760529, 20.0, 23.218041784874956]
keyFrame5387.FocalPathPoints = [20, 20, 20]
keyFrame5387.PositionMode = 'Path'
keyFrame5387.FocalPointMode = 'Path'
keyFrame5387.ClosedFocalPath = 0
keyFrame5387.ClosedPositionPath = 0

# ====================================================================
keyFrame5388 = CameraKeyFrame()
keyFrame5388.KeyTime = 0.97
keyFrame5388.KeyValues = [0.0]
keyFrame5388.Position = [23.15193563580733, 20.0, 23.211744341340843]
keyFrame5388.FocalPoint = [20, 20, 20]
keyFrame5388.ViewUp = [0.3567890741656115, -0.866, -0.350145058016519]
keyFrame5388.ViewAngle = 30.0
keyFrame5388.ParallelScale = 0.97681
keyFrame5388.PositionPathPoints = [23.15193563580733, 20.0, 23.211744341340843]
keyFrame5388.FocalPathPoints = [20, 20, 20]
keyFrame5388.PositionMode = 'Path'
keyFrame5388.FocalPointMode = 'Path'
keyFrame5388.ClosedFocalPath = 0
keyFrame5388.ClosedPositionPath = 0

# ====================================================================
keyFrame5389 = CameraKeyFrame()
keyFrame5389.KeyTime = 0.9725
keyFrame5389.KeyValues = [0.0]
keyFrame5389.Position = [23.158352816274437, 20.0, 23.205434050831332]
keyFrame5389.FocalPoint = [20, 20, 20]
keyFrame5389.ViewUp = [0.35608807091210143, -0.866, -0.35085793537698035]
keyFrame5389.ViewAngle = 30.0
keyFrame5389.ParallelScale = 0.97681
keyFrame5389.PositionPathPoints = [23.158352816274437, 20.0, 23.205434050831332]
keyFrame5389.FocalPathPoints = [20, 20, 20]
keyFrame5389.PositionMode = 'Path'
keyFrame5389.FocalPointMode = 'Path'
keyFrame5389.ClosedFocalPath = 0
keyFrame5389.ClosedPositionPath = 0

# ====================================================================
keyFrame5390 = CameraKeyFrame()
keyFrame5390.KeyTime = 0.975
keyFrame5390.KeyValues = [0.0]
keyFrame5390.Position = [23.164757363338634, 20.0, 23.199110938587037]
keyFrame5390.FocalPoint = [20, 20, 20]
keyFrame5390.ViewUp = [0.3553856433122273, -0.866, -0.35156940931079145]
keyFrame5390.ViewAngle = 30.0
keyFrame5390.ParallelScale = 0.97681
keyFrame5390.PositionPathPoints = [23.164757363338634, 20.0, 23.199110938587037]
keyFrame5390.FocalPathPoints = [20, 20, 20]
keyFrame5390.PositionMode = 'Path'
keyFrame5390.FocalPointMode = 'Path'
keyFrame5390.ClosedFocalPath = 0
keyFrame5390.ClosedPositionPath = 0

# ====================================================================
keyFrame5391 = CameraKeyFrame()
keyFrame5391.KeyTime = 0.9775
keyFrame5391.KeyValues = [0.0]
keyFrame5391.Position = [23.171149251382527, 20.0, 23.192775029899806]
keyFrame5391.FocalPoint = [20, 20, 20]
keyFrame5391.ViewUp = [0.35468179417650975, -0.866, -0.35227947697274925]
keyFrame5391.ViewAngle = 30.0
keyFrame5391.ParallelScale = 0.97681
keyFrame5391.PositionPathPoints = [23.171149251382527, 20.0, 23.192775029899806]
keyFrame5391.FocalPathPoints = [20, 20, 20]
keyFrame5391.PositionMode = 'Path'
keyFrame5391.FocalPointMode = 'Path'
keyFrame5391.ClosedFocalPath = 0
keyFrame5391.ClosedPositionPath = 0

# ====================================================================
keyFrame5392 = CameraKeyFrame()
keyFrame5392.KeyTime = 0.98
keyFrame5392.KeyValues = [0.0]
keyFrame5392.Position = [23.17752845483942, 20.0, 23.186426350112654]
keyFrame5392.FocalPoint = [20, 20, 20]
keyFrame5392.ViewUp = [0.3539765263212075, -0.866, -0.3529881355233198]
keyFrame5392.ViewAngle = 30.0
keyFrame5392.ParallelScale = 0.97681
keyFrame5392.PositionPathPoints = [23.17752845483942, 20.0, 23.186426350112654]
keyFrame5392.FocalPathPoints = [20, 20, 20]
keyFrame5392.PositionMode = 'Path'
keyFrame5392.FocalPointMode = 'Path'
keyFrame5392.ClosedFocalPath = 0
keyFrame5392.ClosedPositionPath = 0

# ====================================================================
keyFrame5393 = CameraKeyFrame()
keyFrame5393.KeyTime = 0.9825
keyFrame5393.KeyValues = [0.0]
keyFrame5393.Position = [23.183894948193398, 20.0, 23.180064924619618]
keyFrame5393.FocalPoint = [20, 20, 20]
keyFrame5393.ViewUp = [0.3532698425661947, -0.866, -0.35369538212684065]
keyFrame5393.ViewAngle = 30.0
keyFrame5393.ParallelScale = 0.97681
keyFrame5393.PositionPathPoints = [23.183894948193398, 20.0, 23.180064924619618]
keyFrame5393.FocalPathPoints = [20, 20, 20]
keyFrame5393.PositionMode = 'Path'
keyFrame5393.FocalPointMode = 'Path'
keyFrame5393.ClosedFocalPath = 0
keyFrame5393.ClosedPositionPath = 0

# ====================================================================
keyFrame5394 = CameraKeyFrame()
keyFrame5394.KeyTime = 0.985
keyFrame5394.KeyValues = [0.0]
keyFrame5394.Position = [23.190248705979464, 20.0, 23.17369077886568]
keyFrame5394.FocalPoint = [20, 20, 20]
keyFrame5394.ViewUp = [0.35256174573105914, -0.866, -0.3544012139481987]
keyFrame5394.ViewAngle = 30.0
keyFrame5394.ParallelScale = 0.97681
keyFrame5394.PositionPathPoints = [23.190248705979464, 20.0, 23.17369077886568]
keyFrame5394.FocalPathPoints = [20, 20, 20]
keyFrame5394.PositionMode = 'Path'
keyFrame5394.FocalPointMode = 'Path'
keyFrame5394.ClosedFocalPath = 0
keyFrame5394.ClosedPositionPath = 0

# ====================================================================
keyFrame5395 = CameraKeyFrame()
keyFrame5395.KeyTime = 0.9875
keyFrame5395.KeyValues = [0.0]
keyFrame5395.Position = [23.196589702783616, 20.0, 23.167303938346667]
keyFrame5395.FocalPoint = [20, 20, 20]
keyFrame5395.ViewUp = [0.35185223864744053, -0.866, -0.35510562816342284]
keyFrame5395.ViewAngle = 30.0
keyFrame5395.ParallelScale = 0.97681
keyFrame5395.PositionPathPoints = [23.196589702783616, 20.0, 23.167303938346667]
keyFrame5395.FocalPathPoints = [20, 20, 20]
keyFrame5395.PositionMode = 'Path'
keyFrame5395.FocalPointMode = 'Path'
keyFrame5395.ClosedFocalPath = 0
keyFrame5395.ClosedPositionPath = 0

# ====================================================================
keyFrame5396 = CameraKeyFrame()
keyFrame5396.KeyTime = 0.99
keyFrame5396.KeyValues = [0.0]
keyFrame5396.Position = [23.202917913242953, 20.0, 23.160904428609115]
keyFrame5396.FocalPoint = [20, 20, 20]
keyFrame5396.ViewUp = [0.3511413241532959, -0.866, -0.35580862195479196]
keyFrame5396.ViewAngle = 30.0
keyFrame5396.ParallelScale = 0.97681
keyFrame5396.PositionPathPoints = [23.202917913242953, 20.0, 23.160904428609115]
keyFrame5396.FocalPathPoints = [20, 20, 20]
keyFrame5396.PositionMode = 'Path'
keyFrame5396.FocalPointMode = 'Path'
keyFrame5396.ClosedFocalPath = 0
keyFrame5396.ClosedPositionPath = 0

# ====================================================================
keyFrame5397 = CameraKeyFrame()
keyFrame5397.KeyTime = 0.9925
keyFrame5397.KeyValues = [0.0]
keyFrame5397.Position = [23.209233312045516, 20.0, 23.15449227525042]
keyFrame5397.FocalPoint = [20, 20, 20]
keyFrame5397.ViewUp = [0.35042900509222186, -0.866, -0.3565101925102746]
keyFrame5397.ViewAngle = 30.0
keyFrame5397.ParallelScale = 0.97681
keyFrame5397.PositionPathPoints = [23.209233312045516, 20.0, 23.15449227525042]
keyFrame5397.FocalPathPoints = [20, 20, 20]
keyFrame5397.PositionMode = 'Path'
keyFrame5397.FocalPointMode = 'Path'
keyFrame5397.ClosedFocalPath = 0
keyFrame5397.ClosedPositionPath = 0

# ====================================================================
keyFrame5398 = CameraKeyFrame()
keyFrame5398.KeyTime = 0.995
keyFrame5398.KeyValues = [0.0]
keyFrame5398.Position = [23.21553587392132, 20.0, 23.148067503925517]
keyFrame5398.FocalPoint = [20, 20, 20]
keyFrame5398.ViewUp = [0.3497152843134437, -0.866, -0.35721033702354127]
keyFrame5398.ViewAngle = 30.0
keyFrame5398.ParallelScale = 0.97681
keyFrame5398.PositionPathPoints = [23.21553587392132, 20.0, 23.148067503925517]
keyFrame5398.FocalPathPoints = [20, 20, 20]
keyFrame5398.PositionMode = 'Path'
keyFrame5398.FocalPointMode = 'Path'
keyFrame5398.ClosedFocalPath = 0
keyFrame5398.ClosedPositionPath = 0

# ====================================================================
keyFrame5399 = CameraKeyFrame()
keyFrame5399.KeyTime = 0.9975
keyFrame5399.KeyValues = [0.0]
keyFrame5399.Position = [23.221825573655636, 20.0, 23.141630140336865]
keyFrame5399.FocalPoint = [20, 20, 20]
keyFrame5399.ViewUp = [0.34900016467180545, -0.866, -0.3579090526939764]
keyFrame5399.ViewAngle = 30.0
keyFrame5399.ParallelScale = 0.97681
keyFrame5399.PositionPathPoints = [23.221825573655636, 20.0, 23.141630140336865]
keyFrame5399.FocalPathPoints = [20, 20, 20]
keyFrame5399.PositionMode = 'Path'
keyFrame5399.FocalPointMode = 'Path'
keyFrame5399.ClosedFocalPath = 0
keyFrame5399.ClosedPositionPath = 0

# ====================================================================
keyFrame5400 = CameraKeyFrame()
keyFrame5400.KeyTime = 1.0
keyFrame5400.KeyValues = [0.0]
keyFrame5400.Position = [23.228102386089574, 20.0, 23.135180210234005]
keyFrame5400.FocalPoint = [20, 20, 20]
keyFrame5400.ViewUp = [0.3482836490277591, -0.866, -0.3586063367266904]
keyFrame5400.ViewAngle = 30.0
keyFrame5400.ParallelScale = 0.97681
keyFrame5400.PositionPathPoints = [23.228102386089574, 20.0, 23.135180210234005]
keyFrame5400.FocalPathPoints = [20, 20, 20]
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
