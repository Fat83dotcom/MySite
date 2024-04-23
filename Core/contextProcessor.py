from SiteSetup.models import SiteSetup, SiteSetupPicture


def contextSiteSetup(request):
    result = SiteSetup.objects.order_by('-id').first()
    result_pics = SiteSetupPicture.objects.all()
    return {
        'siteSetup': result,
        'siteSetupPic': result_pics,
    }
