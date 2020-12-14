import pathlib
import attr

from pylexibank.providers.sndcmp import SNDCMP as BaseDataset
from pylexibank.providers.sndcmp import SNDCMPConcept


@attr.s
class CustomConcept(SNDCMPConcept):
    Spanish_Gloss = attr.ib(default=None)


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = 'mixezoqueanvoices'

    study_name = 'MixeZoque'
    second_gloss_lang = 'Spanish'
    source_id_array = ['Kondic2019']
    create_cognates = False

    only_proto_forms = True
    form_placeholder = '►'

    concept_class = CustomConcept

    def get_source_id_array(self, lexeme):
        # author of proto forms is Wichmann1995
        if lexeme['LanguageIx'] in ['60002000000', '61002000000', '61052000000']:
            return ['Wichmann1995'] + self.source_id_array
        return self.source_id_array
