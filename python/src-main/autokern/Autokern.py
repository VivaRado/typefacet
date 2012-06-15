'''
robofont-extensions-and-scripts
Autokern.py

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
import time
import locale
import itertools
import yaml
import types
import unicodedata

locale.setlocale(locale.LC_ALL, 'en_US')

#from robofab.world import *
import robofab.world

from tfs.common.TFSFont import *
from AutokernSettings import AutokernSettings
#from tfs.common.TFSSilhouette import *
from tfs.common.TFTiming import TFTiming
from tfs.common.TFSMap import TFSMap
import tfs.common.TFSMath as TFSMath
from tfs.common.TFSPath import *
from tfs.common.TFSPoint import TFSPoint, scaleVectorHV
from tfs.common.TFSSegment import TFSSegment
from tfs.common.TFSOval import TFSOval
from tfs.common.TFSValidationException import TFSValidationException
import tfs.common.TFSIntersection as TFSIntersection
import tfs.common.UnicodeCharacterNames as UnicodeCharacterNames
#from collections import defaultdict


TFSMath.setFloatRoundingTolerance(0.1)
TFSMath.setDefaultPrecisionDigits(1)

AUTOKERN_SEGMENT_PRECISION = 16

USE_CACHED_KERNING_MAP = False
#USE_CACHED_KERNING_MAP = True

DEBUG_h_n_ISSUE = False
#DEBUG_h_n_ISSUE = True


DEFAULT_SAMPLE_TEXTS = (
               'Typography',
               'WAVE',
               'COLT',
               'Style',
               'enjoying',
               'hamburgerfont',
               'NNOOoo', # max distance
               'pqpiitt',
               'ijiJn.',
               'N-N=NtN',
               'TaLTLYPJ', # x-extrema overlap
               'VAWML4TO',
               'hhnnhn',
               'JFrf',
               'O!O?O.O;O;O,',
               'o!o?o.o;o;o,',
               'r!r?r.r;r;r,',
               'N!N?N.N;N;N,',
               )


def formatGlyphUnicode(glyph):
    if glyph.unicode is None:
        return 'None'
    else:
        return u'%d %s' % ( glyph.unicode,
                            hex(glyph.unicode), )

def formatUnicode(value):
    if value is None:
        return 'None'
    else:
        return '0x%X' % ( value, )

def formatGlyphName(glyph):
    if glyph.unicode is None:
        name = glyph.name
    elif glyph.name == unichr(glyph.unicode):
        name = glyph.name
    else:
        name = u'%s &#%d;' % ( glyph.name,
                               glyph.unicode, )
    return u'%s (%s)' % ( name,
                          formatGlyphUnicode(glyph), )

def mergeMustacheMaps(srcMap, dstMap, prefix):
    for key, value in srcMap.items():
        dstMap[prefix + key] = value

def formatEms(value):
    return '%0.3f em' % (value,)

def formatTimeDuration(value):
    if value < 60:
        return '%d seconds' % int(round(value))
    if value < 60 * 60:
        return time.strftime('%M:%S', time.gmtime(value))
    if value < 60 * 60 * 24:
        return time.strftime('%H:%M:%S', time.gmtime(value))
    hmsValue = value % (60 * 60 * 24)
    daysValue = int(round((value - hmsValue) / (60 * 60 * 24)))
    return '%d days, %s' % ( daysValue,
                             time.strftime('%H:%M:%S', time.gmtime(hmsValue)), )


class AutokernCache(TFSMap):

    def __init__(self):
        TFSMap.__init__(self)

    def getCachedValue(self, key, func, *argv):
        if key in self:
            return self[key]
        result = func(*argv)
        self[key] = result
        return result

    def getGlyphContours(self, ufoglyph):
        def getCachedContours():
            contours = ufoglyph.getContours(warnings=False)
            return contours
        return self.getCachedValue('getCachedContours %s' % ufoglyph.name, getCachedContours)

    def getContoursMinmax(self, ufoglyph):
        def getCachedMinmax():
            contours = self.getGlyphContours(ufoglyph)
            return minmaxPathsEvaluated(contours, AUTOKERN_SEGMENT_PRECISION)
        return self.getCachedValue('getCachedMinmax %s' % ufoglyph.name, getCachedMinmax)


class Autokern(TFSMap):

    def __init__(self, argumentsMap):
        TFSMap.__init__(self)
        self.argumentsMap = argumentsMap
        for key, value in argumentsMap.items():
            setattr(self, key, value)


    def configureLogging(self):

        if self.log_path is None:
            return

        OVERWRITE_LOGS = True
#            OVERWRITE_LOGS = False

        if OVERWRITE_LOGS:
            if os.path.exists(self.log_path):
                shutil.rmtree(self.log_path)
            if os.path.exists(self.log_path):
                raise Exception('Could not clear log_path: %s' % self.log_path)

        if not os.path.exists(self.log_path):
            os.mkdir(self.log_path)
        if not (os.path.exists(self.log_path) and os.path.isdir(self.log_path)):
            raise Exception('Invalid log_path: %s' % self.log_path)

        if OVERWRITE_LOGS:
            def makeLogSubfolder(parent, name):
                subfolder = os.path.abspath(os.path.join(parent, name))
                os.mkdir(subfolder)
                if not (os.path.exists(subfolder) and os.path.isdir(subfolder)):
                    raise Exception('Invalid log_path: %s' % self.log_path)
                return subfolder

            self.html_folder = makeLogSubfolder(self.log_path, 'html')
            self.css_folder = makeLogSubfolder(self.html_folder, 'stylesheets')
#            self.svg_folder = makeLogSubfolder(self.html_folder, 'svg')

            import tfs.common.TFSProject as TFSProject
            srcCssFile = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', 'styles.css'))
            dstCssFile = os.path.abspath(os.path.join(self.css_folder, os.path.basename(srcCssFile)))
            shutil.copy(srcCssFile, dstCssFile)
        else:
            self.html_folder = os.path.join(self.log_path, 'html')
            self.css_folder = os.path.join(self.html_folder, 'stylesheets')
#            self.svg_folder = os.path.join(self.html_folder, 'svg')

        self.kerningPairLogFilenames = set()
        self.logFileTuples = []


    def configure(self):

        self.dstCache = AutokernCache()
        self.srcCache = AutokernCache()

        ufo_src_path = self.ufo_src_path
        if ufo_src_path is None:
            raise Exception('Missing ufo_src_path')
        if not (os.path.exists(ufo_src_path) and os.path.isdir(ufo_src_path) and os.path.basename(ufo_src_path).lower().endswith('.ufo')):
            raise Exception('Invalid ufo_src_path: %s' % ufo_src_path)

        self.srcUfoFont = TFSFontFromFile(ufo_src_path)
        self.dstUfoFont = TFSFontFromFile(ufo_src_path)
        self.srcFilename = os.path.basename(ufo_src_path)
        self.src_kerning_value_count = self.srcUfoFont.getKerningPairCount()
        self.glyph_count = len(self.srcUfoFont.getGlyphs())


        if self.ufo_dst_path is None:
            raise Exception('Missing ufo_dst_path')
        if os.path.exists(self.ufo_dst_path):
            if os.path.isdir(self.ufo_dst_path):
                shutil.rmtree(self.ufo_dst_path)
            elif os.path.isfile(self.ufo_dst_path):
                os.unlink(self.ufo_dst_path)
            if os.path.exists(self.ufo_dst_path):
                raise Exception('Could not overwrite: %s' % (self.ufo_dst_path,))


        self.configureLogging()


        self.units_per_em = int(round(self.dstUfoFont.units_per_em))
        for key, value in self.argumentsMap.items():
            if key.endswith('_ems'):
                setattr(self, key[:-len('_ems')], value * self.units_per_em)
        self.precision = int(round(self.precision))

        self.ascender = self.srcUfoFont.ascender
        self.descender = self.srcUfoFont.descender
        self.ascender_ems = self.srcUfoFont.ascender / float(self.units_per_em)
        self.descender_ems = self.srcUfoFont.descender / float(self.units_per_em)

        self.timing = TFTiming()
        self.advanceMap = {}
        self.rasterCache = {}
        self.pixelsCache = {}
        self.pairsToKern = None
        self.glyphsToKern = None
        self.sampleTexts = list(DEFAULT_SAMPLE_TEXTS)

        #

        import AutokernGlyphClasses
        allGlyphCategories = AutokernGlyphClasses.unicodedataCategoryMap.keys()

        glyphs = self.srcUfoFont.getGlyphs()
        glyphCodePoints = set()
        glyphNames = set()
        glyphCodePointToNameMap = {}
        self.ignoredGlyphNames = set()
        for glyph in glyphs:
            if glyph.unicode is not None:
                glyphCodePoints.add(glyph.unicode)
            if glyph.name is None:
                raise Exception('Glyph missing name')
            if glyph.name in glyphNames:
                raise Exception('Duplicate glyph name: ' + glyph.name)
            glyphNames.add(glyph.name)
            if glyph.unicode is not None:
                glyphCodePointToNameMap[glyph.unicode] = glyph.name
#            if self.isIgnoredGlyph(glyph):
#                self.ignoredGlyphNames.add(glyph.name)

        #

        if self.extra_sample_texts is not None:
            if len(self.extra_sample_texts) < 1:
                raise Exception('Missing --extra-sample-texts value')
            for sampleText in self.extra_sample_texts:
                if len(sampleText) < 1:
                    raise Exception('Invalid --extra-sample-texts value: %s' % sampleText)
                for glyph in sampleText:
                    if ord(glyph) not in glyphCodePoints:
                        raise Exception('--extra-sample-texts value: %s has unknown glyph: %s' % (sampleText, glyph,))

            # Prepend extra sample texts.
            self.sampleTexts = self.extra_sample_texts + self.sampleTexts

        #

        self.ignoredGlyphNames.add('.notdef')
        if self.glyphs_to_ignore is not None:
#            ignoreArguments.append('--glyphs-to-ignore')
            if len(self.glyphs_to_ignore) < 1:
                raise Exception('Missing --glyphs-to-ignore value')
            for value in self.glyphs_to_ignore:
                self.ignoredGlyphNames.add(self.parseCodePoint('--glyphs-to-ignore', glyphNames, value))
        if self.glyph_categories_to_ignore is not None:
#            ignoreArguments.append('--glyph-categories-to-ignore')
            if len(self.glyph_categories_to_ignore) < 1:
                raise Exception('Missing --glyph-categories-to-ignore value')


            for glyph in glyphs:
                if glyph.name == '.notdef':
                    continue
                category = self.getUnicodeCategory(glyph)
                if category is None:
                    print 'Missing glyph category:', glyph.name
                else:
                    categoryMajor = category[:-1] + '*'
                    if ((category in self.glyph_categories_to_ignore) or
                        (categoryMajor in self.glyph_categories_to_ignore)):
                        self.ignoredGlyphNames.add(glyph.name)
                    elif ((category not in allGlyphCategories) and
                        (categoryMajor not in allGlyphCategories)):
                        print 'Unknown glyph category:', glyph.name, category
#                    else:
#                        if self.isIgnoredGlyph(glyph):
#                            print '\t', 'ignored Glyph?', glyph.name, 'category', category

        print 'ignoring %d glyphs' % len(self.ignoredGlyphNames)

        #

        scopeArguments = []
        if self.glyph_pairs_to_kern is not None:
            scopeArguments.append('--glyph-pairs-to-kern')
            if len(self.glyph_pairs_to_kern) < 1:
                raise Exception('Missing --glyph-pairs-to-kern value')
            if len(self.glyph_pairs_to_kern) % 2 != 0:
                raise Exception('Uneven number of  --glyph-pairs-to-kern values')
            self.pairsToKern = set()
            for index in xrange(len(self.glyph_pairs_to_kern) / 2):
                value0 = self.glyph_pairs_to_kern[index * 2 + 0]
                value1 = self.glyph_pairs_to_kern[index * 2 + 1]
                name0 = self.parseCodePoint('-glyph-pairs-to-kern', glyphNames, value0)
                name1 = self.parseCodePoint('-glyph-pairs-to-kern', glyphNames, value1)
                if name0 in self.ignoredGlyphNames or name1 in self.ignoredGlyphNames:
                    print 'ignoring --pairs-to-kern value:', value
                else:
                    self.pairsToKern.add(( name0, name1, ))
        if self.glyphs_to_kern is not None:
            scopeArguments.append('--glyphs-to-kern')
            if len(self.glyphs_to_kern) < 1:
                raise Exception('Missing --glyphs-to-kern value')
            self.glyphsToKern = set()
#            print 'self.glyphs_to_kern', self.glyphs_to_kern
            for value in self.glyphs_to_kern:
                name = self.parseCodePoint('--glyphs-to-kern', glyphNames, value)
                if name in self.ignoredGlyphNames:
                    print 'ignoring --glyphs-to-kern value:', value
                else:
                    self.glyphsToKern.add(name)
        if self.kern_samples_only:
            scopeArguments.append('--kern-samples-only')
            self.pairsToKern = set()
            for sampleText in self.sampleTexts:
                lastGlyphName = None
                for glyph in sampleText:
                    if ord(glyph) not in glyphCodePointToNameMap:
                        '''
                        We've already validated the "extra" sample texts.
                        Ignore missing characters in the default sample texts.
                        '''
                        continue
                    glyphName = glyphCodePointToNameMap.get(ord(glyph))
                    if glyphName is not None and lastGlyphName is not None:
                        self.pairsToKern.add( (lastGlyphName, glyphName,) )
                    lastGlyphName = glyphName
            print 'kerning %d pairs' % len(self.pairsToKern)

        if len(scopeArguments) > 1:
            raise Exception('Do not use more than one of the %s arguments.' % (' '.join(scopeArguments),))

        #

        def isValidGlyphCategories(key, value):
            if type(value) not in ( types.StringType,
                                    types.UnicodeType, ):
                raise Exception('Invalid %s value: %s' % (key, value,))
            if value in allGlyphCategories:
                return value
            if value[-1] == '*':
                valueMajor = value[:-1]
                categoriesMajor = set([category[0] for category in allGlyphCategories])
                if valueMajor in categoriesMajor:
                    return value
            raise Exception('Invalid unicodedata category value: ' + value)


        self.max_x_extrema_overlap_categoryMap = {}
        if self.max_x_extrema_overlap_ems_per_category is not None:
            if len(self.max_x_extrema_overlap_ems_per_category) < 1:
                raise Exception('Missing --max-x-extrema-overlap-ems-per-category value')
            if len(self.max_x_extrema_overlap_ems_per_category) % 2 != 0:
                raise Exception('Uneven number of  --max-x-extrema-overlap-ems-per-category values')
            for index in xrange(len(self.max_x_extrema_overlap_ems_per_category) / 2):
                value0 = self.max_x_extrema_overlap_ems_per_category[index * 2 + 0]
                value1 = self.max_x_extrema_overlap_ems_per_category[index * 2 + 1]
                isValidGlyphCategories('--max-x-extrema-overlap-ems-per-category', value0)
                try:
                    value1 = float(value1) * self.units_per_em
                except ValueError, e:
                    raise Exception('Invalid --max-x-extrema-overlap-ems-per-category value: %s' % str(value1))

                self.max_x_extrema_overlap_categoryMap[value0] = value1

        #

        minmax = None
        for ufoglyph in self.dstUfoFont.getGlyphs():
            contours = self.dstCache.getGlyphContours(ufoglyph)
            if len(contours) < 1:
                continue
            glyphMinmax = self.dstCache.getContoursMinmax(ufoglyph)
            minmax = minmaxMerge(minmax, glyphMinmax)
        self.allGlyphsMinY = minmax.minY
        self.allGlyphsMaxY = minmax.maxY

    def getGlyphCategoryValue(self, categoryMap, glyph):
        category = self.getUnicodeCategory(glyph)
        if category is None:
            return None
        if category in categoryMap:
            return categoryMap[category]
        categoryMajor = category[:-1] + '*'
        if categoryMajor in categoryMap:
            return categoryMap[categoryMajor]
        return None

    def getGlyphPairCategoryValue(self, categoryMap, func, defaultValue, glyph0, glyph1):
        value0 = self.getGlyphCategoryValue(categoryMap, glyph0)
        value1 = self.getGlyphCategoryValue(categoryMap, glyph1)
        if value0 is None and value1 is None:
            return defaultValue
        if value0 is None:
            return value1
        if value1 is None:
            return value0
        return func(value0, value1)

    def getGlyphPairMaxXExtremaOverlap(self, glyph0, glyph1):
        return self.getGlyphPairCategoryValue(self.max_x_extrema_overlap_categoryMap,
                                              max,
                                              -self.max_x_extrema_overlap,
                                              glyph0, glyph1)

    def formatUnitsInEms(self, value):
        return formatEms(value / float(self.units_per_em))

    def addSidebarMustacheMap(self, mustacheMap, kerned, complete=False):
        vars = (
                ( 'Filename', 'srcFilename',),
                ( 'Family', 'familyName',),
                ( 'Style', 'styleName',),
                ( 'Units per em', 'units_per_em',),
                ( 'Ascender', 'ascender_ems',),
                ( 'Descender', 'descender_ems',),
                ( 'Precision', 'precision_ems',),
#                ( 'Minimum Distance', 'min_distance_ems',),
#                ( 'Maximum Distance', 'max_distance_ems',),
#                ( 'Tracking', 'tracking_ems',),
#                ( 'Intrusion Tolerance', 'intrusion_tolerance_ems',),
##                ( 'Intrusion Min. Thickness', 'intrusion_min_thickness_ems',),
#                ( 'Max. x-extrema Overlap', 'max_x_extrema_overlap_ems',),
#                ( 'x-extrema Overlap Scaling', 'x_extrema_overlap_scaling',),
                ( 'Glyph Count', 'glyph_count',),
                )

        if kerned:
            vars += (
                ( 'Original Kerning Values', 'src_kerning_value_count',),
                ( 'Kerned Pairs', 'kerned_pairs_count',),
                ( 'Valid Kerning Values', 'valid_kerned_pairs_count',),
                )
            if self.max_kerning_pairs:
                vars += (
                    ( 'Final Kerning Values', 'final_kerned_pairs_count',),
                    )

        if complete:
            vars += (
                ( 'Elapsed', 'elapsedDatetime',),
                ( 'Completed', 'finishDatetime',),
                )

        varMaps = []
        for name, key in vars:
            varMaps.append({'sidebarVarName': name,
                            'sidebarVarValue': mustacheMap[key],
                            })
        mustacheMap['sidebarVars'] = varMaps

        argMaps = []
        for key in sorted(self.argumentsMap):
            value = self.argumentsMap[key]
            if key.endswith('_path'):
                continue
            if value is None:
                continue
            if type(value) == types.BooleanType:
                if value:
                    argMaps.append({'sidebarVarName': '--' + key.replace('_', '-'),
                                    'sidebarVarValue': '',
                                    })
                continue
            elif type(value) in ( types.ListType, types.TupleType, ):
                value = ', '.join([str(item) for item in value])
            argMaps.append({'sidebarVarName': '--' + key.replace('_', '-'),
                            'sidebarVarValue': value,
                            })
        mustacheMap['sidebarArgs'] = argMaps


    def makeDefaultMustacheMap(self, localsMap=None):

        mustacheMap = {}

        def addToMustacheMap(key, value):
            if type(value) not in ( types.IntType,
                                    types.LongType,
                                    types.FloatType,
                                    types.UnicodeType,
                                    types.StringType, ):
                return

            if type(value) in ( types.IntType,
                                    types.LongType):
                value = locale.format("%d", value, grouping=True)

            if key not in mustacheMap:
                mustacheMap[key] = value

#        for attr in dir(self):
##            print 'attr', attr
#            if attr.startswith('_'):
#                continue
#            value = getattr(self, attr)
#
#            if attr.endswith('_ems'):
#                value = '%0.3f em' % (value, )
#
#            addToMustacheMap(attr, value)

        for key, value in self.items():
            if key.endswith('_ems'):
                value = formatEms(value)
            elif type(value) in ( types.IntType,
                                    types.FloatType,
                                    types.LongType,):
                emsKey = key + '_in_ems'
                emsValue = formatEms(value / float(self.units_per_em))
                addToMustacheMap(emsKey, emsValue)
            addToMustacheMap(key, value)

        if localsMap:
            for key, value in localsMap.items():
                if type(value) in ( types.IntType,
                                    types.FloatType,
                                    types.LongType,):
                    emsKey = key + '_in_ems'
                    emsValue = formatEms(value / float(self.units_per_em))
                    addToMustacheMap(emsKey, emsValue)
                addToMustacheMap(key, value)

        for key in (
                     'unitsPerEm',
                     'familyName',
                     'styleName',
                     'fullName',
                     'fontName',
                    ):
            mustacheMap[key] = getattr(self.dstUfoFont.info, key)

#        print 'mustacheMap', mustacheMap
#        print 'mustacheMap'
#        for key, value in mustacheMap.items():
#            if type(value) in (types.StringType, types.UnicodeType,) and len(value) > 100:
#                value = value[:100] + '...'
#            print '\t', key, value
#        print

        return mustacheMap


    def getUnicodeCategory(self, glyph):
        def getUnicodeCategory_():
            if glyph.unicode is None:
                return None
            uc = unichr(glyph.unicode)
            if uc is not None:
                unicode_category = unicodedata.category(uc)
                return unicode_category
            return None
        return self.srcCache.getCachedValue('getUnicodeCategory: %s' % glyph.name, getUnicodeCategory_)


    def hasUnicodeCategoryPrefix(self, glyph, prefixes, exceptions=None):
        '''
        The unicodedata glyph categories are:
        L Letter
        M Mark
        N Number
        P Punctuation
        Z Separator
        S Symbol
        C Other
        '''
        unicode_category = self.getUnicodeCategory(glyph)
        if unicode_category is not None:
            if exceptions:
                if unicode_category in exceptions:
                    return False
            if unicode_category[0] in prefixes:
                return True
        return False


    def subrenderGlyphContours(self, tfsSvg, contours, strokeColor, addPoints=True):
        from tfs.common.TFSSvg import TFSSvgPath
        ON_POINT_COLOR = 0x7f7f7f7f
        CONTROL_POINT_COLOR = 0x7fafafaf
        for contour in contours:
#            tfsSvg.addItem(TFSSvgPath(contour).addStroke(strokeColor, 2).addPointHighlights(ON_POINT_COLOR, CONTROL_POINT_COLOR))

            svgPath = TFSSvgPath(contour).addStroke(strokeColor, 2)
            if addPoints:
                svgPath.addPointHighlights(ON_POINT_COLOR, CONTROL_POINT_COLOR)
            tfsSvg.addItem(svgPath)


    def renderSvgScene(self,
                       filename,
                       pathTuples = (),
                       strokePathTuples = None,
                       fillPathTuples = None,
                       hGuidelines=None,
                       hRanges=None,
                       textTuples=None,
                       width=None, height=None, maxWidth=None, maxHeight=None,
                       padding=None):

        from tfs.common.TFSSvg import TFSSvg, TFSSvgPath
        if filename is None:
            dstFile = filename
        else:
            filename = '%s.svg' % ( filename, )
            dstFile = os.path.abspath(os.path.join(self.svg_folder, filename))

        CANVAS_BACKGROUND_COLOR = 0xffffffff
        CANVAS_BORDER_COLOR = 0x07fbfbfbf
        tfsSvg = TFSSvg().withBackground(CANVAS_BACKGROUND_COLOR).withBorder(CANVAS_BORDER_COLOR)

    #    if pathTuples:
        for color, contours in pathTuples:
            self.subrenderGlyphContours(tfsSvg, contours, color)
        if strokePathTuples is not None:
            for color, contours in strokePathTuples:
                self.subrenderGlyphContours(tfsSvg, contours, color, addPoints=False)
        if fillPathTuples is not None:
            for color, contours in fillPathTuples:
                for contour in contours:
                    tfsSvg.addItem(TFSSvgPath(contour).addFill(color))
        if textTuples is not None:
            for textMap in textTuples:
                tfsSvg.addText(textMap.text, textMap.origin, textMap.fillColor, **textMap.params)

        if hGuidelines:
            for hGuideline in hGuidelines:
                p0 = TFSPoint(hGuideline, self.dstUfoFont.info.descender)
                p1 = TFSPoint(hGuideline, self.dstUfoFont.info.ascender)
                GUIDELINE_COLOR = 0x7fdfdfdf
                tfsSvg.addItem(TFSSvgPath(openPathWithPoints(p0, p1)).addStroke(GUIDELINE_COLOR, 1))

        if hRanges:
            for hRange in hRanges:
                rangeName, rangeLeft, rangeRight = hRange
                if rangeLeft == rangeLeft:
                    continue
                p0 = TFSPoint(rangeLeft, int(round(self.max_distance * -1.3)))
                p1 = TFSPoint(rangeRight, int(round(self.max_distance * -1.3)))
                H_RANGE_COLOR = 0xaf3f3faf
                tfsSvg.addItem(TFSSvgPath(openPathWithPoints(p0, p1)).addStroke(H_RANGE_COLOR, 3))

        vGuidelines = ( 0,
                        self.dstUfoFont.info.ascender,
                        self.dstUfoFont.info.descender,
                        )
        if vGuidelines:
            minmax = None
            allPathTuples = pathTuples
            if strokePathTuples is not None:
                allPathTuples = allPathTuples + strokePathTuples
            if fillPathTuples is not None:
                allPathTuples = allPathTuples + fillPathTuples
            for color, contours in allPathTuples:
                minmax = minmaxMerge(minmax, minmaxPaths(contours))

            for vGuideline in vGuidelines:
                p0 = TFSPoint(0, vGuideline)
                p1 = TFSPoint(minmax.maxX, vGuideline)
                GUIDELINE_COLOR = 0x7fdfdfdf
                tfsSvg.addItem(TFSSvgPath(openPathWithPoints(p0, p1)).addStroke(GUIDELINE_COLOR, 1))

        if set((width, height, maxWidth, maxHeight,)) == set((None,)):
            SVG_HEIGHT = 400
            SVG_MAX_WIDTH = 800
            height = SVG_HEIGHT
            maxWidth = SVG_MAX_WIDTH

        self.timing.mark('renderSvgScene.0')
        svgdata = tfsSvg.renderToFile(dstFile,
                                      margin=10,
                                      timing=self.timing,
                                      width=width, height=height, maxWidth=maxWidth, maxHeight=maxHeight,
                                      padding=padding)
        self.timing.mark('renderSvgScene.1')
        if filename is not None:
            return filename
        else:
            return svgdata


    def buildKerningInfoMap(self, ufofont, ufoglyph0, ufoglyph1, cache):
        if (ufoglyph0.name is None) or (ufoglyph1.name is None):
            return None
        kerningInfo = TFSMap()
        kerningInfo.ufoglyph0 = ufoglyph0
        kerningInfo.ufoglyph1 = ufoglyph1
        kerningInfo.name0 = ufoglyph0.name
        kerningInfo.name1 = ufoglyph1.name
        kerningInfo.kerningValue = ufofont.getKerningPair(ufoglyph0.name, ufoglyph1.name)
        if kerningInfo.kerningValue is None:
            kerningInfo.kerningValue = 0
        kerningInfo.contours0 = cache.getGlyphContours(ufoglyph0)
        if (kerningInfo.contours0 is None) or (len(kerningInfo.contours0) < 1):
            return None
        kerningInfo.contours1 = cache.getGlyphContours(ufoglyph1)
        if (kerningInfo.contours1 is None) or (len(kerningInfo.contours1) < 1):
            return None
        kerningInfo.minmax0 = cache.getContoursMinmax(ufoglyph0)
        kerningInfo.minmax1 = cache.getContoursMinmax(ufoglyph1)
        kerningInfo.xAdvance = ufoglyph0.xAdvance
        kerningInfo.kernedAdvance = kerningInfo.xAdvance + kerningInfo.kerningValue
        kerningInfo.x_extrema_overlap = kerningInfo.minmax0.maxX - (kerningInfo.minmax1.minX + kerningInfo.kernedAdvance)
        return kerningInfo


    def buildKerningInfoMaps(self, ufofont, ufoglyphs, cache):
        result = {}
        for ufoglyph0 in ufoglyphs:
            for ufoglyph1 in ufoglyphs:
                kerningInfo = self.buildKerningInfoMap(ufofont, ufoglyph0, ufoglyph1, cache)
                if kerningInfo is not None:
                    result[(ufoglyph0.name, ufoglyph1.name,)] = kerningInfo
        return result


    def findDisparities(self):

        srcGlyphs = self.srcUfoFont.getGlyphs()
        dstGlyphs = self.dstUfoFont.getGlyphs()

        srcKerningInfoMap = self.buildKerningInfoMaps(self.srcUfoFont, srcGlyphs, self.srcCache)
        dstKerningInfoMap = self.buildKerningInfoMaps(self.dstUfoFont, dstGlyphs, self.dstCache)

        disparities = []
        for key, srcKerning in srcKerningInfoMap.items():
            if key not in dstKerningInfoMap:
                print 'Missing output kerning info for pair:', key
                continue
            dstKerning = dstKerningInfoMap[key]
            disparity = TFSMap()
            disparity.key = key
            disparity.srcKerning = srcKerning
            disparity.dstKerning = dstKerning
            disparity.disparity = abs(srcKerning.x_extrema_overlap - dstKerning.x_extrema_overlap)
            disparities.append(disparity)

        def cmpDisparities(d0, d1):
            return cmp(d0.disparity, d1.disparity)
        disparities.sort(cmpDisparities, reverse=True)
        return disparities


    def logDisparitiesGroup(self, disparities, groupName, filterFunc=None):

        '''
        We're only interested in the top 100 disparities.
        '''
        self.disparity_log_count = max(0, self.disparity_log_count)

        # Remove empty values.
        disparities = [disparity for disparity in disparities if disparity.disparity != 0]

        if filterFunc is not None:
            filtered_disparities = []
            for disparity in disparities:
                if filterFunc(disparity.srcKerning.ufoglyph0, disparity.srcKerning.ufoglyph1):
                    filtered_disparities.append(disparity)
                    if len(filtered_disparities) >= self.disparity_log_count:
                        break
            disparities = filtered_disparities
        else:
            disparities = disparities[:self.disparity_log_count]

        if len(disparities) < 1:
            return

        def getDisparityFilename(index):
            return 'disparity-%s-%d.html' % ( groupName.lower().replace(' ', '_'),
                                              index, )

        disparityLinkMaps = []
        for index, disparity in enumerate(disparities):
            disparityLinkMaps.append({ 'filename': getDisparityFilename(index),
                                      'name': str(index + 1),
                                      })

        for index, disparity in enumerate(disparities):
            filenamePrefix = 'disparity-%d' % index
            srcAdvanceSvg = self.renderSvgScene(None,
                                             pathTuples = (
                                                           ( 0x7f7faf7f, disparity.srcKerning.contours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(disparity.srcKerning.kernedAdvance, 0)) for contour in disparity.srcKerning.contours1], ),
                                                           ),
                                             hGuidelines = ( disparity.srcKerning.kernedAdvance, ) )

            dstAdvanceSvg = self.renderSvgScene(None,
                                             pathTuples = (
                                                           ( 0x7f7faf7f, disparity.dstKerning.contours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(disparity.dstKerning.kernedAdvance, 0)) for contour in disparity.dstKerning.contours1], ),
                                                           ),
                                             hGuidelines = ( disparity.dstKerning.kernedAdvance, ) )

            pageTitle0 = u'Autokern Disparity (%s):' % ( groupName, )
            pageTitle1 = u'%s vs. %s' % ( formatGlyphName(disparity.srcKerning.ufoglyph0),
                                          formatGlyphName(disparity.srcKerning.ufoglyph1), )

            def formatEmScalar(value):
                return formatEms(value / float(self.units_per_em))

            def formatGlyphMap(glyph, srcMinmax, dstMinmax):
                return {
                           'glyphName': formatGlyphName(glyph),
                           'srcMinX': formatEmScalar(srcMinmax.minX),
                           'srcMaxX': formatEmScalar(srcMinmax.maxX),
                           'dstMinX': formatEmScalar(dstMinmax.minX),
                           'dstMaxX': formatEmScalar(dstMinmax.maxX),
                        }

            localsMap = {}
            localsMap.update(locals())
            localsMap.update(disparity)

            mergeMustacheMaps(disparity.srcKerning, localsMap, 'src_')
            mergeMustacheMaps(disparity.srcKerning.minmax0, localsMap, 'src0_')
            mergeMustacheMaps(disparity.srcKerning.minmax1, localsMap, 'src1_')
            mergeMustacheMaps(disparity.dstKerning, localsMap, 'dst_')
            mergeMustacheMaps(disparity.dstKerning.minmax0, localsMap, 'dst0_')
            mergeMustacheMaps(disparity.dstKerning.minmax1, localsMap, 'dst1_')

            mustacheMap = self.makeDefaultMustacheMap(localsMap=localsMap)
            self.addSidebarMustacheMap(mustacheMap, kerned=True)

            mustacheMap.update({
                           'pageTitle0': pageTitle0,
                           'pageTitle1': pageTitle1,

                           'disparityLinkMaps': disparityLinkMaps,
                           'firstDisparityLink': getDisparityFilename(0),
                           'lastDisparityLink': getDisparityFilename(len(disparities) - 1),
                           })
            if index > 0:
                mustacheMap['prevDisparityLink'] = {'filename': getDisparityFilename(index - 1), }
            if index + 1 < len(disparities):
                mustacheMap['nextDisparityLink'] = {'filename': getDisparityFilename(index + 1), }

            kerningLogFilename = self.getKerningPairHtmlFilename(disparity.srcKerning.ufoglyph0,
                                                                 disparity.srcKerning.ufoglyph1),
            if kerningLogFilename in self.kerningPairLogFilenames:
                mustacheMap['kerningLogFilename'] = kerningLogFilename

            self.writeLogFile('autokern_disparity_template.txt',
                              getDisparityFilename(index),
                              'Disparities: ' + groupName,
                              '''
    The top disparities between the original kerning and Autokern's kerning.
                              ''',
                              '%d' % (index + 1),
                              mustacheMap)


    def logDisparities(self):

        renderLog = self.log_path is not None
        if not renderLog:
            return
        if (self.disparity_log_count is None) or (self.disparity_log_count < 1):
            return

        print 'Logging disparities...'

        disparities = self.findDisparities()

        def isRomanLetter(ufoglyph):
            if len(ufoglyph.name) != 1:
                return False
            return ord('A') <= ord(ufoglyph.name.upper()) <= ord('Z')
        def romanLettersFilter(ufoglyph0, ufoglyph1):
            return isRomanLetter(ufoglyph0) and isRomanLetter(ufoglyph1)
        self.logDisparitiesGroup(disparities, 'Roman Letters', filterFunc=romanLettersFilter)

        def isArabNumeral(ufoglyph):
            if ufoglyph.unicode is None:
                return False
            return ord('0') <= ufoglyph.unicode <= ord('9')
        def arabNumeralsFilter(ufoglyph0, ufoglyph1):
            return isArabNumeral(ufoglyph0) and isArabNumeral(ufoglyph1)
        self.logDisparitiesGroup(disparities, 'Arab Numerals', filterFunc=arabNumeralsFilter)

        '''
        The unicodedata glyph categories are:
        L Letter
        M Mark
        N Number
        P Punctuation
        Z Separator
        S Symbol
        C Other
        '''
        def lettersAndNumbersFilter(ufoglyph0, ufoglyph1):
            unicodeCategoryPrefixes = ('L','N',)
            unicodeCategoryExceptions = ('Lm',)
            return (self.hasUnicodeCategoryPrefix(ufoglyph0, prefixes=unicodeCategoryPrefixes, exceptions=unicodeCategoryExceptions) and
                    self.hasUnicodeCategoryPrefix(ufoglyph1, prefixes=unicodeCategoryPrefixes, exceptions=unicodeCategoryExceptions))
        self.logDisparitiesGroup(disparities, 'Letters And Numbers', filterFunc=lettersAndNumbersFilter)

        self.logDisparitiesGroup(disparities, 'All')


    def getFilenamePrefixPair(self, prefix, ufoglyph0, ufoglyph1):
        return '%s-%s-%s' % ( prefix,
                              formatUnicode(ufoglyph0.unicode),
                              formatUnicode(ufoglyph1.unicode), )

    def getKerningPairFilenamePrefix(self, ufoglyph0, ufoglyph1):
        return self.getFilenamePrefixPair('autokern', ufoglyph0, ufoglyph1)

    def getKerningPairHtmlFilename(self, ufoglyph0, ufoglyph1):
        return self.getKerningPairFilenamePrefix(ufoglyph0, ufoglyph1) + '.html'


    def convertProfileToLogPaths(self, profile, isLeft, offset=None):
        minYunits = int(math.floor((self.allGlyphsMinY - self.max_distance) / float(self.precision)))

        result = []

        def addPath(points):
            firstPoint = points[0]
            lastPoint = points[-1]
            if isLeft:
                extraX = reduce(min, [point.x for point in points])
#                extraX = min(firstPoint.x, lastPoint.x)
                extraX += -10
            else:
                extraX = reduce(max, [point.x for point in points])
#                extraX = max(firstPoint.x, lastPoint.x)
                extraX += +10

            points.append(TFSPoint(extraX, lastPoint.y))
            points.append(TFSPoint(extraX, firstPoint.y))

            if offset is not None:
                points = [point.plus(offset) for point in points]

            result.append(concatenatePath(True, *points))

        currentPoints = []
        for index, xValue in enumerate(profile):
            if xValue is None:
                if len(currentPoints) > 0:
                    '''
                    Tie off path
                    '''
                    addPath(currentPoints)
                    currentPoints = []
            else:
                yValue = self.precision * (index + minYunits)
#                print 'convertProfileToLogPaths point', 'yValue', yValue, 'precision', self.precision, 'index', index, 'minYunits', minYunits, 'xValue', xValue
                currentPoints.append(TFSPoint(xValue, yValue))

        if len(currentPoints) > 0:
            '''
            Tie off path
            '''
            addPath(currentPoints)

        return result


    def makeProfile(self, paths=None, segments=None, debug=False):
        maxYunits = int(math.ceil((self.allGlyphsMaxY + self.max_distance) / float(self.precision)))
        minYunits = int(math.floor((self.allGlyphsMinY - self.max_distance) / float(self.precision)))
        yHeightUnits = 1 + maxYunits - minYunits

#        print 'maxYunits', maxYunits
#        print 'minYunits', minYunits
#        print 'self.allGlyphsMinY', self.allGlyphsMinY
#        print 'self.allGlyphsMaxY', self.allGlyphsMaxY
#        print 'self.precision', self.precision
#        print 'yHeightUnits', yHeightUnits

        maxProfile = list((None,) * yHeightUnits)
        minProfile = list((None,) * yHeightUnits)

        # combine paths and segments parameters
        allSegments = []
        if segments is not None:
            allSegments.extend(segments)
        if paths is not None:
            for path in paths:
                allSegments.extend(path.segments)

        def addProfilePoint(yIndex, xValue):
            if yIndex < 0 or yIndex >= len(maxProfile):
                raise Exception('Invalid yIndex: %d' % yIndex)
#            print 'yIndex', yIndex, 'len(profile)', len(profile)
            if debug:
                print 'yIndex', yIndex, 'xValue', xValue
            if maxProfile[yIndex] is None:
                minProfile[yIndex] = maxProfile[yIndex] = xValue
            else:
                minProfile[yIndex] = min(minProfile[yIndex], xValue)
                maxProfile[yIndex] = max(maxProfile[yIndex], xValue)

        def addSegmentSection(point0, point1):
            '''
            Given two endpoints of a straight segment, interpolate x values along the y-axis.

            Not very precise; rounds y value of endpoint locations.
            Acceptable; as precise as "precision".
            '''
            y0u = int(round(point0.y / float(self.precision)))
            y1u = int(round(point1.y / float(self.precision)))
#            y0u = int(round((point0.y - self.max_distance) / float(self.precision)))
#            y1u = int(round((point1.y - self.max_distance) / float(self.precision)))

            if debug:
                print 'addSegmentSection', point0.description(), point1.description(), 'y0u', y0u, 'y1u', y1u

            if y0u == y1u:
                yIndex = y0u - minYunits
                addProfilePoint(yIndex, point0.x)
                addProfilePoint(yIndex, point1.x)
                return

            if y0u < y1u:
                minYIndex = y0u - minYunits
                maxYIndex = y1u - minYunits
                minXValue = point0.x
                maxXValue = point1.x
            else:
                minYIndex = y1u - minYunits
                maxYIndex = y0u - minYunits
                minXValue = point1.x
                maxXValue = point0.x

            for yIndexOffset in xrange(1 + maxYIndex - minYIndex):
                yIndex = minYIndex + yIndexOffset
                xValue = minXValue + (maxXValue - minXValue) * yIndexOffset / float(maxYIndex - minYIndex)
                addProfilePoint(yIndex, xValue)

        for segment in allSegments:
            if debug:
                print 'segment', segment.description()
            if segment.isStraight():
                addSegmentSection(segment.startPoint(), segment.endPoint())
            else:
                segmentPoints = segment.evaluateRangeWithPrecision(AUTOKERN_SEGMENT_PRECISION)
                lastPoint = None
                for point in segmentPoints:
                    if lastPoint is not None:
                        addSegmentSection(lastPoint, point)
                    lastPoint = point

        return minProfile, maxProfile

    def isValidProfileIntrusion(self, profile0, profile1, referenceProfiles, advance):

#        DEBUG_h_n_ISSUE = True
#        print 'isValidProfileIntrusion', 'advance', advance

        maxRowExtrusion = self.max_distance
        maxSectionGapLength = int(round(self.max_distance * 1.0 / self.precision))
        maxSectionPadding = int(round(self.max_distance * 0.5 / self.precision))
        defaultMaxXOffset = maxRowExtrusion


        def isValidRow(x_offset):
            return (x_offset is not None) and (x_offset < maxRowExtrusion)

        '''
        Step 1

        Evaluate the x-offset between the profiles for each row.
        '''
        allXOffsets = []
        for index in xrange(len(profile0)):
            edge0 = profile0[index]
            edge1 = profile1[index]

            x_offset = None
            if (edge0 is not None) and (edge1 is not None):
                x_offset = advance + edge1 - edge0

            '''
            A row is hollow if it only exists because one of the profiles was inflated,
            ie. the top and bottom spacing around the glyph.
            '''
            hollow = False
            for referenceProfile in referenceProfiles:
                if referenceProfile[index] is None:
                    hollow = True
            if hollow and x_offset >= 0:
                '''
                If a row is hollow and there is no intrusion, ignore it
                so that it does not count towards extrusion.
                '''
                x_offset = None

            allXOffsets.append(x_offset)

#        if DEBUG_h_n_ISSUE:
#            print 'sections.0', len(sections), [len(section) for section in sections]
#            print 'sections.0', len(sections), sections

        def splitSection(section):
            '''
            Step 2

            We need to split sections that have large internal gaps.
            Consider C vs. O.  If the mouth of the C is too large,
            it cases the upper and lower arms of the C to be kerned too
            closely to the next glyph.

            To resolve this, we split sections with large continuous internal gaps.
            The gaps must be entirely deeper and longer than self.max_distance.

            We leave up to self.max_distance of the gap around the split which
            will be trimmed by the next phase anyhow.
            '''

            lastValidIndex = None
            for index, x_offset in enumerate(section):
#                print 'index, x_offset', index, x_offset
                if isValidRow(x_offset):
                    if lastValidIndex is not None:
                        gapLength = index - lastValidIndex
                        if gapLength >= maxSectionGapLength:
                            left = section[:index]
                            right = section[lastValidIndex + 1:]
#                            print 'maxGapLength', maxGapLength, 'gapLength', gapLength, 'self.max_distance', self.max_distance
#                            print 'left', left
#                            print 'right', right
                            return splitSection(left) + splitSection(right)

                    lastValidIndex = index

            return [section,]

#        print 'splitSections.0', len(sections)
        sections = splitSection(allXOffsets)
#        print 'splitSections.1', len(sections)


        def trimSection(section):
            '''
            Step 3

            We need to trim the sections that have huge gaps at the top and/or bottom.
            Consider h vs. h.  The huge space between the top stems distorts the
            profile and causes their bottoms to be kerned too closely.

            To resolve this, we trim large continuous gaps at the top or bottom
            of a section.  The gaps must be entirely greater than self.max_distance.

            We leave up to self.max_distance * 0.5 of the gap, so that beaks
            and arms are kerned closer.  For example, t vs. L or r vs. a.

            This isn't an ideal solution.  It might better to add a new argument that
            discards sections below a certain length.
            '''
            headCount = 0
            for index, x_offset in enumerate(section):
#                print 'index, x_offset', index, x_offset
                if isValidRow(x_offset):
                    break
                headCount = index
            tailCount = 0
            for index, x_offset in enumerate(reversed(section)):
#                print 'reversed index, x_offset', index, x_offset
                if isValidRow(x_offset):
                    break
                tailCount = index
#            maxPadding = int(round(self.max_distance * 0.5 / self.precision))
            headTrimCount = max(0, headCount - maxSectionPadding)
            tailTrimCount = max(0, tailCount - maxSectionPadding)
            if headTrimCount + tailTrimCount >= len(section):
                return []
#            print 'section', len(section)
#            print 'maxPadding', maxPadding, 'self.max_distance', self.max_distance, 'self.precision', self.precision
#            print 'headCount', headCount, 'headTrimCount', headTrimCount
#            print 'tailCount', tailCount, 'tailTrimCount', tailTrimCount
            if tailTrimCount > 0:
                result = section[headTrimCount:-tailTrimCount]
            else:
                result = section[headTrimCount:]

            # Trim empty space
            while (len(result) > 0) and (result[0] is None):
                result = result[1:]
            while (len(result) > 0) and (result[-1] is None):
                result = result[:-1]

            return result

        trimmedSections = []
        for section in sections:
            section = trimSection(section)
            if len(section) > 0:
                trimmedSections.append(section)
        sections = trimmedSections


        if DEBUG_h_n_ISSUE:
            print 'sections.1', len(sections), [len(section) for section in sections]
            print 'sections.1', len(sections), sections

#        print 'sections', sections

        if len(sections) < 1:
            '''
            No collision found.
            '''
            return True

        '''
        Step 4
        Now consider each section separately.
        '''
        for section in sections:
            intrusionTotal = 0
            extrusionTotal = 0

            for x_offset in section:
                if x_offset is None:
                    '''
                    Fill in missing gaps with maximum extrusion value.
                    '''
                    x_offset = defaultMaxXOffset
                rowIntrusion = max(0, -x_offset)
                '''
                Ignore extrusion greater than --max-distance argument.
                '''
                rowExtrusion = min(maxRowExtrusion, max(0, +x_offset))
#                print 'edge0, edge1', edge0, edge1, 'diff', diff, 'advance', advance, 'rowIntrusion', rowIntrusion, 'rowExtrusion', rowExtrusion
                intrusionTotal += rowIntrusion
                extrusionTotal += rowExtrusion

            '''
            Enforce
            '''

#            print 'advance', advance
#            print 'intrusionTotal', intrusionTotal, 'extrusionTotal', extrusionTotal
#            INTRUSION_EXTRUSION_MIN_RATIO = 1.5
            INTRUSION_EXTRUSION_MIN_RATIO = 1.0
            if intrusionTotal > extrusionTotal * INTRUSION_EXTRUSION_MIN_RATIO:
                return False

            intrusionToleranceArea = self.intrusion_tolerance * len(section)
#            print 'intrusionToleranceArea', intrusionToleranceArea
            if intrusionTotal > intrusionToleranceArea:
                return False

#        print 'totalSectionRowCount', totalSectionRowCount, 'advance', advance
#        print 'intrusionTotal', intrusionTotal, 'extrusionTotal', extrusionTotal, 'intrusionToleranceArea', intrusionToleranceArea

        return True


    def findMinProfileAdvance(self, profile0, profile1):
        if len(profile0) != len(profile1):
            raise Exception('profile heights do not match. %d != %d', len(profile0), len(profile1))

        contactAdvance = None
        for edge0, edge1 in itertools.izip(profile0, profile1):
            if edge0 is None or edge1 is None:
                continue
            diff = edge0 - edge1
            if contactAdvance is None:
                contactAdvance = diff
            else:
                contactAdvance = max(contactAdvance, diff)

        return contactAdvance


    def findMinProfileAdvance_withIntrusion(self, profile0, profile1, referenceProfiles):
        contactAdvance = self.findMinProfileAdvance(profile0, profile1)

        if contactAdvance is None:
            return None

        '''
        Binary search for best intrusion offset.
        '''
        lowValidIntrusionOffset = 0
        '''
        I'm not sure what the best way to determine an upper bound on this value is,
        so I've erred on the side of accuracy by chosing a very high upper bound.
        '''
        maximumIntrusionOffset = int(math.ceil(2.0 * max(self.intrusion_tolerance,
                                                         self.max_distance)))
        highInvalidIntrusionOffset = maximumIntrusionOffset
        while True:
            intrusionOffset = int(round((lowValidIntrusionOffset + highInvalidIntrusionOffset) / 2))
            if DEBUG_h_n_ISSUE:
                print 'intrusionOffset', intrusionOffset, 'lowValidIntrusionOffset', lowValidIntrusionOffset, 'highInvalidIntrusionOffset', highInvalidIntrusionOffset

            if intrusionOffset in ( lowValidIntrusionOffset,
                                    highInvalidIntrusionOffset, ):
                intrudingAdvance = contactAdvance - lowValidIntrusionOffset
                return intrudingAdvance

            if self.isValidProfileIntrusion(profile0, profile1, referenceProfiles, contactAdvance - intrusionOffset):
                lowValidIntrusionOffset = intrusionOffset
            else:
                highInvalidIntrusionOffset = intrusionOffset


    def inflateSegmentLeft(self, segment, hDistance, vDistance=None):
        '''
        '''
        if vDistance is None:
            vDistance = hDistance

        startTangent = segment.startTangent()
        endTangent = segment.endTangent()

        p0 = segment.startPoint()
        p1 = segment.endPoint()

        if len(segment) == 2:
            offset = scaleVectorHV(startTangent.rotate(math.pi * 0.5), hDistance, vDistance)
            p0 = p0.plus(offset)
            p1 = p1.plus(offset)
            newPoints = (p0, p1)
        elif len(segment) == 3:
            startOffset = scaleVectorHV(startTangent.rotate(math.pi * 0.5), hDistance, vDistance)
            endOffset = scaleVectorHV(endTangent.rotate(math.pi * 0.5), hDistance, vDistance)
            p0 = p0.plus(startOffset)
            p1 = p1.plus(endOffset)
            cp0 = TFSIntersection.intersectionWithTangents(p0, startTangent, p1, endTangent.invert())
            newPoints = (p0, cp0, p1)
        elif len(segment) == 4:
            startOffset = scaleVectorHV(startTangent.rotate(math.pi * 0.5), hDistance, vDistance)
            endOffset = scaleVectorHV(endTangent.rotate(math.pi * 0.5), hDistance, vDistance)
            oldScale = p0.distanceTo(p1)
            p0 = p0.plus(startOffset)
            p1 = p1.plus(endOffset)
            newScale = p0.distanceTo(p1)
            cp0 = p0.plus(segment.naiveStartVector().scale(newScale / oldScale))
            cp1 = p1.minus(segment.naiveEndVector().scale(newScale / oldScale))
            newPoints = (p0, cp0, cp1, p1)
        else:
            raise Exception('Invalid segment')

        try:
            result = TFSSegment(*newPoints).roundWithDefaultPrecision()

            '''
            Segments can be turned "inside out" when deflating.
            For example, deflating an arc by more than its "radius".
            We want to discard these segments.
            We can detect them by checking whether the naive endpoint tangent has reversed.
            '''
            affinity = result.naiveEndpointTangent().dotProduct(segment.naiveEndpointTangent())
            if affinity < 0:
                return None

            return result
        except TFSValidationException, e:
#            print e.message, e
            '''
            flating a segment can result in an empty or otherwise invalid segment.
            In fact, this will happen often since we'll be deflating previously
            inflated rounding curves.
            That's fine; ignore them.
            '''
            return None


    def makeInflatedProfile(self, contours, radius):

        segments = []

        def addEndpointRounding(point):
#            print
#            print 'addEndpointRounding', point.description(), 'radius', radius
            circle = TFSOval(point, hRadius=radius, vRadius=radius)
            segments.extend(circle.createPath().segments)

        for contour in contours:
            contour = orientClosedPathClockwise(contour)
            for segment in contour:
                addEndpointRounding(segment.startPoint())
                addEndpointRounding(segment.endPoint())
                inflatedSegment = self.inflateSegmentLeft(segment, radius)
                if inflatedSegment is not None:
                    segments.append(inflatedSegment)

        return self.makeProfile(segments=segments)


    def processKerningPair(self, ufoglyph0, ufoglyph1):
        '''
        returns True iff pair is kerned.
        '''

        self.timing.mark('processKerningPair.0.')
#        print 'processKerningPair', ufoglyph0.name, ufoglyph1.name

        if (ufoglyph0.name is None) or (ufoglyph1.name is None):
            return
        if self.pairsToKern is not None:
            if (ufoglyph0.name, ufoglyph1.name) not in self.pairsToKern:
                return False
        elif self.glyphsToKern is not None:
            if ufoglyph0.name not in self.glyphsToKern:
                return False
            if ufoglyph1.name not in self.glyphsToKern:
                return False

#        if self.isIgnoredGlyph(ufoglyph0) or self.isIgnoredGlyph(ufoglyph1):
#            return False

#        print 'processKerningPair'

        debugKerning = True
        debugKerning = False

        renderLog = (self.log_path is not None) and self.write_kerning_pair_logs

        contours0 = self.dstCache.getGlyphContours(ufoglyph0)
        contours1 = self.dstCache.getGlyphContours(ufoglyph1)
        if (not contours0) or (not contours1):
            return False

        self.timing.mark('processKerningPair.01')

        minmax0 = self.dstCache.getContoursMinmax(ufoglyph0)
        minmax1 = self.dstCache.getContoursMinmax(ufoglyph1)

        self.timing.mark('processKerningPair.010')

        def getGlyphProfiles(contours):
            return self.makeProfile(paths=contours)

        def maxAdvance(advance0, advance1, defaultAdvance):
            if advance0 is None and advance1 is None:
                result = defaultAdvance
            elif advance0 is None:
                result = advance1
            elif advance1 is None:
                result = advance0
            else:
                result = max(advance0, advance1)
            result = int(round(result))
            return result

        def getGlyphProfilesInflateMin(contours):
            return self.makeInflatedProfile(contours=contours, radius=self.min_distance * 0.5)
        def getGlyphProfilesInflateMax(contours):
            return self.makeInflatedProfile(contours=contours, radius=self.max_distance * 0.5)

        _, profile0 = self.dstCache.getCachedValue('getGlyphProfiles %s' % ufoglyph0.name, getGlyphProfiles, contours0)
        self.timing.mark('processKerningPair.011')

        _, profileMin0 = self.dstCache.getCachedValue('getGlyphProfilesInflateMin %s' % ufoglyph0.name, getGlyphProfilesInflateMin, contours0)
        self.timing.mark('processKerningPair.012')

        _, profileMax0 = self.dstCache.getCachedValue('getGlyphProfilesInflateMax %s' % ufoglyph0.name, getGlyphProfilesInflateMax, contours0)
        self.timing.mark('processKerningPair.013')

        profile1, _ = self.dstCache.getCachedValue('getGlyphProfiles %s' % ufoglyph1.name, getGlyphProfiles, contours1)
        self.timing.mark('processKerningPair.014')

        profileMin1, _ = self.dstCache.getCachedValue('getGlyphProfilesInflateMin %s' % ufoglyph1.name, getGlyphProfilesInflateMin, contours1)
        self.timing.mark('processKerningPair.015')

        profileMax1, _ = self.dstCache.getCachedValue('getGlyphProfilesInflateMax %s' % ufoglyph1.name, getGlyphProfilesInflateMax, contours1)
        self.timing.mark('processKerningPair.016')

        if DEBUG_h_n_ISSUE:
            print ufoglyph0.name, ufoglyph1.name, 'findMinProfileAdvance(profileMin0, profileMin1)'
        minDistanceAdvance = self.findMinProfileAdvance(profileMin0, profileMin1)
        if minDistanceAdvance is None:
            minDistanceAdvance = minmax0.maxX + self.min_distance - minmax1.minX
        minDistanceAdvance = int(round(minDistanceAdvance))
        self.timing.mark('processKerningPair.020')
        if debugKerning:
            print 'minDistanceAdvance', minDistanceAdvance

        if DEBUG_h_n_ISSUE:
            print ufoglyph0.name, ufoglyph1.name, 'findMinProfileAdvance_withIntrusion(profileMax0, profileMax1)'
        intrudingAdvance = self.findMinProfileAdvance_withIntrusion(profileMax0, profileMax1, referenceProfiles=(profile0, profile1))
        self.timing.mark('processKerningPair.022')
        if intrudingAdvance is None:
            intrudingAdvance = minmax0.maxX + self.min_distance - minmax1.minX
        intrudingAdvance = int(round(intrudingAdvance))
        if debugKerning:
            print 'intrudingAdvance', intrudingAdvance

        if DEBUG_h_n_ISSUE:
            print 'minDistanceAdvance', minDistanceAdvance
            print 'intrudingAdvance', intrudingAdvance

        '''
        Now combine results into the final advance value.
        1. Start with the "intruding advance."

        All subsequent steps should only serve to increase the advance.
        '''
        advance = intrudingAdvance

        '''
        2. Make sure advance is at least the "minimum advance."
        '''
        advance = maxAdvance(advance, minDistanceAdvance, minmax0.maxX + self.min_distance - minmax1.minX)

        '''
        3. Add the "tracking" value.
        '''
        advance += self.tracking

        '''
        4. Apply --x-extrema-overlap-scaling argument.
        '''
        x_extrema_overlap = minmax0.maxX - (minmax1.minX + advance)
        if x_extrema_overlap > 0:
            '''
            If x-extrema are overlapping, adjust advance accordingly.
            '''
            scaled_x_extrema_overlap = x_extrema_overlap * self.x_extrema_overlap_scaling
            advance += x_extrema_overlap - scaled_x_extrema_overlap

        '''
        5. Make sure the "x-extrema overlap" is not greater than the "max x-extrema overlap".
        '''
        x_extrema_overlap = minmax0.maxX - (minmax1.minX + advance)
        pair_max_x_extrema_overlap = self.getGlyphPairMaxXExtremaOverlap(ufoglyph0, ufoglyph1)

        if x_extrema_overlap > pair_max_x_extrema_overlap:
            advance += x_extrema_overlap - pair_max_x_extrema_overlap

        advance = int(round(advance))

        self.advanceMap[(ufoglyph0.name,
                         ufoglyph1.name,)] = advance

        if debugKerning:
            print '\t', ufoglyph0.unicode, ufoglyph1.unicode, advance

        self.timing.mark('processKerningPair.5')

        if renderLog:

            logSections = []

            def addLogSection(title,
                              glyphXAdvance0, glyphXAdvance1,
                              glyphContours0, glyphContours1,
                              glyphProfile0, glyphProfile1,
                              advanceValue,
                              extraVariableTuples=None,
                              comments=None):

                fillPathTuples = ()

                strokePathTuples = ()
                if glyphProfile0 is not None:
                    strokePathTuples = (
                    ( 0xafff7faf, glyphProfile0, ),
                    ( 0xafaf7fff, xTranslateContours(glyphProfile1, advanceValue), ),
                    )

                glyphMinmax0 = minmaxPaths(glyphContours0)
                glyphMinmax1 = minmaxPaths(glyphContours1)
                glyphContours1 = xTranslateContours(glyphContours1, advanceValue)
                glyphMinmax1_ = minmaxPaths(glyphContours1)

                avgGlyphWidth = ((glyphMinmax0.maxX - glyphMinmax0.minX) +
                                 (glyphMinmax1.maxX - glyphMinmax1.minX)) * 0.5
                fillAdvance = glyphMinmax1_.maxX + avgGlyphWidth / 3.0
                fillPathTuples += (
                                   ( 0x7f7faf7f, xTranslateContours(glyphContours0, fillAdvance,), ),
                                   ( 0x7f7f7faf, xTranslateContours(glyphContours1, fillAdvance,), ),
                                   )

                variableTuples = (
                                  ('%s (%s) lsb' % (ufoglyph0.name, formatUnicode(ufoglyph0.unicode),), (glyphMinmax0.minX), True,),
                                  ('%s (%s) rsb' % (ufoglyph0.name, formatUnicode(ufoglyph0.unicode),), (glyphXAdvance0 - glyphMinmax0.maxX), True,),
                                  ('%s (%s) right x-extrema' % (ufoglyph0.name, formatUnicode(ufoglyph0.unicode),), (glyphMinmax0.maxX), True,),
                                  ('%s (%s) x-advance' % (ufoglyph0.name, formatUnicode(ufoglyph0.unicode),), (glyphXAdvance0), True,),
                                  ('%s (%s) lsb' % (ufoglyph1.name, formatUnicode(ufoglyph1.unicode),), (glyphMinmax1.minX), True,),
                                  ('%s (%s) rsb' % (ufoglyph1.name, formatUnicode(ufoglyph1.unicode),), (glyphXAdvance1 - glyphMinmax1.maxX), True,),
                                  ('%s (%s) right x-extrema' % (ufoglyph0.name, formatUnicode(ufoglyph1.unicode),), (glyphMinmax1.maxX), True,),
#                                  ('%s x-advance' % (title,), self.formatUnitsInEms(glyphXAdvance0), True,),
                                  ('%s kerning value' % (title,), self.formatUnitsInEms(advanceValue - glyphXAdvance0), True,),
                                  ('%s kerned x-advance' % (title,), self.formatUnitsInEms(advanceValue), True,),
                                  )

                section_x_extrema_offset = glyphMinmax1_.minX - glyphMinmax0.maxX
                if section_x_extrema_offset >= 0:
                    variableTuples += ( (title + ' x-extrema offset', self.formatUnitsInEms(section_x_extrema_offset), True, ), )
                else:
                    variableTuples += ( (title + ' x-extrema overlap', self.formatUnitsInEms(-section_x_extrema_offset), True, ), )

                if extraVariableTuples:
                    variableTuples += extraVariableTuples

                hRanges = ( ( 'x-extrema overlap',
                              min(glyphMinmax0.maxX, glyphMinmax1_.minX),
                              max(glyphMinmax0.maxX, glyphMinmax1_.minX), ), )

                logSections.append({'title': title, # + ' Kerning',
                                    'svg': self.renderSvgScene(None,
                                                               pathTuples = (
                                                                             ( 0x7f7faf7f, glyphContours0, ),
                                                                             ( 0x7f7f7faf, glyphContours1, ),
                                                                             ),
                                                               fillPathTuples = fillPathTuples,
                                                               strokePathTuples = strokePathTuples,
                                                               hRanges = hRanges,
                                                               hGuidelines = ( advanceValue, # RSB
                                                                               glyphXAdvance0, # LSB
                                                                               min(glyphMinmax0.maxX, glyphMinmax1_.minX),
                                                                               max(glyphMinmax0.maxX, glyphMinmax1_.minX),
                                                                 ) ),
                                    'variables': variableTuples,
                                    'comments': comments,
                                    })


            srcufoglyph0 = self.srcUfoFont.getGlyphByName(ufoglyph0.name)
            if srcufoglyph0 is None:
                raise Exception('Could not find glyph by name: %s %s' % (str(ufoglyph0.name),
                                                                         str(ufoglyph0.unicode)))
            srcufoglyph1 = self.srcUfoFont.getGlyphByName(ufoglyph1.name)
            if srcufoglyph1 is None:
                raise Exception('Could not find glyph by name: %s %s' % (str(ufoglyph1.name),
                                                                         str(ufoglyph1.unicode)))

            srcContours0 = self.srcCache.getGlyphContours(srcufoglyph0)
            srcContours1 = self.srcCache.getGlyphContours(srcufoglyph1)
            srcKerning = self.dstUfoFont.getKerningPair(ufoglyph0.name, ufoglyph1.name)
            if srcKerning is None:
                srcKerning = 0
            srcAdvance = srcufoglyph0.xAdvance
            srcKernedAdvance = srcufoglyph0.xAdvance + srcKerning

            self.timing.mark('processKerningPair.60')

            def xTranslateContours(contours, value):
                return [contour.applyPlus(TFSPoint(value, 0)) for contour in contours]

            addLogSection('Original',
                          srcufoglyph0.xAdvance, srcufoglyph1.xAdvance,
                          srcContours0, srcContours1,
                          None, None,
                          srcKernedAdvance,
                          comments=('The original kerning from the input.',))

            self.timing.mark('processKerningPair.61')

            # -----------

            profilePaths0 = self.convertProfileToLogPaths(profile0, isLeft=True)
            profileMinPaths0 = self.convertProfileToLogPaths(profileMin0, isLeft=True)
            profileMaxPaths0 = self.convertProfileToLogPaths(profileMax0, isLeft=True)
            profilePaths1 = self.convertProfileToLogPaths(profile1, isLeft=False)
            profileMinPaths1 = self.convertProfileToLogPaths(profileMin1, isLeft=False)
            profileMaxPaths1 = self.convertProfileToLogPaths(profileMax1, isLeft=False)

            self.timing.mark('processKerningPair.62')

            # -----------

            contactAdvance = self.findMinProfileAdvance(profile0, profile1)
            if contactAdvance is None:
                contactAdvance = minmax0.maxX - minmax1.minX
            contactAdvance = int(round(contactAdvance))

            self.timing.mark('processKerningPair.63')

            addLogSection('Contact',
                          ufoglyph0.xAdvance, ufoglyph1.xAdvance,
                          contours0, contours1,
                          profilePaths0, profilePaths1,
                          contactAdvance,
                          comments=('The raw contours brought into contact if possible.',
                                    'From each glyph, a facade profile is constructed from its contours.',))

            self.timing.mark('processKerningPair.64')

            # -----------

            addLogSection('Minimum Distance',
                          ufoglyph0.xAdvance, ufoglyph1.xAdvance,
                          contours0, contours1,
                          profileMinPaths0, profileMinPaths1,
                          minDistanceAdvance,
                          (
                              ('--min-distance-ems', 'min_distance_ems',),
                          ),
                          comments=('The minimum distance kerning.',
                                    'From each glyph, a facade profile is constructed from its contours (inflated by half of --min-distance-ems).',))

            self.timing.mark('processKerningPair.65')

            # -----------

            maxDistanceAdvance = self.findMinProfileAdvance(profileMax0, profileMax1)
            if debugKerning:
                print 'maxDistanceAdvance', maxDistanceAdvance

            if maxDistanceAdvance is None:
                '''
                If no collisions between the glyph profiles, use x-extrema
                plus the max_distance argument.
                '''
                maxDistanceAdvance = minmax0.maxX + self.max_distance - minmax1.minX
            maxDistanceAdvance = int(round(maxDistanceAdvance))

            self.timing.mark('processKerningPair.66')

            addLogSection('Maximum Distance',
                          ufoglyph0.xAdvance, ufoglyph1.xAdvance,
                          contours0, contours1,
                          profileMaxPaths0, profileMaxPaths1,
                          maxDistanceAdvance,
                          (
                              ('--max-distance-ems', 'max_distance_ems',),
                          ),
                          comments=('The maximum distance kerning.',
                                    'From each glyph, a facade profile is constructed from its contours (inflated by half of --max-distance-ems).',))
            self.timing.mark('processKerningPair.67')

            # -----------

            addLogSection('Intruding',
                          ufoglyph0.xAdvance, ufoglyph1.xAdvance,
                          contours0, contours1,
                          profileMaxPaths0, profileMaxPaths1,
                          intrudingAdvance,
                          (
#                              ('intrudingAdvance', 'intrudingAdvance_in_ems',),
#                              ('intrudingAdvance (Right)', 'intrudingAdvance0_in_ems',),
#                              ('intrudingAdvance (Left)', 'intrudingAdvance1_in_ems',),
                              ('--intrusion-tolerance-ems', 'intrusion_tolerance_ems',),
                          ),
                          comments=('The intrusion kerning.',
                                    'From each glyph, a facade profile is constructed from its contours (inflated by half of --max-distance-ems).',
                                    'The profiles are then drawn towards each other using the intrusion algorithm.'))
            self.timing.mark('processKerningPair.68')

            # -----------

            addLogSection('Autokern Raw',
                          ufoglyph0.xAdvance, ufoglyph1.xAdvance,
                          contours0, contours1,
                          profileMaxPaths0, profileMaxPaths1,
                          advance,
                          (
                              ('--max-x-extrema-overlap-ems', 'max_x_extrema_overlap_in_ems',),
                              ('--x-extrema-overlap-scaling', 'x_extrema_overlap_scaling',),
                          ),
                          comments=('The raw kerning.',
                                    'The results of the previous steps are combined, and the effects of various arguments are applied.',
                                    'Does not represent the final output which is effected by changes to the side bearings.',))

            self.timing.mark('processKerningPair.69')

            # -----------

            pageTitle0 = u'Autokern Log:'
            pageTitle1 = u'%s vs. %s' % ( formatGlyphName(ufoglyph0),
                                                         formatGlyphName(ufoglyph1), )

            def formatEmScalar(value):
                return formatEms(value / float(self.units_per_em))

            def formatGlyphMap(glyph, glyphMinmax):
                return {
                           'glyphName': formatGlyphName(glyph),
                           'minX': formatEmScalar(glyphMinmax.minX),
                           'maxX': formatEmScalar(glyphMinmax.maxX),
                           'minY': formatEmScalar(glyphMinmax.minY),
                           'maxY': formatEmScalar(glyphMinmax.maxY),
                        }

            x_extrema_overlap = minmax0.maxX - (minmax1.minX + advance)

            localsMap = {}
            localsMap.update(locals())

            mustacheMap = self.makeDefaultMustacheMap(localsMap=localsMap)
            self.addSidebarMustacheMap(mustacheMap, kerned=False)

            logSectionMaps = []
            for logSection in logSections:
                logSectionMap = {}
                logSectionMap['sectionTitle'] = logSection['title']
                logSectionMap['sectionSvg'] = logSection['svg']
                if logSection['comments']:
                    logSectionMap['sectionComments'] = [{'comment': comment,} for comment in logSection['comments']]
                def formatSectionVariable(variableTuple):
                    if len(variableTuple) == 2:
                        name, var = variableTuple
                        return {'varName': name, 'varValue':mustacheMap[var],}
                    else:
                        return {'varName': variableTuple[0], 'varValue':variableTuple[1],}

                logSectionMap['sectionVariables'] = [formatSectionVariable(variableTuple) for variableTuple in logSection['variables']]
                logSectionMaps.append(logSectionMap)

            mustacheMap.update({
                           'pageTitle0': pageTitle0,
                           'pageTitle1': pageTitle1,
                           'logSectionMaps': logSectionMaps,
                           })

            logFilename = self.getKerningPairHtmlFilename(ufoglyph0, ufoglyph1)
            self.kerningPairLogFilenames.add(logFilename)
            self.writeLogFile('autokern_pair_template.txt',
                              logFilename,
                              'Kerning Pairs',
                              '''
    Logs that document the kerning process for each glyph pair kerned by Autokern.
                              ''',
                              ('%s vs. %s' % (ufoglyph0.name, ufoglyph1.name,)),
                              mustacheMap)

        self.timing.mark('processKerningPair.9')

        return True


    def processAllKerningPairs(self):

        print
        print 'Processing kerning pairs...'

        if USE_CACHED_KERNING_MAP:
            import tfs.common.TFSProject as TFSProject
            tmpFolder = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'tmp'))
            advanceMapYamlFile = os.path.abspath(os.path.join(tmpFolder, 'advanceMap.yaml'))
            if os.path.exists(advanceMapYamlFile):
                with open(advanceMapYamlFile, 'rt') as f:
                    yamldata = f.read()
                    self.advanceMap = yaml.load(yamldata)
                    return

        glyphs = self.dstUfoFont.getGlyphs()
        total = len(glyphs) * len(glyphs)
        count = 0
        startTime = time.time()
        lastLog = None
        firstKernedName = None
        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.unicode, glyph1.unicode))
        for ufoglyph0 in glyphs:
            if ufoglyph0.name in self.ignoredGlyphNames:
                count += len(glyphs)
                continue

            for ufoglyph1 in glyphs:
                if ufoglyph1.name in self.ignoredGlyphNames:
                    count += 1
                    continue

                pairKerned = self.processKerningPair(ufoglyph0, ufoglyph1)

                count += 1

                if not pairKerned:
                    continue

                if firstKernedName is None:
                    firstKernedName = ufoglyph0.name
#                    print
                    continue
                elif firstKernedName == ufoglyph0.name:
                    '''
                    Do not log until we have completed a first successful pass.
                    '''
                    if count % 10 == 0:
                        print '.',
                    continue

                now = time.time()
                if (lastLog is not None) and (now - lastLog < 3.0):
                    '''
                    Do not log more than once per second.
                    '''
                    continue
                if lastLog is None:
                    print
                lastLog = now

                elapsedTime = time.time() - startTime
#                    print 'elapsedTime', elapsedTime, 'total', total
                averageTime = elapsedTime / float(count)
#                    print 'averageTime', averageTime
                totalTime = averageTime * total
                remainingTime = totalTime - elapsedTime

                remaining = '%s remaining' % ( formatTimeDuration(remainingTime), )

                def formatUnicode(value):
                    if value is None:
                        return 'None'
                    else:
                        return '0x%X' % ( value, )
#                print 'ufoglyph0', ufoglyph0.unicode, ufoglyph0.name, 'ufoglyph1', ufoglyph1.unicode, ufoglyph1.name
                print '\t', '%s %s vs. %s %s (%0.2f%%)' % ( ufoglyph0.name,
                                                      formatUnicode(ufoglyph0.unicode),
                                                      ufoglyph1.name,
                                                      formatUnicode(ufoglyph1.unicode),
                                                      100 * count / float(total),), '\t', remaining

#        print
#        print 'self.advanceMap =', repr(self.advanceMap)
        print

        if USE_CACHED_KERNING_MAP:
            yamldata = yaml.dump(self.advanceMap)
            import tfs.common.TFSProject as TFSProject
            tmpFolder = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'tmp'))
            if not os.path.exists(tmpFolder):
                os.mkdir(tmpFolder)
            advanceMapYamlFile = os.path.abspath(os.path.join(tmpFolder, 'advanceMap.yaml'))
            with open(advanceMapYamlFile, 'wt') as f:
                f.write(yamldata)


    def parseCodePoint(self, argName, glyphNames, value):
        '''
        Parses a glyph value in one of three forms and returns to glyph's name.
        1. Glyph name in font, ie. A = A.
        2. Hexidecimal, ie. 0x41 = A.
        3. Decimal, ie. 65 = A.
        '''
        if value in glyphNames:
            return value

        if value.startswith('0x'):
            try:
                codePoint = int(value, 16)
            except ValueError, e:
                raise Exception('Invalid hexidecimal value in %s: %s' % (argName, value,) )
        else:
            try:
                codePoint = int(value)
            except ValueError, e:
                raise Exception('Invalid value in %s: %s' % (argName, value,) )

        try:
#            print 'codePoint', codePoint
            name = UnicodeCharacterNames.getUnicodeCharacterName(codePoint)
            return name
        except ValueError, e:
            raise Exception('Unknown value in %s: %s' % (argName, value,) )


    def updateKerning(self):
        print 'Updating kerning...'
        self.dstUfoFont.clearKerning()

        glyphs = self.dstUfoFont.getGlyphs()
        glyphWidthMap = {}
        for ufoglyph in glyphs:
            if ufoglyph.name is None:
                continue
            glyphWidthMap[ufoglyph.name] = ufoglyph.xAdvance

        kerningTuples = []
        for key in self.advanceMap:
            advance = self.advanceMap[key]
            name0, name1 = key
            kerningValue = advance - glyphWidthMap[name0]

#            if key in (
#                       ('j', 'o',),
#                        ):
#                print 'updateKerning', key, kerningValue

            if abs(kerningValue) < self.kerning_threshold:
                continue
            kerningTuples.append( ( name0, name1, kerningValue, ) )

        def cmpKerningTuples(value0, value1):
            return cmp(abs(value0[-1]), abs(value1[-1]))
        kerningTuples.sort(cmpKerningTuples, reverse=True)

#        print 'kerningTuples', kerningTuples[0]
#        print 'kerningTuples[-1]', kerningTuples[-1]

        self.kerned_pairs_count = len(self.advanceMap)
        self.valid_kerned_pairs_count = len(kerningTuples)

#        for i in xrange(len(kerningTuples) / 1000):
#            index = i * 1000
#            print 'kerningTuples[%d]' % index, kerningTuples[index]

        if self.max_kerning_pairs:
            self.max_kerning_pairs = max(0, self.max_kerning_pairs)
            kerningTuples = kerningTuples[:self.max_kerning_pairs]

        self.final_kerned_pairs_count = len(kerningTuples)

        for name0, name1, kerningValue in kerningTuples:
#            if (name0, name1) in (
#                       ('j', 'o',),
#                        ):
#                print 'updateKerning.1', key, kerningValue

            self.dstUfoFont.setKerningPair(name0, name1, kerningValue)


    def clearSideBearings(self):

        if self.pairsToKern is not None:
            return
        if self.glyphsToKern is not None:
            return

        '''
        Removes the left and right side bearings from the glyph.
        '''
        glyphs = self.dstUfoFont.getGlyphs()
        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.unicode, glyph1.unicode))
        for ufoglyph in glyphs:
            if self.glyphsToKern is not None:
                if ufoglyph.name not in self.glyphsToKern:
                    continue
#            elif self.isIgnoredGlyph(ufoglyph):
#                '''
#                TODO: Should we normalize the side bearings of these glyphs to perhaps half of max_distance?
#                '''
#                continue

            contours = self.dstCache.getGlyphContours(ufoglyph)
#            contours = ufoglyph.getContours()
            if len(contours) == 0:
                '''
                Do not modify width of space and other empty glyphs.
                '''
                continue
            minmax = minmaxPaths(contours)

            if ufoglyph.name in self.ignoredGlyphNames:
                '''
                TODO: Should we normalize the side bearings of these glyphs to perhaps half of max_distance?
                '''
#                defaultSideBearing = self.max_distance * 0.5
#                contours = [contour.applyPlus(TFSPoint(defaultSideBearing + -minmax.minX, 0)) for contour in contours]
#                ufoglyph.setContours(contours, correctDirection=False)
#                ufoglyph.setXAdvance(2 * defaultSideBearing + minmax.maxX - minmax.minX)
                continue

            contours = [contour.applyPlus(TFSPoint(-minmax.minX, 0)) for contour in contours]
            ufoglyph.setContours(contours, correctDirection=False)
            ufoglyph.setXAdvance(minmax.maxX - minmax.minX)

        # Clear the dst cache.
        self.dstCache = AutokernCache()


    def updateSideBearings(self):
        '''
        Rewrite the left and right side bearings of every glyph to be half of the average spacing
        with other glyphs.
        '''

        if self.pairsToKern is not None:
            return
        if self.glyphsToKern is not None:
            return

        print 'Updating side-bearings...'

        modifiedAdvanceMap = {}
        modifiedAdvanceMap.update(self.advanceMap)

        '''
        Removes the left and right side bearings from the glyph.
        '''
        glyphs = self.dstUfoFont.getGlyphs()
        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.unicode, glyph1.unicode))

        glyphWidthMap = {}
        for ufoglyph in glyphs:
            if ufoglyph.name is None:
                continue
            glyphWidthMap[ufoglyph.name] = ufoglyph.xAdvance

        #

        leftKeyMap = {}
        rightKeyMap = {}
        for key in self.advanceMap:
            advance = self.advanceMap[key]
            name0, name1 = key
            spacing = advance - glyphWidthMap[name0]

            leftKeyList = leftKeyMap.get(name1, [])
            leftKeyList.append( ( key, advance, spacing, ) )
            leftKeyMap[name1] = leftKeyList

            rightKeyList = rightKeyMap.get(name0, [])
            rightKeyList.append( ( key, advance, spacing, ) )
            rightKeyMap[name0] = rightKeyList

        #

        if USE_CACHED_KERNING_MAP:
            for ufoglyph in glyphs:
                contours = self.dstCache.getGlyphContours(ufoglyph)
#            print

#        for key in self.advanceMap:
#            if key in (
#                       ('j', 'o',),
##                       ('N','N',),
##                       ('A','A',),
##                        ('A','F',),
#                        ):
#                print 'self.advanceMap', key, self.advanceMap[key]

        for ufoglyph in glyphs:
            if self.glyphsToKern is not None:
                if ufoglyph.name not in self.glyphsToKern:
                    continue
            elif ufoglyph.name in self.ignoredGlyphNames:
                continue

            contours = self.dstCache.getGlyphContours(ufoglyph)

            if len(contours) == 0:
                '''
                Do not modify width of space and other empty glyphs.
                '''
                continue

            rightSpacings = []
            rightKeys = []
            leftSpacings = []
            leftKeys = []

            for key, advance, spacing in leftKeyMap[ufoglyph.name]:
                leftSpacings.append(spacing)
                leftKeys.append(key)
            for key, advance, spacing in rightKeyMap[ufoglyph.name]:
                rightSpacings.append(spacing)
                rightKeys.append(key)

            '''
            Default sidebearings to half of the "max distance" parameter.
            '''
            leftSideBearing = rightSideBearing = 0.5 * self.max_distance_ems * self.units_per_em
            '''
            If we have kerning values for left or right side, use half of the average as the side bearing.
            '''
            if len(rightSpacings) > 0:
                rightSideBearing = 0.5 * reduce(float.__add__, [float(value) for value in rightSpacings]) / len(rightSpacings)
            if len(leftSpacings) > 0:
                leftSideBearing = 0.5 * reduce(float.__add__, [float(value) for value in leftSpacings]) / len(leftSpacings)

            '''
            Use round numbers
            '''
            rightSideBearing = int(round(rightSideBearing))
            leftSideBearing = int(round(leftSideBearing))
            if self.allow_negative_side_bearings:
                '''
                Check that the side bearings are not "negative", ie. do not
                intrude within the glyph bounds.
                '''
                leftSideBearing = max(0, leftSideBearing)
                rightSideBearing = max(0, rightSideBearing)

#            if ufoglyph.name in (
#                       'j', 'o',
##                                 'N',
##                                  'A',
##                                  'F',
#                                   ):
#                print
#                print 'ufoglyph.name', ufoglyph.name
#                print 'glyphWidthMap[]', glyphWidthMap[ufoglyph.name]
#                print 'ufoglyph.xAdvance', ufoglyph.xAdvance
#                print 'leftKeys', len(leftKeys), leftKeys
#                print 'rightKeys', len(rightKeys), rightKeys
#                print 'rightSpacings', len(rightSpacings), rightSpacings
#                print 'leftSpacings', len(leftSpacings), leftSpacings
#                print 'updateSideBearings', 'leftSideBearing', leftSideBearing, 'rightSideBearing', rightSideBearing, 'ufoglyph.xAdvance', ufoglyph.xAdvance

            '''
            Apply the LSB to the contours.
            '''
            contours = [contour.applyPlus(TFSPoint(+leftSideBearing, 0)) for contour in contours]
            ufoglyph.setContours(contours, correctDirection=False)
            '''
            Update the glyph x advance to reflect the LSB and RSB.
            '''
            ufoglyph.setXAdvance(ufoglyph.xAdvance + leftSideBearing + rightSideBearing)

#            if ufoglyph.name in (
#                       'j', 'o',
##                                 'N',
##                                  'A',
##                                  'F',
#                                   ):
#                print 'updateSideBearings.1', 'leftSideBearing', leftSideBearing, 'rightSideBearing', rightSideBearing, 'ufoglyph.xAdvance', ufoglyph.xAdvance

            '''
            Lastly, update the kerning values in the advance map.

            The LSBs effect the advance maps, but the RSBs don't, because the
            advance map represents the kerned advance, not the kerning value itself.
            '''
            for key in leftKeys:
                modifiedAdvanceMap[key] = modifiedAdvanceMap[key] - leftSideBearing
            for key in rightKeys:
#                modifiedAdvanceMap[key] = modifiedAdvanceMap[key] + leftSideBearing - rightSideBearing
                modifiedAdvanceMap[key] = modifiedAdvanceMap[key] + leftSideBearing


#        for key in self.advanceMap:
#            if key in (
#                       ('j', 'o',),
##                       ('N','N',),
##                       ('A','A',),
##                        ('A','F',),
#                        ):
#                print 'self.advanceMap', key, self.advanceMap[key]
#        for key in modifiedAdvanceMap:
#            if key in (
#                       ('j', 'o',),
##                       ('N','N',),
##                       ('A','A',),
##                        ('A','F',),
#                        ):
#                print 'modifiedAdvanceMap', key, modifiedAdvanceMap[key]

        '''
        Replace the advance map.
        '''
        self.advanceMap = modifiedAdvanceMap

        # Clear the dst cache.
        self.dstCache = AutokernCache()


    def assessKerningPair(self, ufoglyph0, ufoglyph1):

        contours0 = self.dstCache.getGlyphContours(ufoglyph0)
        contours1 = self.dstCache.getGlyphContours(ufoglyph1)

        if (not contours0) or (not contours1):
            return None

        kerning = self.dstUfoFont.getKerningPair(ufoglyph0.name, ufoglyph1.name)
        if kerning is None:
            kerning = 0
        advance = ufoglyph0.xAdvance + kerning

        profile0 = self.makeProfile(func=max, paths=contours0)
        profile1 = self.makeProfile(func=min, paths=contours1)

        def convertToPixelUnits(value):
            return int(math.ceil(value / float(self.precision)))

        '''
        Find the closest pair of pixels.
        '''
        minDistanceSqrd = None
        for y0, x0 in enumerate(profile0):
            for y1, x1 in enumerate(profile1):
                if x0 is None or x1 is None:
                    continue
                diffX = x0 - (x1 + advance / float(self.precision))
                diffY = y0 - y1
                distanceSqrd = (diffX * diffX) + (diffY * diffY)
                if (minDistanceSqrd is None) or (distanceSqrd < minDistanceSqrd):
                    minDistanceSqrd = distanceSqrd

        if minDistanceSqrd is None:
            return None
        else:
            minDistance = math.sqrt(float(minDistanceSqrd))
            return minDistance * self.precision


    def assessKerning(self):

        glyphs = self.dstUfoFont.getGlyphs()
#        glyphNameMap = {}
#        for ufoglyph in glyphs:
#            glyphNameMap[ufoglyph.name] = ufoglyph
        unicodeGlyphMap = {}
        for ufoglyph in glyphs:
            if ufoglyph.unicode:
                unicodeGlyphMap[ufoglyph.unicode] = ufoglyph


        pairGroups = (
                      ( min, 'Minimum Distance Pairs',
                         ( ('A', 'A'),
                           ('T', 'T'),
                           ('A', 'V'),
                           ('M', 'M'),
                           ('W', 'W'),
                           ('V', 'V'),
                           ('L', 'L'),
                           ('L', 'J'),
                           ('Y', 'Y'),
                           ('W', 'A'),
                           ('V', 'A'),
                           ('A', 'V'),
                           ('A', 'W'),
                           ),
                         ),
                      ( max, 'Maximum Distance Pairs',
                         ( ('J', 'L'),
                           ('H', 'H'),
                           ('H', 'L'),
                           ('J', 'H'),
                           ('H', 'F'),
                           ('V', 'V'),
                           ('I', 'I'),
                           ('N', 'F'),
                           ('N', 'B'),
                           ('N', 'H'),
                           ('N', 'L'),
                           ('H', 'B'),
                           ('W', 'A'),
                           ('V', 'A'),
                           ('A', 'V'),
                           ('A', 'W'),
                           ),
                         ),
                      )

        def formatEmScalar(value):
            return formatEms(value / float(self.units_per_em))

        for reduceFunc, pairGroupName, pairs in pairGroups:
            print
            print pairGroupName
            values = []
            for char0, char1 in pairs:
                unicode0 = ord(char0)
                unicode1 = ord(char1)
#                print 'pair', char0, char1, unicode0, unicode1
                ufoglyph0 = unicodeGlyphMap[unicode0]
                ufoglyph1 = unicodeGlyphMap[unicode1]
                pairDistance = self.assessKerningPair(ufoglyph0, ufoglyph1)
                print 'pair', char0, hex(unicode0), 'vs.', char1, hex(unicode1), 'pairDistance:', pairDistance, ('(%s)' % ( formatEmScalar(pairDistance), ) )
                values.append(pairDistance)
            print pairGroupName, formatEmScalar(reduce(reduceFunc, values))
        print


    def convertTextToContours(self, text, ufoFont, cache, lastKerningValues=None):
        outsideContours = []
        insideContours = []
        labels = []
        kerningValues = []
        xOffset = 0
        lastUfoGlyph = None
        lastMinmax = None
        for index, textGlyph in enumerate(text):
            codePoint = ord(textGlyph)
            ufoglyph = ufoFont.getGlyphByCodePoint(codePoint)
            if ufoglyph is None:
                print 'Unknown glyph in sample text: %s %s' % (textGlyph, formatUnicode(codePoint),)
                return None
#                if len(contours) < 1:
#                    continue

            contours = cache.getGlyphContours(ufoglyph)
#            contours = ufoglyph.getContours(warnings=False)
#                contours = self.getGlyphContours(ufoglyph)

            '''
            We use robofab's correctDirection() method to correctly orient the
            inside and outside contours in truetype orientation.

            We don't want to effect the output, so we do this in a temporary font.
            '''
            tempUfoFont = robofab.world.NewFont(familyName='ignore', styleName='ignore')
            tempUfoGlyph = tempUfoFont.newGlyph('ignore')
            tempTFSGlyph = TFSGlyph(tempUfoGlyph)
            tempTFSGlyph.setContours(contours, correctDirection=True)
            contours = tempTFSGlyph.getContours(warnings=False)

            kerningValue = None
            if lastUfoGlyph is None:
                minmax = minmaxPaths(contours)
                xOffset = -minmax.minX
            else:
#                if lastUfoGlyph is not None:
                kerningValue = ufoFont.getKerningPair(lastUfoGlyph.name, ufoglyph.name, )
                if kerningValue is not None:
                    xOffset += kerningValue
                else:
                    kerningValue = 0

#            print
#            print 'xOffset', xOffset
#            print 'ufoglyph.name', ufoglyph.name
#            print 'ufoglyph.xAdvance', ufoglyph.xAdvance
#            print 'kerningValue', kerningValue
#            minmax = minmaxPaths(contours)
#            print 'minmax.raw', minmax

            contours = [contour.applyPlus(TFSPoint(xOffset, 0)) for contour in contours]
            minmax = minmaxPaths(contours)

#            print 'minmax', minmax

            if kerningValue is not None:
                xExtremaOverlap = minmax.minX - lastMinmax.maxX
#                print 'lastMinmax', lastMinmax
#                print 'xExtremaOverlap', xExtremaOverlap
#                    text = '%0.0f/%s%0.0f' % (
#                                                 float(kerningValue),
#                                                 '+' if xExtremaOverlap > 0 else '-',
#                                                 float(abs(xExtremaOverlap)),
#                                                 )
                text = '%d' % ( int(xExtremaOverlap), )

                KERNING_LABEL_COLOR = 0xdf000000
                if lastKerningValues is not None:
                    lastXExtremaOverlap = lastKerningValues[index - 1]
                    xExtremaOverlapDelta = xExtremaOverlap - lastXExtremaOverlap

#                    print 'index', index
#                    print 'lastXExtremaOverlap', lastXExtremaOverlap
#                    print 'xExtremaOverlapDelta', xExtremaOverlapDelta

                    KERNING_HIGHLIGHT_LOW_THRESHOLD = 10
                    KERNING_HIGHLIGHT_HIGH_THRESHOLD = 20
                    if abs(xExtremaOverlapDelta) >= KERNING_HIGHLIGHT_HIGH_THRESHOLD:
                        KERNING_LABEL_COLOR = 0xdfa70000
                    elif abs(xExtremaOverlapDelta) >= KERNING_HIGHLIGHT_LOW_THRESHOLD:
                        KERNING_LABEL_COLOR = 0xdf530000

                    text += ' (%s%0.0f)' % (
                                           '' if xExtremaOverlapDelta == 0 else ('+' if xExtremaOverlapDelta > 0 else '-'),
                                           float(abs(xExtremaOverlapDelta)),
                                           )


                label = TFSMap()
                label.text = text
#                # Subtract half of the kerning value to center on the ker
#                labelX = xOffset - kerningValue * 0.5
#                labelX = xOffset
                # Center label between the x-extrema of the two glyphs.
                labelX = (minmax.minX + lastMinmax.maxX) * 0.5
                label.origin = TFSPoint(labelX, -abs(self.descender * 1.1))
                label.fillColor = KERNING_LABEL_COLOR
                label.params = {
                                       'text-anchor': 'middle',
                                       'dominant-baseline': 'text-before-edge',
                                       'font-family': "Lato, Helvetica, Arial, sans-serif;",
#                                           'font-size': "14px",
#                                           'font-weight': "bold",
                                       }
                labels.append(label)
                kerningValues.append( xExtremaOverlap )

            for contour in contours:
                if isClosedPathClockwise(contour):
                    outsideContours.append(contour)
                else:
                    insideContours.append(contour)

            xOffset += ufoglyph.xAdvance
            lastMinmax = minmax
            lastUfoGlyph = ufoglyph

        return outsideContours, insideContours, labels, kerningValues


    def renderTextWithFont(self, text, ufoFont, cache, source, fillColor, lastKerningValues=None):
        converted = self.convertTextToContours(text, ufoFont, cache, lastKerningValues=lastKerningValues)
        if converted is None:
            return {'errorMap': {'text': text,
                                 'source': source,
                                 'message': 'error'},
                    }, None
        else:
            outsideContours, insideContours, labels, kerningValues = converted

            sampleSvg = self.renderSvgScene(None,
                                            fillPathTuples = ( ( fillColor, outsideContours, ),
                                                               ( 0xffffffff, insideContours, ),
                                                               ),
                                            textTuples = labels,
                                            padding=(0,0,20,0),
#                                            maxWidth = 800,
#                                            maxHeight = 300,
                                            maxWidth = 700,
                                            maxHeight = 250,
                                            )
            return {'renderMap': {'text': text,
                   'source': source,
                   'svg': sampleSvg},
                   }, kerningValues


    def writeSamples(self):

        renderLog = self.log_path is not None
        if not renderLog:
            return
        print 'Writing samples...'

        sampleTextsMaps = []
        for sampleText in self.sampleTexts:
            sampleTextMap, kerningValues = self.renderTextWithFont(sampleText, self.srcUfoFont, self.srcCache, 'Original', 0x7f7f7faf)
            sampleTextsMaps.append(sampleTextMap)
            sampleTextMap, _ = self.renderTextWithFont(sampleText, self.dstUfoFont, self.dstCache, 'Autokern', 0x7f7faf7f,
                                                       lastKerningValues=kerningValues)
            sampleTextsMaps.append(sampleTextMap)


        pageTitle = u'Autokern Sample Texts'

        mustacheMap = self.makeDefaultMustacheMap(localsMap=locals())
        self.addSidebarMustacheMap(mustacheMap, kerned=True)
        mustacheMap.update({
                   'pageTitle': pageTitle,
                   'sampleTextsMaps': sampleTextsMaps,
                   })

        self.writeLogFile('autokern_samples_template.txt',
                          'sample_texts.html',
                          'Sample Texts',
                              '''
    Side-by-side comparisons of short texts using the original kerning and Autokern's kerning.
                              ''',
                          'Sample Texts',
                          mustacheMap)


    def writeLogIndex(self):

        renderLog = self.log_path is not None
        if not renderLog:
            return
        print 'Writing log index...'

        groupDescriptionMap = {}
        groupNames = []
        groupItemsMap = {}
        for groupName, groupDescription, filename, logShortname in self.logFileTuples:
            groupDescriptionMap[groupName] = groupDescription
            groupItemsMap[groupName] = groupItemsMap.get(groupName, []) + [(filename, logShortname,)]
            if groupName not in groupNames:
                groupNames.append(groupName)

        logGroupMaps = []
        for groupName in groupNames:
            logGroupItems = []
            for filename, logShortname in groupItemsMap[groupName]:
                logGroupItems.append({'groupName': groupName,
                                      'filename': filename,
                                      'logShortname': logShortname,
                                      })
            groupSuffix = ''
            if len(logGroupItems) > 100:
                logGroupItems = logGroupItems[:100]
                groupSuffix = '...'
            logGroupMaps.append({'logGroupName': groupName,
                                 'logGroupDescription': groupDescriptionMap[groupName],
                                 'logGroupItems': logGroupItems,
                                 'groupSuffix': groupSuffix,
                                 })


        pageTitle = u'Autokern Results'

        mustacheMap = self.makeDefaultMustacheMap(localsMap=locals())
        self.addSidebarMustacheMap(mustacheMap, kerned=True, complete=True)
        mustacheMap.update({
                   'pageTitle': pageTitle,
                   'logGroupMaps': logGroupMaps,
                   })

        self.writeLogFile('autokern_index_template.txt',
                          'index.html',
                          None,
                          None,
                          None,
                          mustacheMap)


    def writeLogFile(self,
                     templateFilename, logFilename,
                     groupName, groupDescription,
                     logShortname, mustacheMap):

        import tfs.common.TFSProject as TFSProject
#        dataFolder = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data'))
        mustache_template_file = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', templateFilename))
        with open(mustache_template_file, 'rt') as f:
            mustache_template = f.read()

        import pystache

#        class CustomMustacheRenderer(pystache.renderer.Renderer):
#
#            def __init__(self):
#                pystache.renderer.Renderer.__init__(self, search_dirs=[dataFolder,])
#
#            def load_template(self, template_name):
#                print 'load_template', template_name
#                return pystache.renderer.Renderer.load_template(self, template_name)
#
#
#        renderer = CustomMustacheRenderer()
#        renderer = pystache.renderer.Renderer(search_dirs=[dataFolder,],
#                                              file_extension='.mustache')
##        print 'renderer', renderer
#        logHtml = renderer.render(mustache_template, mustacheMap)

        logHtml = pystache.render(mustache_template, mustacheMap)

        logFile = os.path.abspath(os.path.join(self.html_folder, logFilename))
        with open(logFile, 'wt') as f:
            # TODO: explicitly encode unicode
            f.write(logHtml)

        if groupName is not None:
            self.logFileTuples.append( (groupName, groupDescription, logFilename, logShortname,) )


    def process(self):
        startTime = time.time()

        self.configure()

        if self.assess_only:
            print 'Entering assessment mode...'
            self.assessKerning()
            return

        self.timing.mark('configure.')

        if not self.do_not_modify_side_bearings:
            self.clearSideBearings()
            self.timing.mark('clearSideBearings.')

        self.processAllKerningPairs()
        self.timing.mark('processAllKerningPairs.')

#        print 'logDisparities'

        if not self.do_not_modify_side_bearings:
#            print 'updateSideBearings'
            self.updateSideBearings()
            self.timing.mark('updateSideBearings.')

#        print 'updateKerning'
        self.updateKerning()
        self.timing.mark('updateKerning.')

        self.writeSamples()
        self.timing.mark('writeSamples.')

        self.logDisparities()
        self.timing.mark('logDisparities.')

        self.elapsedDatetime = formatTimeDuration(time.time() - startTime)
        self.finishDatetime = time.strftime('%h. %d, %Y %H:%M:%S', time.localtime())

        self.writeLogIndex()
        self.timing.mark('writeLogIndex.')

        self.dstUfoFont.update()
        self.dstUfoFont.save(self.ufo_dst_path)
        self.dstUfoFont.close()

        self.timing.mark('finished.')
        if True:
            self.timing.dump()


if __name__ == "__main__":
    autokern = Autokern()
    AutokernSettings(autokern).getCommandLineSettings()
    try:
        autokern.process()
        print
        print 'complete.'
    except Exception, e:
        print 'Error:', e.message
