
#
#Day 15 Gibberellin Hormone 10^-5 M RGB Values
import numpy as np
from scipy.stats import ttest_ind

def load_data():
    rgbData                            = dict()
    rgbData['Gibberellin']           = dict()
    rgbData['Gibberellin']['day15'] = dict()
    rgbData['Gibberellin']['day18'] = dict()
    rgb_solution        = dict()
    d  = dict()
    #Day 15 Gibberellin Hormone Control Group RGB Values
    d['R'] = [149, 154, 151, 165, 163, 163, 161, 126, 167, 163, 191, 176, 168, 165, 170, 173, 154, 155, 165, 163]
    d['G'] = [221, 231, 229, 236, 235, 231, 230, 200, 207, 230, 240, 210, 233, 225, 216, 214, 217, 223, 228, 220]
    d['B'] = [136, 149, 151, 173, 150, 174, 121, 178, 131, 147, 162, 121, 162, 156, 175, 134, 145, 165, 137, 140]
    rgbData['Gibberellin']['day15']['Control Group'] = d.copy()
    #Day 15 Gibberellin Hormone 10^-7 M RGB Values
    d['R'] = [157, 146, 140, 158, 137, 182, 168, 155, 163, 153, 143, 153, 185, 182, 164, 201, 184, 151, 175, 176]
    d['G'] = [228, 217, 201, 222, 195, 210, 229, 233, 227, 223, 212, 220, 248, 247, 236, 253, 238, 223, 240, 237]
    d['B'] = [124, 98, 112, 126, 105, 137, 159, 149, 166, 172, 161, 122, 142, 136, 140, 146, 102, 134, 156, 145]
    rgbData['Gibberellin']['day15']['10^-7']   = d.copy()
    d['R'] = [136, 155, 188, 197, 136, 166, 146, 177, 140, 160, 153, 130, 133, 179, 134, 143, 128, 136, 141, 132]
    d['G'] = [212, 234, 255, 255, 221, 235, 232, 216, 225, 247, 241, 203, 213, 236, 224, 226, 224, 234, 243, 233]
    d['B'] = [122, 155, 203, 207, 132, 193, 141, 132, 144, 156, 162, 113, 134, 123, 154, 133, 134, 143, 123, 142]
    rgbData['Gibberellin']['day15']['10^-5']  = d.copy()
    # https://stackoverflow.com/questions/11222440/python-variable-reference-assignment
    # go to python, read reference
    #Day 15 Gibberellin Hormone 10^-5 M RGB Values
    d['R'] = [140, 144, 138, 171, 133, 147, 167, 112, 139, 128, 154, 117, 140, 141, 171,116, 142, 123, 142, 136]
    d['G'] = [238, 234, 232, 255, 222, 232, 241, 198, 217, 202, 226, 198, 220, 210, 250,185, 239, 230, 220, 212]
    d['B'] = [128, 145, 118, 182, 134, 156, 154, 125, 165, 162, 186, 126, 150, 178, 203,102, 124, 156, 145, 157]
    rgbData['Gibberellin']['day15']['10^-3'] = d.copy()
    #Day 18 Gibberellin Hormone Control Group RGB Values
    d['R'] = [139, 121, 168, 166, 126, 148, 176, 149, 131, 166, 143, 124, 112, 145, 145, 158, 144, 154, 160, 165]
    d['G'] = [208, 190, 236, 238, 188, 221, 241, 218, 196, 237, 207, 191, 169, 211, 213, 223, 209, 230, 237, 240]
    d['B'] = [155, 126, 193, 186, 96, 172, 200, 164, 142, 193, 153, 129, 98, 137, 151, 139, 109, 149, 155, 181]
    rgbData['Gibberellin']['day18']['Control Group'] = d.copy()
    #Day 18 Gibberellin Hormone 10-7 M RGB Values
    d['R'] = [185, 145, 164, 163, 161, 170, 146, 147, 170, 139, 159, 138, 145, 146, 134, 177, 173, 164, 160, 177]
    d['G'] = [216, 196, 213, 223, 210, 224, 217, 209, 224, 210, 210, 205, 218, 195, 205, 192, 244, 243, 227, 247]
    d['B'] = [144, 140, 158, 150, 155, 174, 159, 143, 158, 142, 134, 141, 127, 145, 147, 134, 174, 155, 150, 177]
    rgbData['Gibberellin']['day18']['10^-7'] = d.copy()

    #Day 18 Gibberellin Hormone 10^-5 RGB Values
    d['R'] = [150, 158, 164, 162, 165, 161, 167, 143, 149, 164, 134, 140, 143, 169, 139, 143, 134, 132, 129, 171]
    d['G'] = [230, 241, 241, 232, 241, 236, 235, 215, 226, 241, 240, 225, 221, 239, 217, 208, 195, 200, 227, 246]
    d['B'] = [159, 154, 163, 130, 200, 203, 172, 175, 176, 163, 120, 130, 137, 140, 131, 145, 135, 138, 147, 164]
    rgbData['Gibberellin']['day18']['10^-5'] = d.copy()

    #Day 18 Gibberellin Hormone 10^-3 RGB Values
    d['R'] = [124, 139, 146, 137, 135, 137, 142, 178, 138, 109, 137, 135, 159, 148, 170, 161, 157, 146, 167, 158]
    d['G'] = [195, 212, 216, 207, 202, 214, 209, 247, 218, 162, 204, 207, 240, 234, 250, 240, 240, 230, 239, 232]
    d['B'] = [125, 141, 154, 130, 133, 134, 130, 219, 121, 76, 133, 134, 145, 130, 163, 135, 134, 124, 168, 153]
    rgbData['Gibberellin']['day18']['10^-3'] = d.copy()

    rgbData['IAA']                     = dict()
    rgbData['IAA']['day15']          = dict()
    rgbData['IAA']['day18']          = dict()

    #Day 15 IAA Hormone Control Group RGB Values
    d['R'] = [153, 139, 119, 114, 134, 124, 144, 131, 119, 113, 156, 157, 128, 129, 134, 140, 150, 120, 140, 139]
    d['G'] = [248, 235, 197, 190, 224, 208, 241, 227, 200, 215, 245, 252, 200, 216, 220, 220, 219, 234, 225, 218]
    d['B'] = [176, 172, 154, 155, 166, 157, 179, 161, 157, 173, 180, 194, 170, 161, 160, 155, 156, 149, 148, 163]
    rgbData['IAA']['day15']['Control Group'] = d.copy()
    #Day 15 IAA Hormone 10^-8 M RGB Values
    d['R'] = [153, 145, 148, 159, 169, 148, 137, 143, 144, 119, 128, 134, 129, 125, 130, 145, 154, 148, 143, 138]
    d['G'] = [243, 235, 245, 254, 255, 236, 221, 235, 234, 199, 202, 220, 212, 220, 219, 205, 221, 234, 215, 209]
    d['B'] = [181, 167, 173, 196, 211, 189, 194, 202, 199, 152, 179, 161, 177, 178, 168, 167, 174, 182, 188, 156]
    rgbData['IAA']['day15']['10^-8'] = d.copy()
    #Day 15 IAA Hormone 10^-6 M RGB Values
    d['R'] = [128, 131, 123, 134, 130, 144, 135, 160, 135, 135, 159, 139, 138, 128, 126, 134, 135, 136, 138, 139]
    d['G'] = [219, 224, 214, 224, 224, 241, 228, 247, 229, 233, 239, 234, 232, 218, 218, 225, 227, 234, 218, 220]
    d['B'] = [178, 171, 173, 173, 166, 174, 181, 189, 176, 176, 190, 166, 168, 179, 169, 186, 167, 175, 178, 182]
    rgbData['IAA']['day15']['10^-6'] = d.copy()
    #Day 15 IAA Hormone 10^-4 M RGB Values
    d['R'] = [145, 126, 126, 135, 123, 116, 120, 134, 141, 145, 106, 118, 134, 109, 133, 120, 128, 118, 124, 128]
    d['G'] = [219, 199, 203, 215, 206, 204, 202, 216, 223, 231, 196, 192, 216, 190, 218, 189, 210, 208, 230, 213]
    d['B'] = [192, 163, 157, 144, 135, 125, 135, 176, 175, 160, 126, 145, 167, 124, 169, 157, 154, 145, 139, 151]
    rgbData['IAA']['day15']['10^-4'] = d.copy()

    #Day 18 IAA Hormone Control Group RGB Values
    d['R'] = [133, 124, 131, 126, 134, 171, 148, 142, 135, 127, 141, 151, 159, 153, 156, 141, 140, 143, 177, 139]
    d['G'] = [213, 203, 213, 216, 222, 249, 221, 216, 207, 204, 212, 225, 238, 225, 229, 213, 209, 210, 246, 210]
    d['B'] = [151, 138, 144, 126, 130, 202, 180, 179, 168, 149, 110, 126, 139, 147, 132, 147, 164, 167, 202, 142]
    rgbData['IAA']['day18']['Control Group'] = d.copy()
    #Day 18 IAA Hormone 10^-8 M RGB Values
    d['R'] = [171, 147, 130, 150, 149, 162, 160, 183, 174, 148, 153, 170, 147, 160, 157, 168, 152, 162, 160, 140]
    d['G'] = [242, 217, 208, 219, 221, 228, 242, 253, 253, 234, 235, 251, 232, 244, 232, 238, 221, 229, 233, 215]
    d['B'] = [198, 180, 133, 190, 183, 200, 142, 154, 158, 135, 133, 156, 129, 138, 178, 205, 189, 298, 187, 149]
    rgbData['IAA']['day18']['10^-8'] = d.copy()
    #Day 18 IAA Hormone 10^-6 M RGB Values
    d['R'] = [138, 143, 142, 140, 137, 143, 134, 157, 154, 155, 171, 146, 151, 165, 155, 150, 138, 140, 137, 145]
    d['G'] = [216, 222, 217, 219, 212, 224, 209, 232, 234, 229, 244, 223.45, 238, 248, 238, 236, 226, 224, 219, 218]
    d['B'] = [157, 157, 161, 155, 156, 155, 152, 173, 163, 167, 165, 160.4, 144, 170, 153, 146, 116, 119, 109, 159]
    rgbData['IAA']['day18']['10^-6']   = d.copy()
    #Day 18 IAA Hormone 10^-4 M RGB Values
    d['R'] = [149, 141, 149, 153, 132, 153, 158, 153, 146, 173, 160, 152, 156, 152, 154, 152, 146, 163,155, 156]
    d['G'] = [219, 212, 213, 223, 204, 224, 232, 221, 216, 244, 243, 236, 200, 238, 239, 234, 232, 236, 228, 229]
    d['B'] = [149, 139, 145, 151, 131, 146, 170, 144, 146, 184, 154, 140, 185, 145, 149, 149, 142, 170, 165, 150]
    rgbData['IAA']['day18']['10^-4'] = d.copy()
    
    return rgbData

def calculate_mean(d):
    sum = 0
    for dd in d:
        sum = sum+dd
    d_mean = sum/len(d)
    return d_mean

def hypotest(data1,data2):
    stat, p = ttest_ind(data1, data2)
    print('stat=%.3f, p=%.3f' % (stat, p))
    if p > 0.05:
        print('Probably the same distribution')
    else:
        print('Probably different distributions')
    return stat, p

# calculate mean
rgbData = load_data()
for hormone in rgbData.keys():
    for dayA in rgbData[hormone].keys():
        for solutionA in rgbData[hormone][dayA].keys():
            for rgb in rgbData[hormone][dayA][solutionA].keys():
                d = rgbData[hormone][dayA][solutionA][rgb]
                d_mean = calculate_mean(d)
                print(hormone,' ', dayA, ' ', solutionA, ' ', rgb,': ', str(d_mean))

# get gindex
rgbData = load_data()
for hormone in rgbData.keys():
    for dayA in rgbData[hormone].keys():
        for solutionA in rgbData[hormone][dayA].keys():
            d = rgbData[hormone][dayA][solutionA]
            dg = d['G']
            dr = d['R']
            dindex =[]
            for i in range(len(dg)):
                dindex.append(dg[i]/dr[i])
            d_mean_index = calculate_mean(dindex)
            d_std_index  = np.std(np.array(dindex))
            print(hormone,' ', dayA, ' ', solutionA, ' index,: ', d_mean_index,',    ', d_std_index)

# hypthesis testing
rgbData = load_data()
gIndex = {}
for hormone in rgbData.keys():
    gIndexH = {}
    for dayA in rgbData[hormone].keys():
        gIndexD = {}
        for solutionA in rgbData[hormone][dayA].keys():
            d = rgbData[hormone][dayA][solutionA]
            dg = d['G']
            dr = d['R']
            dindex =[]
            for i in range(len(dg)):
                dindex.append(dg[i]/dr[i])
            gIndexD[solutionA] = dindex
        gIndexH[dayA] = gIndexD
    gIndex[hormone] = gIndexH


data1 = gIndex['Gibberellin']['day15']['10^-5']
# data2 = gIndex['Gibberellin']['day15']['Control Group']
data2 = gIndex['Gibberellin']['day15']['10^-7']
s,p = hypotest(data1, data2)


# Gibberellin   day15   10^-5  index,:  1.5494041254440103
# Gibberellin   day15   10^-3  index,:  1.6016810814127425
# Gibberellin   day15   Control Group  index,:  1.3871287671808825
# Gibberellin   day15   10^-7  index,:  1.3938573326832902
# Gibberellin   day18   10^-5  index,:  1.5162939937822721
# Gibberellin   day18   10^-3  index,:  1.5074794821615778
# Gibberellin   day18   Control Group  index,:  1.4679889321847652
# Gibberellin   day18   10^-7  index,:  1.3755469547347603
# IAA   day15   10^-8  index,:  1.5937459930767157
i = 1
# R_sum5 = 0
# G_sum5 = 0
# B_sum5 = 0
# R_sum7 = 0
# G_sum7 = 0
# B_sum7 = 0
# for R in rgbData['Gibberellin']:
#     if R in rgbData['Gibberellin']['10^-5']:
#         if R in rgbData['Gibberellin']['10^-5']['R']:
#             R_sum5 = R_sum5 + R
#         elif R in rgbData['Gibberellin']['10^-5']['G']:
#             G_sum5 = G_sum5 + R
#         else:
#             B_sum5 = B_sum5 + R
#     elif R in rgbData['Gibberellin']['10^-7']:
#         if R in rgbData['Gibberellin']['10^-7']['R']:
#             R_sum7 = R_sum7 + R
#         elif R in rgbData['Gibberellin']['10^-7']['G']:
#             G_sum7 = G_sum7 + R
#         else:
#             B_sum7 = B_sum7 + R
# R_mean = R_sum5/len(rgbData['Gibberellin']['10^-5']['R'])
# G_mean = G_sum5/len(rgbData['Gibberellin']['10^-5']['G'])
# B_mean = B_sum5/len(rgbData['Gibberellin']['10^-5']['B'])
# print('R_mean = ', R_mean,      'G_mean = ', G_mean,    'B_mean = ', B_mean)