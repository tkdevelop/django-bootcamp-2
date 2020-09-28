from django.views.generic import TemplateView

from .models import Post

class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts': posts,
        }
        return self.render_to_response(context)


class SupportView(TemplateView):
    template_name = "support.html"
 
class ContactView(TemplateView):
    template_name = "contact.html"