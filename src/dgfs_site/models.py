from django.db import models
import uuid


class Profile(models.Model):
    profileID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   # user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    social_links = models.JSONField(blank=True, null=True)


class Tag(models.Model):
    tagID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tagNom = models.CharField(max_length=255)


class ServiceProposer(models.Model):
    serviceProposerID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    serviceProposerNom = models.CharField(max_length=255, null=False, unique=True)
    serviceProposerType = models.TextField()


class Categorie(models.Model):
    categorieID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categorieNom = models.CharField(max_length=255, null=False, unique=True)
    categorieDesc = models.TextField(blank=True)


class Etat(models.Model):
    etatID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    etatNom = models.CharField(max_length=255, null=False, unique=True)
    etatDesc = models.TextField(blank=True)


class Province(models.Model):
    provinceID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    provinceNom = models.CharField(max_length=255, null=False, unique=True)
    provinceDesc = models.TextField(blank=True)

    etat = models.ForeignKey(Etat, on_delete=models.CASCADE, null=True)
    
    def __unicode__(self):
        return self.provinceNom

    @property
    def etat_nom(self):
        return self.etat.etatNom


class Region(models.Model):
    regionID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    regionNom = models.CharField(max_length=255, null=False, unique=True)
    regionDesc = models.TextField(blank=True)

    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return self.regionNom

    @property
    def province_nom(self):
        return self.province.provinceNom


class District(models.Model):
    districtID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    districtNom = models.CharField(max_length=255, null=False, unique=True)
    districtDesc = models.TextField(blank=True)

    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)


class Commune(models.Model):
    communeID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    communeNom = models.CharField(max_length=255, null=False)
    communeDesc = models.TextField(blank=True)

    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)


class Fokontany(models.Model):
    fokontanyID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fokontanyNom = models.CharField(max_length=255, null=False)
    fokontanyDesc = models.TextField(blank=True)

    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, null=True)


class Adresse(models.Model):
    fokontanyID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fokontanyNom = models.CharField(max_length=255, null=False)
    fokontanyDesc = models.TextField(blank=True)

    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, null=True)


class CHU_CHRR(models.Model):
    chu_chrrID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chu_chrrNom = models.CharField(max_length=255, null=False)
    chu_chrrDesc = models.TextField(blank=True)

    adresse = models.OneToOneField(Adresse, on_delete=models.SET_NULL, null=True)
    serviceProposer = models.ForeignKey(ServiceProposer, on_delete=models.CASCADE, null=True)


class Actualite(models.Model):
    actualiteID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    actualiteNom = models.CharField(max_length=255)
    contenu = models.TextField(blank=False)
    datePublication = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField(auto_now=True)
    imageActualite = models.ImageField(upload_to='statics/public/images', null=True)

    categorie = models.ManyToManyField(Categorie)
    tags = models.ManyToManyField(Tag)


#   author = models.ForeignKey(User, on_delete=models.CASCADE)


class Commentaire(models.Model):
    commentaireID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    commentaireNom = models.CharField(max_length=255, null=False)
    commentaireContenu = models.TextField(blank=False)
    imageCommentaire = models.ImageField(upload_to='statics/public/images', null=True)
    dateCommentaire = models.DateTimeField(auto_now_add=True)
    is_liked = models.BooleanField(default=False)

    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    actualite = models.ForeignKey(Actualite, on_delete=models.CASCADE)

class NewsLetter(models.Model):
    newsLetterID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    newsLetterNom = models.CharField(max_length=255)
    newsLetterSuject = models.TextField(blank=False, default='default subject')
    newsLetterContenu = models.TextField(blank=False, default='MON COMMENTAIRE')
    emailAbonne = models.EmailField(max_length=50, unique=True)
    date_sent = models.DateTimeField(auto_now_add=True)

    #categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=False)
