'''
robofont-extensions-and-scripts
GlyphImplementationAudit.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com

Apache License

Version 2.0, January 2004

http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.

"License" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document.

"Licensor" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License.

"Legal Entity" shall mean the union of the acting entity and all other entities that control, are controlled by, or are under common control with that entity. For the purposes of this definition, "control" means (i) the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the outstanding shares, or (iii) beneficial ownership of such entity.

"You" (or "Your") shall mean an individual or Legal Entity exercising permissions granted by this License.

"Source" form shall mean the preferred form for making modifications, including but not limited to software source code, documentation source, and configuration files.

"Object" form shall mean any form resulting from mechanical transformation or translation of a Source form, including but not limited to compiled object code, generated documentation, and conversions to other media types.

"Work" shall mean the work of authorship, whether in Source or Object form, made available under the License, as indicated by a copyright notice that is included in or attached to the work (an example is provided in the Appendix below).

"Derivative Works" shall mean any work, whether in Source or Object form, that is based on (or derived from) the Work and for which the editorial revisions, annotations, elaborations, or other modifications represent, as a whole, an original work of authorship. For the purposes of this License, Derivative Works shall not include works that remain separable from, or merely link (or bind by name) to the interfaces of, the Work and Derivative Works thereof.

"Contribution" shall mean any work of authorship, including the original version of the Work and any modifications or additions to that Work or Derivative Works thereof, that is intentionally submitted to Licensor for inclusion in the Work by the copyright owner or by an individual or Legal Entity authorized to submit on behalf of the copyright owner. For the purposes of this definition, "submitted" means any form of electronic, verbal, or written communication sent to the Licensor or its representatives, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, the Licensor for the purpose of discussing and improving the Work, but excluding communication that is conspicuously marked or otherwise designated in writing by the copyright owner as "Not a Contribution."

"Contributor" shall mean Licensor and any individual or Legal Entity on behalf of whom a Contribution has been received by Licensor and subsequently incorporated within the Work.

2. Grant of Copyright License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form.

3. Grant of Patent License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work, where such license applies only to those patent claims licensable by such Contributor that are necessarily infringed by their Contribution(s) alone or by combination of their Contribution(s) with the Work to which such Contribution(s) was submitted. If You institute patent litigation against any entity (including a cross-claim or counterclaim in a lawsuit) alleging that the Work or a Contribution incorporated within the Work constitutes direct or contributory patent infringement, then any patent licenses granted to You under this License for that Work shall terminate as of the date such litigation is filed.

4. Redistribution. You may reproduce and distribute copies of the Work or Derivative Works thereof in any medium, with or without modifications, and in Source or Object form, provided that You meet the following conditions:

You must give any other recipients of the Work or Derivative Works a copy of this License; and

You must cause any modified files to carry prominent notices stating that You changed the files; and

You must retain, in the Source form of any Derivative Works that You distribute, all copyright, patent, trademark, and attribution notices from the Source form of the Work, excluding those notices that do not pertain to any part of the Derivative Works; and

If the Work includes a "NOTICE" text file as part of its distribution, then any Derivative Works that You distribute must include a readable copy of the attribution notices contained within such NOTICE file, excluding those notices that do not pertain to any part of the Derivative Works, in at least one of the following places: within a NOTICE text file distributed as part of the Derivative Works; within the Source form or documentation, if provided along with the Derivative Works; or, within a display generated by the Derivative Works, if and wherever such third-party notices normally appear. The contents of the NOTICE file are for informational purposes only and do not modify the License. You may add Your own attribution notices within Derivative Works that You distribute, alongside or as an addendum to the NOTICE text from the Work, provided that such additional attribution notices cannot be construed as modifying the License. You may add Your own copyright statement to Your modifications and may provide additional or different license terms and conditions for use, reproduction, or distribution of Your modifications, or for any such Derivative Works as a whole, provided Your use, reproduction, and distribution of the Work otherwise complies with the conditions stated in this License.

5. Submission of Contributions. Unless You explicitly state otherwise, any Contribution intentionally submitted for inclusion in the Work by You to the Licensor shall be under the terms and conditions of this License, without any additional terms or conditions. Notwithstanding the above, nothing herein shall supersede or modify the terms of any separate license agreement you may have executed with Licensor regarding such Contributions.

6. Trademarks. This License does not grant permission to use the trade names, trademarks, service marks, or product names of the Licensor, except as required for reasonable and customary use in describing the origin of the Work and reproducing the content of the NOTICE file.

7. Disclaimer of Warranty. Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

8. Limitation of Liability. In no event and under no legal theory, whether in tort (including negligence), contract, or otherwise, unless required by applicable law (such as deliberate and grossly negligent acts) or agreed to in writing, shall any Contributor be liable to You for damages, including any direct, indirect, special, incidental, or consequential damages of any character arising as a result of this License or out of the use or inability to use the Work (including but not limited to damages for loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses), even if such Contributor has been advised of the possibility of such damages.

9. Accepting Warranty or Additional Liability. While redistributing the Work or Derivative Works thereof, You may choose to offer, and charge a fee for, acceptance of support, warranty, indemnity, or other liability obligations and/or rights consistent with this License. However, in accepting such obligations, You may act only on Your own behalf and on Your sole responsibility, not on behalf of any other Contributor, and only if You agree to indemnify, defend, and hold each Contributor harmless for any liability incurred by, or claims asserted against, such Contributor by reason of your accepting any such warranty or additional liability.

END OF TERMS AND CONDITIONS
'''




import os
import shutil
import math
import tempfile
import shutil
import zipfile

import freetype
import pystache

#from FIFont import *
#from FIMap import *
#from FISvg import *
from GiaSettings import getCommandLineSettings
#import FICompoundsList
from tfs.common.TFSPoint import TFSPoint
from tfs.common.TFSPath import polygonWithPoints
#from collections import defaultdict
from tfs.common.TFSMap import TFSMap
from tfs.common.UnicodeCharacterNames import getUnicodeCharacterName, getUnicodeLongName

class GlyphImplementationAudit(object):

    def __init__(self, settings = None):
        if settings is None:
            self.settings = getCommandLineSettings()
        else:
            self.settings = settings

        self.configure()
        self.initMetrics()


    def configure(self):

        src_paths = self.settings.src_paths
        if src_paths is None:
            raise Exception('Missing src_paths')
        for src_path in src_paths:
            if not (os.path.exists(src_path) and os.path.isdir(src_path)):
                raise Exception('Invalid src_path: %s' % src_path)
        self.src_paths = src_paths


    #    testFont = os.path.abspath(os.path.join('..', '..', 'data', 'FITest Plain.ufo'))
#        self.fifont = FIFontFromFile(ufo_src)

    #    interpolation.srcCodePoints = interpolation.fifont.glyphCodePoints()

        log_dst = self.settings.log_dst
        if log_dst is None:
            self.log_dst = None
    #        raise Exception('Missing log_dst')
            pass
        else:
            if os.path.exists(log_dst):
                shutil.rmtree(log_dst)
            os.mkdir(log_dst)
            if not (os.path.exists(log_dst) and os.path.isdir(log_dst)):
                raise Exception('Invalid log_dst: %s' % log_dst)
            self.log_dst = log_dst

            def makeLogSubfolder(parent, name):
                subfolder = os.path.abspath(os.path.join(parent, name))
                os.mkdir(subfolder)
                if not (os.path.exists(subfolder) and os.path.isdir(subfolder)):
                    raise Exception('Invalid log_dst: %s' % log_dst)
                return subfolder

            self.html_folder = makeLogSubfolder(log_dst, 'html')
            self.css_folder = makeLogSubfolder(self.html_folder, 'stylesheets')
            self.svg_folder = makeLogSubfolder(self.html_folder, 'svg')

            srcCssFile = os.path.abspath(os.path.join('..', '..', '..', 'data', 'styles.css'))
            dstCssFile = os.path.abspath(os.path.join(self.css_folder, os.path.basename(srcCssFile)))
            shutil.copy(srcCssFile, dstCssFile)


#    def subrenderGlyphContours(self, fiSvg, contours, strokeColor):
#        from FISvg import FISvgPath
#
#        ON_POINT_COLOR = 0x7f7f7f7f
#        CONTROL_POINT_COLOR = 0x7fafafaf
#        for contour in contours:
#            fiSvg.addItem(FISvgPath(contour).addStroke(strokeColor, 2).addPointHighlights(ON_POINT_COLOR, CONTROL_POINT_COLOR))
#
#
#    def renderSvgScene(self,
#                       filenamePrefix,
#                       pathTuples,
#                       hGuidelines=None):
#        from FISvg import FISvg, FISvgPath
#
#        filename = '%s.svg' % ( filenamePrefix, )
#        dstFile = os.path.abspath(os.path.join(self.svg_folder, filename))
#
#        CANVAS_BACKGROUND_COLOR = 0xffffffff
#        CANVAS_BORDER_COLOR = 0x07fbfbfbf
#        fiSvg = FISvg().withBackground(CANVAS_BACKGROUND_COLOR).withBorder(CANVAS_BORDER_COLOR)
#
#    #    if pathTuples:
#        for color, contours in pathTuples:
#            self.subrenderGlyphContours(fiSvg, contours, color)
#
#        if hGuidelines:
#            for hGuideline in hGuidelines:
#                p0 = FIPoint(hGuideline, self.fifont.info.descender)
#                p1 = FIPoint(hGuideline, self.fifont.info.ascender)
#                GUIDELINE_COLOR = 0x7fdfdfdf
#                fiSvg.addItem(FISvgPath(openPathWithPoints(p0, p1)).addStroke(GUIDELINE_COLOR, 1))
#
#        vGuidelines = ( 0,
#                        self.fifont.info.ascender,
#                        self.fifont.info.descender,
#                        )
#        if vGuidelines:
#            minmax = None
#            for color, contours in pathTuples:
#                minmax = minmaxMerge(minmax, minmaxPaths(contours))
#
#            for vGuideline in vGuidelines:
#                p0 = FIPoint(0, vGuideline)
#                p1 = FIPoint(minmax.maxX, vGuideline)
#                GUIDELINE_COLOR = 0x7fdfdfdf
#                fiSvg.addItem(FISvgPath(openPathWithPoints(p0, p1)).addStroke(GUIDELINE_COLOR, 1))
#
#        SVG_HEIGHT = 400
#        SVG_MAX_WIDTH = 800
#        fiSvg.renderToFile(dstFile, margin=10, height=SVG_HEIGHT, maxWidth=SVG_MAX_WIDTH)
#        return filename
#
#
#    def convertCodePoint(self, glyph):
#        if type(glyph) is types.IntType:
#            return glyph
#        elif type(glyph) is types.StringType:
#            return ord(glyph)
#        else:
#            raise Exception('Bad glyph: ' + str(glyph))
#
#



    def writeMustacheLog(self, mustacheFilename, dstFilename, mustacheVars, replaceMap=None):
        mustacheFile = os.path.abspath(os.path.join('..', '..', '..', 'data', mustacheFilename))
        if not (os.path.exists(mustacheFile) and os.path.isfile(mustacheFile)):
            raise Exception('Invalid mustacheFile: ' + mustacheFile)
        with open(mustacheFile, 'rt') as f:
            mustache_template = f.read()

        mustacheMap = {
                       }
        mustacheMap.update(mustacheVars)

        logHtml = pystache.render(mustache_template, mustacheMap)

        if replaceMap:
            for key, value in replaceMap.items():
                logHtml = logHtml.replace(key, value)

        dstFile = os.path.abspath(os.path.join(self.html_folder, dstFilename))
        with open(dstFile, 'wt') as f:
            # TODO: explicitly encode unicode
            f.write(logHtml)
#
#
    def initMetrics(self):
        self.processedPostscriptNames = set()
        self.nonEmptyPostscriptNames = set()
        self.glyphCountMap = {}


    def getTableSvg(self, glyphs, maxValue):
        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.codePoint, glyph1.codePoint))
        glyphs = glyphs[:1000]

        from tfs.common.TFSSvg import TFSSvg, TFSSvgPath, blendArgbColors

        CANVAS_BACKGROUND_COLOR = 0xffffffff
        CANVAS_BORDER_COLOR = 0x07fbfbfbf
        fiSvg = TFSSvg().withBackground(CANVAS_BACKGROUND_COLOR).withBorder(CANVAS_BORDER_COLOR)

        glyphCount = len(glyphs)
        margin = 10
        hSpacing = vSpacing = 10
        cellWidth = cellHeight = 10
        glyphsPerRow = 13
        width = 2 * margin + (glyphsPerRow * cellWidth) + ((glyphsPerRow - 1) * hSpacing)
        rowCount = int(math.ceil(glyphCount / glyphsPerRow))
        height = 2 * margin + (rowCount * cellHeight) + ((rowCount - 1) * vSpacing)

        for index, glyph in enumerate(glyphs):
            x = index % glyphsPerRow
            y = int(math.floor(index / glyphsPerRow))
            corner = TFSPoint(margin + x * (cellWidth + hSpacing),
                              margin + y * (cellHeight + vSpacing))
            path = polygonWithPoints(corner,
                                     corner.right(cellWidth),
                                     corner.right(cellWidth).up(cellHeight),
                                     corner.up(cellHeight))
            path = path.applyScaleXY(1.0, -1.0)
            minGlyphColor = 0xffafafff
            maxGlyphColor = 0xff0f0f5f
            phase = glyph.count / float(maxValue)
            glyphColor = blendArgbColors(minGlyphColor, maxGlyphColor, phase)
            fiSvg.addItem(TFSSvgPath(path).addFill(glyphColor))

#    #    if pathTuples:
#        for color, contours in pathTuples:
#            self.subrenderGlyphContours(fiSvg, contours, color)
#
#        if hGuidelines:
#            for hGuideline in hGuidelines:
#                p0 = FIPoint(hGuideline, self.fifont.info.descender)
#                p1 = FIPoint(hGuideline, self.fifont.info.ascender)
#                GUIDELINE_COLOR = 0x7fdfdfdf
#                fiSvg.addItem(FISvgPath(openPathWithPoints(p0, p1)).addStroke(GUIDELINE_COLOR, 1))
#
#        vGuidelines = ( 0,
#                        self.fifont.info.ascender,
#                        self.fifont.info.descender,
#                        )
#        if vGuidelines:
#            minmax = None
#            for color, contours in pathTuples:
#                minmax = minmaxMerge(minmax, minmaxPaths(contours))
#
#            for vGuideline in vGuidelines:
#                p0 = FIPoint(0, vGuideline)
#                p1 = FIPoint(minmax.maxX, vGuideline)
#                GUIDELINE_COLOR = 0x7fdfdfdf
#                fiSvg.addItem(FISvgPath(openPathWithPoints(p0, p1)).addStroke(GUIDELINE_COLOR, 1))

#        SVG_HEIGHT = 400
#        SVG_MAX_WIDTH = 800

        return fiSvg.renderRaw(None, width, height)

#        filename = '%s.svg' % ( filenamePrefix, )
#        dstFile = os.path.abspath(os.path.join(self.svg_folder, filename))
#        fiSvg.renderToFile(dstFile, margin=10, height=SVG_HEIGHT, maxWidth=SVG_MAX_WIDTH)
#        return filename


    def dumpMetrics(self):

        print
        print 'fonts scanned:', len(self.processedPostscriptNames)
        print 'fonts processed:', len(self.nonEmptyPostscriptNames)
        print 'glyphs observed:', len(self.glyphCountMap)
        maxGlyphCount = reduce(max, self.glyphCountMap.values())
        print 'Highest glyph frequency:', maxGlyphCount

        glyphs = []
        for codePoint, count in self.glyphCountMap.iteritems():
            glyph = TFSMap()
            glyph.codePoint = codePoint
            glyph.count = count
            glyphs.append(glyph)

        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.count, glyph1.count), reverse=True)

        print 'Most common glyph:', glyphs[0]
        print 'Least common glyph:', glyphs[-1]

        pres = []
        for glyph in glyphs[:1000]:
            pre = {}
            pre['value'] = '%s %s: %d (%0.2f%%)' % ( hex(glyph.codePoint),
                                            getUnicodeLongName(glyph.codePoint,
                                                                    ignoreUnknown=True,
                                                                    skipValidation=True),
                                            glyph.count,
                                            glyph.count / float(len(self.nonEmptyPostscriptNames)),
                                            )
#            print 'pre', pre
            pres.append(pre)

        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.codePoint, glyph1.codePoint))
        headerPres = []
        for glyph in glyphs[:10000]:

            minGlyphColor = 0xffafafff
            maxGlyphColor = 0xff0f0f5f
            phase = glyph.count / float(maxGlyphCount)
            from tfs.common.TFSSvg import blendArgbColors
            glyphColor = 0xffffff & blendArgbColors(minGlyphColor, maxGlyphColor, phase)

            pre = {
#                    'glyphHex': hex(glyph.codePoint),
                    'glyphHex': '%X' % glyph.codePoint,
                    'glyphName': getUnicodeLongName(glyph.codePoint,
                                                    ignoreUnknown=True,
                                                    skipValidation=True),
                   'glyphCount': glyph.count,
                   'glyphPercent': (glyph.count / float(len(self.nonEmptyPostscriptNames))),
                   'glyphColor': '%06X' % glyphColor,
                   }
#            pre['value'] = '%s %s: %d (%0.2f%%)' % ( hex(glyph.codePoint),
#                                            getUnicodeCharacterName(glyph.codePoint,
#                                                                    ignoreUnknown=True,
#                                                                    skipValidation=True),
#                                            glyph.count,
#                                            glyph.count / float(len(self.nonEmptyPostscriptNames)),
#                                            )
#            print 'pre', pre
            headerPres.append(pre)

#        tableSvg = self.getTableSvg(glyphs, maxGlyphCount)

        self.writeMustacheLog('gia_pre_template.txt',
                              'most_common_glyphs.html',
                              mustacheVars = { 'pres': pres,
                                              'headerPres': headerPres,
                                              'pageTitle': '1,000 Most Commonly Implemented Font Glyphs',
                                              'headerTitle': 'Glyph Implementation Statistics',
                                              'statsTitle': 'Statistics',
                                              'stats': (
                                                        { 'key': 'Total Fonts Scanned', 'value': len(self.processedPostscriptNames), },
                                                        { 'key': 'Total Code Points Observed', 'value': len(self.glyphCountMap), },
                                                        ),
                                              }
#                              replaceMap = {'<!-- SVG Graph Placeholder -->': tableSvg,
#                                            }
                              )
#        self.processedPostscriptNames = set()
#        self.glyphCountMap = defaultdict(0)
#        self.glyphCountMap = {}

#    def writeOutput(self):
#        pass

    def processFont(self, filepath):
#        print
#        print 'filepath', filepath

        face = None

        try:
            face = freetype.Face(filepath)

            postscript_name = face.postscript_name
            if postscript_name not in self.processedPostscriptNames:
#                print '\t', 'postscript_name', postscript_name
                self.processedPostscriptNames.add(postscript_name)

                glyphs = []
                characterCode, glyphIndex = face.get_first_char();
#                while characterCode > 0 and glyphIndex > 0:
                while glyphIndex > 0:
                    if characterCode > 0:
                        glyphs.append(characterCode)
                    characterCode, glyphIndex = face.get_next_char(characterCode, 0);

                for glyph in glyphs:
                    self.glyphCountMap[glyph] = 1 + self.glyphCountMap.get(glyph, 0)

                if len(glyphs) > 0:
                    self.nonEmptyPostscriptNames.add(postscript_name)
                    pass
#                    print 'glyphs', len(glyphs), glyphs[0], glyphs[-1]
#                    print 'characterCode', type(characterCode), characterCode
                else:
                    print 'filepath', filepath
                    print 'no glyphs'
#                    print 'characterCode, glyphIndex', characterCode, glyphIndex

        except Exception, e:
            print e.message

        del face


    def processZip(self, filepath):
        with zipfile.ZipFile(filepath, 'r') as zf:
            for filename in zf.namelist():
                basename = filename
                if '/' in basename:
                    basename = basename[basename.rindex('/') + 1:]
#                print 'basename', basename, 'zip file', filename
                if basename.startswith('.'):
                    continue
                if (filename.lower().endswith('.otf') or
                    filename.lower().endswith('.ttf')):
#                    print '\t', 'zip file', filename

                    zf.extract(filename, self.tempdir)

                    filepath = os.path.join(self.tempdir, filename)

                    self.processFont(filepath)

                    if not os.path.exists(filepath):
                        raise Exception('Invalid temporary zip file: ' + filepath)
                    os.unlink(filepath)
                    if os.path.exists(filepath):
                        raise Exception('Could not delete temporary zip file: ' + filepath)


    def process(self):

        self.tempdir = tempfile.mkdtemp()
        print 'self.tempdir', self.tempdir

        def processPath(_, dirname, names):
#            if len(self.nonEmptyPostscriptNames) > 10:
#                return
            for filename in names:
                filepath = os.path.join(dirname, filename)
                if filename.startswith('.'):
                    continue
                if (filename.lower().endswith('.otf') or
                    filename.lower().endswith('.ttf')):
#                    print 'filepath', filepath
                    self.processFont(filepath)
                elif filename.lower().endswith('.zip'):
#                    print 'filepath', filepath
                    self.processZip(filepath)

        for src_path in self.src_paths:
            os.path.walk(src_path, processPath, None)

        shutil.rmtree(self.tempdir)

        self.dumpMetrics()

#        self.writeOutput()
#
#        self.dumpMetrics()


if __name__ == "__main__":
    import sys
    print 'sys.argv', sys.argv

    settings = getCommandLineSettings()
    print 'settings', settings
    GlyphImplementationAudit(settings).process()

    print
    print 'complete.'


