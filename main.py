from Objs import *
import random
import copy


def main():
    allobjs = []
    newobjs = []


    objtm = TestObj()
    objtm.setTip1(0, 0)
    objtm.setTip2(0, 2)
    allobjs.append(objtm)

    objtb = TestObj()
    objtb.setTip1(0, 0)
    objtb.setTip2(0, 4)
    allobjs.append(objtb)

    objtn = TestObj()
    objtn.setTip1(0, 0)
    # objtn.setTip2(0, 2)
    allobjs.append(objtn)


    # objmt = TestObj()
    # objmt.setTip1(0, 2)
    # objmt.setTip2(0, 0)
    # allobjs.append(objmt)

    objmb = TestObj()
    objmb.setTip1(0, 2)
    objmb.setTip2(0, 4)
    allobjs.append(objmb)

    objmn = TestObj()
    objmn.setTip1(0, 2)
    # objtn.setTip2(0, 2)
    allobjs.append(objmn)


    # objbt = TestObj()
    # objbt.setTip1(0, 4)
    # objbt.setTip2(0, 0)
    # allobjs.append(objbt)

    # objbm = TestObj()
    # objbm.setTip1(0, 4)
    # objbm.setTip2(0, 2)
    # allobjs.append(objbm)

    objbn = TestObj()
    objbn.setTip1(0, 4)
    # objtn.setTip2(0, 2)
    allobjs.append(objbn)


    # objnt = TestObj()
    # # objnt.setTip1(0, 2)
    # objnt.setTip2(0, 0)
    # allobjs.append(objnt)

    # objnm = TestObj()
    # # objnm.setTip1(0, 2)
    # objnm.setTip2(0, 2)
    # allobjs.append(objnm)

    # objnb = TestObj()
    # # objnb.setTip1(0, 2)
    # objtn.setTip2(0, 4)
    # allobjs.append(objnb)

    objnn = TestObj()
    # objnn.setTip1(0, 2)
    # objtn.setTip2(0, 2)
    allobjs.append(objnn)







    # testobj = TestObj()
    # testobj.setTip1(0, 4)
    # testobj.setTip2(0, 2)
    #
    # allobjs.append(testobj)

    stillIterating = True
    while(stillIterating):
        for obj in allobjs:
            if(obj.processed == 0):
                moveable_dirs = obj.getMoveableTipDirections(obj.tip1)
                for dir in moveable_dirs:
                    newobj = copy.deepcopy(obj)
                    newobj.moveTip1(dir)
                    newobjs.append(newobj)

                obj.pickSuitableNumbers()
                obj.processed = 1

        if(len(newobjs) == 0):
            stillIterating = False
        else:
            for obj in newobjs:
                allobjs.append(obj)
            newobjs = []




    print()





main()