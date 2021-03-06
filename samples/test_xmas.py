"""
This test is a ludicrous sort of silly thing.
It takes two molecules, (a christmas tree made of cyclodextrin, and a fullerene.)
It then shoots the fullerene at the cyclodextrins, because why not?
I suppose it also gives some example of velocity initalization and transposition.
"""
from __future__ import absolute_import
from __future__ import print_function
from TensorMol import *
import os
os.environ["CUDA_VISIBLE_DEVICES"]=""

def GetChemSpider12(a):
	TreatedAtoms = np.array([1,6,7,8], dtype=np.uint8)
	PARAMS["NetNameSuffix"] = "act_sigmoid100"
	PARAMS["learning_rate"] = 0.00001
	PARAMS["momentum"] = 0.95
	PARAMS["max_steps"] = 21
	PARAMS["batch_size"] =  50   # 40 the max min-batch size it can go without memory error for training
	PARAMS["test_freq"] = 1
	PARAMS["tf_prec"] = "tf.float64"
	PARAMS["EnergyScalar"] = 1.0
	PARAMS["GradScalar"] = 1.0/20.0
	PARAMS["DipoleScaler"]=1.0
	PARAMS["NeuronType"] = "sigmoid_with_param"
	PARAMS["sigmoid_alpha"] = 100.0
	PARAMS["HiddenLayers"] = [2000, 2000, 2000]
	PARAMS["EECutoff"] = 15.0
	PARAMS["EECutoffOn"] = 0
	#PARAMS["Erf_Width"] = 1.0
	#PARAMS["Poly_Width"] = 4.6
	PARAMS["Elu_Width"] = 4.6  # when elu is used EECutoffOn should always equal to 0
	#PARAMS["AN1_r_Rc"] = 8.0
	#PARAMS["AN1_num_r_Rs"] = 64
	PARAMS["EECutoffOff"] = 15.0
	#PARAMS["DSFAlpha"] = 0.18
	PARAMS["DSFAlpha"] = 0.18
	PARAMS["AddEcc"] = True
	PARAMS["KeepProb"] = [1.0, 1.0, 1.0, 0.7]
	#PARAMS["KeepProb"] = 0.7
	PARAMS["learning_rate_dipole"] = 0.0001
	PARAMS["learning_rate_energy"] = 0.00001
	PARAMS["SwitchEpoch"] = 2
	d = MolDigester(TreatedAtoms, name_="ANI1_Sym_Direct", OType_="EnergyAndDipole")  # Initialize a digester that apply descriptor for the fragme
	tset = TensorMolData_BP_Direct_EE_WithEle(a, d, order_=1, num_indis_=1, type_="mol",  WithGrad_ = True)
	manager=TFMolManage("Mol_chemspider12_maxatom35_H2O_with_CH4_ANI1_Sym_Direct_fc_sqdiff_BP_Direct_EE_ChargeEncode_Update_vdw_DSF_elu_Normalize_Dropout_act_sigmoid100_rightalpha", tset,False,"fc_sqdiff_BP_Direct_EE_ChargeEncode_Update_vdw_DSF_elu_Normalize_Dropout",False,False)
	return manager

treeXYZ = """485
	Energy:    2246.0845828
C         13.57199       -7.12447       -3.85872
C         13.28281       -6.17099       -5.02709
H         12.28931       -5.73847       -4.86949
C         13.41517       -6.90904       -6.36843
H         14.31516       -7.53621       -6.29089
C         13.75082       -5.94432       -7.52788
H         14.83186       -5.98894       -7.71432
C         13.38359       -4.48688       -7.22865
H         13.75349       -3.84531       -8.03655
C         13.92773       -4.00643       -5.85542
H         13.19282       -3.38736       -5.33043
O         14.24706       -5.10085       -4.97518
O         15.13840       -3.28096       -6.07706
C         15.11654       -1.84177       -5.95620
H         16.06958       -1.57423       -6.43120
C         15.18769       -1.36269       -4.47858
H         15.33705       -2.23009       -3.82441
O         13.95313       -0.76685       -4.03269
C         13.40845        0.30392       -4.80912
H         12.33047        0.10524       -4.85460
C         13.91129        0.33445       -6.26548
H         14.87901        0.83668       -6.36095
C         14.01389       -1.11488       -6.75132
H         13.04127       -1.60880       -6.66212
O         14.33119       -1.13011       -8.15000
O         13.01981        1.06824       -7.11941
O         13.62791        1.56665       -4.15603
C         12.41931        2.12311       -3.59705
H         11.77573        1.29880       -3.26451
C         11.64906        3.02582       -4.58262
H         11.32542        2.38650       -5.41202
O         10.45407        3.53087       -3.99457
C         10.55670        4.21845       -2.75487
H         11.01141        5.19529       -2.95543
C         11.44410        3.48178       -1.71200
H         10.91322        2.64249       -1.25658
C         12.73995        2.93085       -2.33442
H         13.45501        3.73506       -2.53595
O         13.37832        2.09126       -1.35403
O         11.78299        4.35493       -0.62319
O          9.21943        4.54988       -2.27770
C          8.37069        3.41590       -1.98688
H          8.98125        2.66394       -1.48502
C          7.75843        2.80071       -3.26940
H          8.37666        3.07060       -4.12162
O          6.48825        3.27891       -3.72339
C          5.51062        3.74844       -2.80376
H          4.92677        4.48590       -3.37004
C          6.10998        4.53483       -1.61899
H          5.32255        4.69198       -0.87212
C          7.29192        3.81846       -0.96542
H          7.73903        4.50327       -0.23322
O          6.84044        2.67108       -0.23928
O          6.53349        5.84119       -2.06259
O          4.57984        2.73784       -2.38674
C          3.71528        2.26113       -3.45140
H          3.54556        3.07356       -4.16844
C          2.34159        1.83433       -2.87311
H          2.02194        2.65750       -2.21978
O          2.37792        0.68414       -2.02097
C          3.19960       -0.42339       -2.39012
H          3.52099       -0.76871       -1.40163
C          4.46977       -0.12263       -3.20194
H          4.74575       -0.96942       -3.82605
C          4.36144        1.06885       -4.14666
H          5.36109        1.33756       -4.48065
O          3.66418        0.68001       -5.33601
O          5.55462        0.02022       -2.28440
O          2.44689       -1.49688       -2.97619
C          2.82672       -2.80868       -2.48012
H          3.07358       -2.71412       -1.41550
C          3.99288       -3.46501       -3.27074
H          4.34328       -2.82325       -4.07992
O          3.59797       -4.71006       -3.86892
C          2.52765       -4.55038       -4.79122
H          2.80342       -3.82805       -5.56894
C          1.25843       -4.09145       -4.02012
H          0.49532       -4.87822       -4.01500
C          1.59774       -3.73088       -2.56367
H          1.81547       -4.65255       -2.00761
O          0.44849       -3.12812       -1.94675
O          0.64182       -2.97269       -4.67737
O          2.19709       -5.78640       -5.44181
C          3.24245       -6.67568       -5.85623
H          2.66975       -7.43295       -6.41107
C          3.89537       -7.44518       -4.69380
H          4.30231       -6.79581       -3.91820
O          4.95713       -8.24581       -5.21189
C          6.10108       -7.48288       -5.62265
H          6.65457       -7.21318       -4.72280
C          5.73365       -6.17937       -6.38929
H          6.39646       -6.06023       -7.25256
C          4.27608       -6.16282       -6.88043
H          4.00554       -5.14952       -7.21022
O          4.22559       -6.98624       -8.06373
O          5.95775       -5.03325       -5.55347
O          6.82812       -8.40234       -6.43188
C          8.26264       -8.46491       -6.43820
H          8.45944       -9.52379       -6.65396
C          9.09483       -8.10262       -5.18317
H          8.86713       -7.07656       -4.87107
O         10.51324       -8.19541       -5.42279
C         11.02480       -7.50095       -6.56177
H         10.90185       -6.42883       -6.39443
O         12.40140       -7.85885       -6.70846
C         10.27084       -7.89867       -7.84914
H         10.63825       -7.32435       -8.70510
C          8.77426       -7.67475       -7.65281
H          8.56506       -6.60712       -7.53081
O          8.09025       -8.10825       -8.84035
O         10.48273       -9.28265       -8.19218
C          8.82581       -9.05758       -4.00260
O          7.50512       -8.97504       -3.49539
C          2.85438       -8.35755       -4.01823
O          1.75899       -7.63562       -3.46855
C          5.17868       -3.79598       -2.34720
O          5.68702       -2.64406       -1.67770
C          1.22788        1.67132       -3.92457
O          1.14292        2.81376       -4.77403
C          7.87301        1.27298       -3.18405
O          9.23897        0.84389       -3.28059
C         12.45056        4.17609       -5.21450
O         13.43255        3.68794       -6.12527
C         16.40402       -0.42683       -4.26257
O         16.58054       -0.11712       -2.88083
O         11.94461       -4.38392       -7.28229
O         13.09578       -6.35389       -8.74234
O         13.52777       -6.40201       -2.62642
H         12.83886       -7.93472       -3.80999
H         14.57315       -7.56190       -3.93882
H         13.75486       -0.44594       -8.54967
H         13.12734        2.01299       -6.85925
H         13.97210        1.48651       -1.84715
H         12.40533        3.84278       -0.06846
H          7.50868        2.47298        0.43983
H          7.37208        5.72536       -2.55168
H          3.86125        1.35045       -6.01516
H          5.64076       -0.83837       -1.81865
H          0.75813       -2.62531       -1.17134
H          0.20561       -2.47185       -3.95635
H          4.31800       -7.91466       -7.78648
H          6.91758       -4.88290       -5.50362
H          7.15598       -8.25178       -8.58846
H          9.85308       -9.46702       -8.91771
H          9.04226      -10.09646       -4.27794
H          9.50778       -8.81388       -3.17962
H          6.94338       -9.57692       -4.02000
H          2.46348       -9.09709       -4.73152
H          3.32913       -8.93273       -3.21645
H          1.37070       -7.10691       -4.19945
H          4.87900       -4.53395       -1.59423
H          5.99308       -4.24599       -2.92610
H          6.41934       -2.96616       -1.11659
H          1.36251        0.77710       -4.53829
H          0.26274        1.55389       -3.41725
H          0.42691        2.63482       -5.40929
H          7.52721        0.92999       -2.21107
H          7.32504        0.78090       -3.98801
H          9.21410       -0.12537       -3.19288
H         11.77244        4.83470       -5.77012
H         12.94063        4.79568       -4.45707
H         13.92547        4.47356       -6.43187
H         17.32076       -0.91459       -4.61515
H         16.29500        0.52201       -4.79213
H         17.36510        0.45793       -2.81952
H         11.73829       -4.69060       -8.19170
H         13.13159       -7.33317       -8.74922
H         14.11869       -5.63414       -2.75647
H         17.61134       -8.07851        7.27725
O         17.16533       -7.51258        6.61820
H         16.94615       -7.48351        3.87923
O         16.72046       -5.58541        4.39472
H         16.93940       -3.64314        6.50543
H         16.36717       -6.99935        1.86617
H         16.51890       -9.17834        5.61488
H         16.63503       -5.87869        6.83307
H         16.46898       -3.61772        4.25236
C         16.08435       -6.80698        3.98593
C         16.09514       -8.28468        6.08803
C         15.94401       -4.44077        4.75123
C         15.97958       -4.11914        6.27035
C         15.51358       -6.81213        2.53171
O         15.91663       -5.26982        7.12048
H         15.53903       -9.41211        3.31132
C         15.22621       -7.50321        5.07282
H         15.46699       -8.63364        6.91577
O         15.01563       -5.54781        2.07640
H         15.43953       -2.19221        2.86546
O         14.61693       -8.40656        0.93824
H         14.43031       -7.66853        0.32452
H         15.26685       -1.68356        5.30180
O         15.20608       -2.45685        7.83140
C         14.43484       -7.88573        2.26176
C         14.52699       -8.98901        3.31867
H         15.32528       -3.10507        8.55105
O         14.60330       -4.44008        4.26873
C         14.79683       -3.21648        6.68392
H         14.66626       -6.74656        5.62685
H         14.42147       -5.24513        2.79575
H         14.50793       -3.70639        1.60254
C         14.36112       -2.32846        2.99147
O         14.25291       -8.43091        4.59472
H         14.24935      -11.14258        4.68011
C         14.38074       -2.29082        5.53266
O         13.90238      -11.56155        5.49077
C         14.01533       -3.11631        4.27198
O         13.67979      -10.12456        3.10648
O         13.86545       -3.00550        1.83991
H         13.89267       -1.33911        3.01764
H         13.43833       -7.42994        2.28923
H         13.94086       -3.82494        7.00067
O         13.38018       -1.30999        5.83793
C         12.54775      -11.13356        5.61316
H         12.94073       -3.30963        4.22350
H         12.53281      -10.14234        6.07995
C         12.27700       -9.93605        3.37611
H         12.16433      -10.10648        1.20374
H         12.05523      -12.06824        3.76016
H         12.04959      -11.81600        6.30963
H         12.56692        0.44943        5.41800
C         11.81270      -11.12019        4.25932
H         12.08962       -8.99855        3.91449
C         12.09855       -1.77066        6.29435
C         11.49670       -9.91286        2.05157
O         12.15803       -2.01724        7.69289
H         11.81167       -2.69338        5.78497
O         11.63818        0.36751        5.11882
O         10.97639       -8.59038        1.81766
H         10.79323      -11.92563        1.84050
H         11.33179       -4.40890        8.13692
C         11.06938       -0.66160        5.94557
C         10.35107      -10.93727        2.01759
O         10.40859      -11.07879        4.51764
H         11.28021        0.41835        7.81223
C         10.89408       -2.29850        8.32331
H         11.11314       -2.24907        9.39796
H         10.33116       -8.71493        1.09041
C         10.46859       -3.74315        8.02195
C         10.48339       -0.05986        7.22947
C          9.57588      -10.99722        3.36062
H         10.26360       -1.09826        5.34387
O          9.51776      -10.64168        0.88583
H         10.11898       -3.85039        6.98981
C          9.83157       -1.19287        8.05496
H          8.95744      -11.89945        3.34539
O          9.44930       -4.18381        8.90274
O          9.54997        0.98715        6.92665
H          8.72034      -11.19860        0.93279
O          8.76208       -9.83496        3.50960
H          9.31265       -5.13309        8.74939
H          9.49140       -0.80119        9.02151
H          9.09480        0.74393        6.09971
O          8.69167       -1.72621        7.34177
H          8.06261       -8.26357        1.40322
C          7.34329      -10.05205        3.40508
H          7.13590      -10.74650        2.58144
C          6.99680       -8.26313        1.64193
H          7.32997      -10.24411        5.57109
H          7.19581       -7.90112        3.74069
C          7.48244       -0.98538        7.60227
H          7.72263       -0.00345        8.02129
O          6.98444      -12.06468        4.74425
C          6.73867       -8.66664        3.09921
C          6.77337      -10.64047        4.71312
O          7.26387       -1.89514        9.87871
H          6.59935       -7.26209        1.44474
O          6.33054       -9.16585        0.75699
O          6.87585       -0.73459        6.33409
H          6.85724       -3.80184        8.25021
H          6.62691       -3.52589        6.09574
H          6.39922      -12.41859        5.44365
C          6.58540       -1.70049        8.62598
H          6.72486       -2.54377       10.37309
C          6.09053       -3.03711        8.07836
C          5.78757       -2.99578        6.56932
H          5.93343       -1.73159        4.86757
C          5.79120       -1.58164        5.94679
O          5.31651       -8.64375        3.28796
H          5.38133       -9.10547        0.97376
H          5.55861       -8.25657        5.32206
C          5.26899      -10.37763        4.90257
H          5.51438       -4.69738        4.74351
H          5.41116      -10.36270        6.87007
C          4.96868       -8.88417        4.64853
H          5.73403       -1.06179        8.86927
O          4.88259      -10.83538        6.20728
O          4.89942       -5.96919        6.21914
H          4.69680      -10.99200        4.19397
C          4.66001       -4.79823        5.42370
O          4.96725       -3.47490        8.86095
H          4.83910       -8.30885        7.44212
O          4.21361       -6.45410        3.04713
O          4.54510       -3.65455        6.27153
H          4.22435       -7.41325        2.84681
C          4.46430       -0.80165        6.03272
H          4.58766        0.18178        5.56569
H          4.57776       -4.22934        8.37701
C          3.92531       -7.73577        7.60156
O          4.08193       -7.05755        8.84992
O          3.57571       -8.63099        4.82380
O          4.04303       -0.58605        7.36871
C          3.69395       -6.70318        6.49431
H          4.07049       -7.73114        9.55245
C          3.36183       -4.84778        4.56120
H          3.45688       -4.11146        3.75443
C          3.18067       -6.25903        4.00844
H          3.66662       -1.33553        5.50627
C          3.14267       -7.30132        5.17102
H          3.06770       -8.40974        7.69092
H          3.24893       -0.02468        7.33888
H          2.97274       -5.99034        6.91230
H          2.23231       -6.32919        3.46246
H          2.51382       -3.77721        5.94297
O          2.20155       -4.46504        5.31709
H          2.07468       -7.45039        5.38510
H          2.56343       -8.81643       18.39700
O          3.41345       -8.67494       17.94238
H          2.85271       -9.79904       16.33975
C          3.64067       -9.79721       17.09907
H          3.53986      -10.71569       17.68638
H          5.03609       -6.16807       16.66610
H          4.32041       -7.80224       15.68633
O          6.36350       -4.72907       18.33333
H          3.56987       -9.46112       13.60524
H          6.33375       -4.13504       17.56019
H          3.57666      -11.15588       14.90276
C          5.21898       -8.42813       15.62772
C          6.10676       -6.36405       16.53693
C          5.04552       -9.72306       16.46273
O          5.31997       -7.56100       13.36749
C          4.59531       -9.85394       13.61588
C          6.81328       -6.01928       17.86834
O          6.56726       -5.46775       15.52226
H          6.52300       -6.74853       18.63317
C          4.60993      -11.10128       14.54428
H          5.32920       -7.84772       12.43363
C          5.51300       -8.74975       14.15617
H          6.47076       -5.16883       13.36601
H          5.75650       -9.68887       17.29828
O          6.34856       -7.71972       16.17163
O          4.88815      -10.08270       12.23612
O          5.38818      -10.91495       15.72063
O          4.72520      -12.40089       13.98341
O          7.36836       -5.05994       12.98945
C          8.00027       -5.45244       15.29726
C          8.34851       -5.98256       17.72204
H          8.27726       -4.39814       15.40700
H          6.56522       -9.02899       14.02348
H          8.73976       -4.99873       18.00892
H          5.80881      -10.42545       12.20517
C          8.22130       -5.83524       13.83231
O          8.94059       -6.91588       18.64199
H          7.98667       -6.88842       13.65677
H          5.99499      -13.58356       16.31753
C          8.80802       -6.32008       16.29342
C          5.93165      -13.04652       13.59563
H          5.51999      -12.61966       11.50233
H          5.58393      -14.08720       13.53062
H          8.56342       -7.37131       16.11469
C          6.37705      -12.72234       12.17670
C          6.87368      -13.94387       15.77436
H          9.24647       -5.64257       13.51692
O          7.05887      -11.44561       12.15157
H          9.89372       -6.94054       18.43912
C          7.16776      -13.07387       14.53859
H          7.42907      -12.06725       14.87877
H         10.36692       -4.35665       15.72366
H          6.69421      -14.98569       15.48823
O         10.23993       -6.36695       16.25581
O          7.98027      -13.94501       16.67165
C         10.99377       -5.24456       15.83547
H          7.69906      -11.54503       11.40772
H          6.74218      -14.61028       11.15590
C          7.32019      -13.81949       11.64815
O         12.32474       -3.52290       16.93397
H         11.78263       -5.24780       17.86163
H          7.44580      -15.23303       13.23962
O          8.39445      -13.57734       13.88279
H         10.44902       -7.47962       13.70251
C         12.10522       -4.94644       16.85854
O          8.08742      -13.18268       10.62267
O         11.59628       -5.51326       14.56320
C          8.12558      -14.48482       12.81344
H          8.78427      -14.07710       16.13689
H         12.75549       -3.24266       16.10650
H         10.98816       -8.39479       15.10698
C         11.33031       -7.89097       14.19827
H          8.74690      -13.83875       10.29905
C         12.34328       -6.76349       14.50018
H         11.08236       -9.34118       12.94291
C         13.41789       -5.64969       16.48029
O          9.20723      -15.31327       12.37810
O         11.84924       -8.87931       13.32643
H         12.69285       -7.66280       16.49527
C         13.19713       -7.00697       15.77824
H         10.19281      -12.79394       11.83596
O         14.20761       -5.84896       17.66662
H         13.01398       -6.66609       13.63876
H         14.02710       -5.00234       15.83585
H         10.73541      -14.17032       14.41942
O         10.47064      -13.87785       10.12470
C         10.82744      -13.61966       11.49620
H         12.82492       -9.65649       15.75587
C         10.57365      -14.87715       12.33548
H         10.85804      -13.13309        9.61471
H         11.95038      -12.39739       13.51984
C         11.26965      -14.82092       13.71971
H         14.93823       -6.43712       17.38956
H         10.37267      -16.70107       14.40136
O         14.53564       -7.49223       15.55679
H         13.60108      -10.71359       17.59876
C         13.88212       -9.91025       15.85609
O         13.09176      -12.17850       15.81561
O         14.13942       -9.96692       17.26686
H         13.01434      -10.75475       13.49367
H         11.07370      -15.68578       11.78261
O         12.39967      -11.94356       10.82087
C         11.35598      -16.22798       14.33223
C         12.28921      -13.18039       11.53951
C         12.67736      -13.04360       13.01034
C         14.77437       -8.84934       15.16420
O         11.90149      -16.14806       15.64951
O         12.62948      -14.32724       13.61874
C         14.08897      -11.30606       15.25786
H         13.30021      -13.08737       15.51201
C         13.97334      -11.20940       13.73417
O         14.78902       -8.93271       13.74047
H         13.34426      -11.69543       10.85484
H         12.02233      -16.86135       13.73492
H         12.92577      -13.90969       11.02347
O         14.00644      -12.49816       13.10711
H         12.24454      -17.03188       15.87025
C         15.03868      -10.24432       13.19621
H         15.80319       -9.02168       15.49919
H         15.05132      -11.72827       15.56704
H         14.89672      -10.14251       12.11292
C         16.48631      -10.73142       13.40694
H         16.78451      -10.69997       14.45774
H         16.60931      -11.75405       13.03733
O         17.39186       -9.90281       12.68247
H         18.29458      -10.16003       12.94216
C         -1.31810       -0.91669       -0.19502
C         -2.80154       -0.47827       -0.18049
C         -0.40159        0.34291       -0.23833
O         -1.02225       -1.82408       -1.22997
O         -3.69909       -1.54058       -0.33047
O         -0.44081        0.97618       -1.49119
C          1.04426        0.00810        0.23733
C          1.82345        1.31400        0.58105
O          1.78628       -0.66343       -0.75864
C          3.31942        1.01601        0.71767
O          1.27056        1.94053        1.71022
O          3.85495        0.85340        1.78888
H         -1.08163       -1.52061        0.71301
H         -3.04613        0.17550       -1.03772
H         -3.01496        0.08462        0.74884
H         -0.83196        1.12438        0.43197
H         -1.46904       -1.52463       -2.01290
H         -3.50281       -2.18331        0.34021
H          0.08545        0.46483       -2.09499
H          0.98150       -0.63337        1.15244
H          1.66832        2.08171       -0.21273
H          1.35900       -1.49887       -0.90016
H          3.89522        0.94952       -0.21814
H          1.54150        1.45212        2.47913
C         15.49603      -11.09219       22.32711
C         14.41103       -9.99245       22.22547
C         12.98262      -10.61255       22.32052
C         11.88827       -9.49933       22.23549
C         10.50055      -10.12820       22.37381
O         16.76583      -10.56405       22.58812
O         14.61961       -9.34788       20.98880
O         12.80598      -11.37270       23.48949
O         12.05197       -8.71751       21.07462
O          9.72433      -10.20141       21.45139
H         15.50807      -11.72174       21.41573
H         15.31786      -11.75137       23.19491
H         14.54535       -9.24458       23.04818
H         12.83074      -11.36709       21.51473
H         12.03065       -8.74767       23.04734
H         10.24107      -10.52409       23.36775
H         17.00019      -10.01122       21.85273
H         13.86880       -8.76921       20.85183
H         13.12004      -10.85438       24.22112
H         11.63580       -9.17305       20.35029
"""

ballXYZ = """20

C          5.52099        0.88543       -0.73505
C          4.32460        0.06439       -0.82090
C          3.17513        2.86436       -2.01768
C          3.15538        0.91408       -0.82084
C          5.46288        2.86075       -2.03795
C          3.56604        2.30614       -0.73468
C          6.17378        0.68584       -2.01786
C          5.01570        2.24585       -0.80945
C          4.31280       -0.77831       -2.00514
C          2.35753        0.64250       -2.00465
C          4.31308        3.33411       -2.78994
C          6.26835        1.91329       -2.79043
C          5.45075       -0.30857       -2.77739
C          3.16300       -0.30496       -2.75713
C          2.45211        1.86995       -2.77722
C          4.30128        2.49140       -3.97417
C          5.47050        1.64171       -3.97424
C          5.05984        0.24965       -4.06040
C          3.61019        0.30995       -3.98563
C          3.10489        1.67036       -4.06002
"""

def Xmas():
	"""
	Shoot a tree with a ball.
	"""
	tree = Mol()
	tree.FromXYZString(treeXYZ)
	tree.coords -= tree.Center()
	ball = Mol()
	ball.FromXYZString(ballXYZ)
	ball.coords -= ball.Center()
	ball.coords -= np.array([15.0,0.0,0.0])
	ntree = tree.NAtoms()
	toshoot = Mol(np.concatenate([tree.atoms,ball.atoms],axis=0),np.concatenate([tree.coords,ball.coords],axis=0))

	# The tree is at rest, and the ball is headed towards the tree :)
	v0 = np.zeros(toshoot.coords.shape)
	v0[ntree:] -= np.array([-0.1581,0.0,0.0]) # Angstrom/fs.ch

	# Everything's ready! now just propagate.
	def GetEnergyForceForMol(m):
		s = MSet()
		s.mols.append(m)
		manager = GetChemSpider12(s)
		def EnAndForce(x_, DoForce=True):
			tmpm = Mol(m.atoms,x_)
			Etotal, Ebp, Ebp_atom, Ecc, Evdw, mol_dipole, atom_charge, gradient = manager.EvalBPDirectEEUpdateSingle(tmpm, PARAMS["AN1_r_Rc"], PARAMS["AN1_a_Rc"], PARAMS["EECutoffOff"], True)
			energy = Etotal[0]
			force = gradient[0]
			if DoForce:
				return energy, force
			else:
				return energy
		return EnAndForce
	F = GetEnergyForceForMol(toshoot)
	PARAMS["MDThermostat"]=None
	PARAMS["MDV0"]=None
	traj = VelocityVerlet(None, toshoot,"MerryXmas",F)
	traj.v = v0.copy()
	traj.Prop()

Xmas()
