from SiteSetup.models import SiteSetup


def contextSiteSetup(request):
    result = SiteSetup.objects.order_by('-id').first()
    return {
        'siteSetup': result
    }
