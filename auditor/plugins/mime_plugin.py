from auditor.plugins import base_plugin
from auditor.string_dist import levenshtienDist
import mimetypes

class mimePlugin(base_plugin.BasePlugin):
    '''Plugin that reads mime types.'''
    name    = "mime Plugin."
    author  = "Tom Bytheway"
    version = "0.0.0" 
    
    def load(self,cachedir):
        self.mClass = mimetypes.MimeTypes()
    
    def get_attribute_types(self):
        return {'MIME':levenshtienDist}
    
    def evaluate_file(self,filename,path):
        (t,e) = self.mClass.guess_type(path+'/'+filename)
        if t != None:
            return {'MIME':t}
        else:
            return {'MIME':''}
    
    
