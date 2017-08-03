"""Methods to pull data from source into GitHub."""
import requests
import os
import json
import codecs

class HarvestSource:

    def __init__(self, form, items):
        print("Creating an instance of a Harvest Source object.")
        self.format = form
        self.items = items

class StanfordHarvest(HarvestSource):
    purl = "https://purl.stanford.edu/%s.mods"
    marc = "https://searchworks.stanford.edu/view/%s.marcxml"

    def __init__(self, form, items):
        HarvestSource.__init__(self, form, items)

    def download(self):
        print("format: " + self.format)
        if self.format == 'mods':
            for id in self.items:
                if 'druid:' in id:
                    id = id.replace('druid:', '')
                resp = requests.get(StanfordHarvest.purl % id).text
                # Add validation step
                out = "output/stanford_" + id + ".mods.xml"
                os.makedirs(os.path.dirname(out), exist_ok=True)
                with open(out, 'w') as fh:
                    fh.write(resp)

        elif self.format == 'marc':
            for id in self.items:
                resp = requests.get(StanfordHarvest.marc % id).text
                # Add validation step
                out = "output/stanford_" + id + ".marc.xml"
                os.makedirs(os.path.dirname(out), exist_ok=True)
                with open(out, 'w') as fh:
                    fh.write(resp)

        elif self.format == 'iiif':
            # do something else
            print('done')

class PrincetonHarvest(HarvestSource):
    marc = "https://pulsearch.princeton.edu/catalog/%s.marcxml"
    geomarc = "https://raw.githubusercontent.com/OpenGeoMetadata/edu.princeton.arks/master/%s/marc.xml"
    fgdc = "https://raw.githubusercontent.com/OpenGeoMetadata/edu.princeton.arks/master/%s/fgdc.xml"

    def __init__(self, form, items):
        HarvestSource.__init__(self, form, items)

    def download(self):
        print("format: " + self.format)
        if self.format == 'marc':
            for id in self.items:
                resp = requests.get(PrincetonHarvest.marc % id).text
                # Add validation step
                out = "output/princeton_" + id + ".marc.xml"
                os.makedirs(os.path.dirname(out), exist_ok=True)
                with open(out, 'w') as fh:
                    fh.write(resp)

        elif self.format == 'opengeo':
            for id in self.items:
                ark = id[:2] + '/' + id[2:4] + '/' + id[4:6] + '/' + id[6:8] + '/' + id[8:]
                resp = requests.get(PrincetonHarvest.geomarc % ark).text
                out = "output/princeton_" + id + ".marc.xml"
                os.makedirs(os.path.dirname(out), exist_ok=True)
                with open(out, 'w') as fh:
                    fh.write(resp)
                resp2 = requests.get(PrincetonHarvest.fgdc % ark).text
                out = "output/princeton_" + id + ".fgdc.xml"
                os.makedirs(os.path.dirname(out), exist_ok=True)
                with open(out, 'w') as fh:
                    fh.write(resp)

class PennHarvest(HarvestSource):
    tei = "http://openn.library.upenn.edu/Data/0001/%s/data/%s_TEI.xml"

    def __init__(self, form, items):
        HarvestSource.__init__(self, form, items)

    def download(self):
        print("format: " + self.format)
        if self.format == 'tei':
            for id in self.items:
                resp = requests.get(PennHarvest.tei % (id, id)).text
                # Add validation step
                out = "output/penn_" + id + ".tei.xml"
                os.makedirs(os.path.dirname(out), exist_ok=True)
                with open(out, 'w') as fh:
                    fh.write(resp)
        elif self.format == 'local':
            for id in self.items:
                with open(id) as fh:
                    invalid = fh.read().replace('\n', '').replace('   ', '')
                    valid = "[" + invalid.replace('}{', '},{') + "]"
                    data = json.loads(valid)
                    for object in data:
                        emuIRN = object['emuIRN']
                        out = "output/penn_" + emuIRN + ".local.json"
                        os.makedirs(os.path.dirname(out), exist_ok=True)
                        with open(out, 'w') as fh:
                            fh.write(resp)
