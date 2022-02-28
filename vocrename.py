####将voc中的jpgImag和Annotion文件夹重命名

import os


class BatchRename():
    """
      :param path: path fot images
      :param prename: whether need a prefix filename or not
      :param prevalue: prefix filename
      """
    def __init__(self, pathimg, pathxml, prename=False, prevalue=''):
        self.imgpath = pathimg
        self.xmlpath = pathxml
        self.prename = prename
        self.prevalue = prevalue

    def rename(self):
        filelist = os.listdir(self.imgpath)
        total_num = len(filelist)
        i = 1
        n = len(str(total_num))*2
        for item in filelist:
            if item.lower().endswith(('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
                itemnot, _ = os.path.splitext(item)
                n = 6 - len(str(i))
                srcimg = os.path.join(os.path.abspath(self.imgpath), item)
                srcxml = os.path.join(os.path.abspath(self.xmlpath), itemnot + ".xml")
                if not os.path.exists(srcxml):
                    continue
                if self.prename:
                    filenewnameimg = self.prevalue + str(0) * n + str(i) + '.jpg'
                    filenewnamexml = self.prevalue + str(0) * n + str(i) + '.xml'
                else:
                    filenewnameimg = str(0) * n + str(i) + '.jpg'
                    filenewnamexml = str(0) * n + str(i) + '.xml'
                dstimg = os.path.join(os.path.abspath(self.imgpath), filenewnameimg)
                dstxml = os.path.join(os.path.abspath(self.xmlpath), filenewnamexml)

                # try:
                os.rename(srcimg, dstimg)
                os.rename(srcxml, dstxml)
                print('converting %s to %s ...' % (srcimg, dstimg))
                print('converting %s to %s ...' % (srcxml, dstxml))
                i = i + 1
                # except:
                #     continue
        print('total %d to rename & converted %d jpgs' % (total_num, i-1))


if __name__ == '__main__':
    demo = BatchRename(r"/home/YOLOX/datasets/VOCdevkitnb/VOC2007/JPEGImages", r"/home/YOLOX/datasets/VOCdevkitnb/VOC2007/Annotations", True, "NB")
    demo.rename()
