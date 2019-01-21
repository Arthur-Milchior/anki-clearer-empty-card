from anki.collection import _Collection
from anki.lang import _
from anki.utils import ids2str


def emptyCardReport(self, cids):
    rep = []
    for ords, mid, flds in self.db.all("""
    select group_concat(ord), mid, flds from cards c, notes n
    where c.nid = n.id and c.id in %s group by nid""" % ids2str(cids)):
        model = mw.col.models.get(mid)
        templates = model["tmpls"]
        rep.append(_("Empty cards")+": ")
        for ord in ords.split(","):
            ord = int(ord)
            templateName = templates[ord]["name"]
            rep.append(templateName+", ")
        rep.append("\nFields: %(f)s\n\n" % dict(f=flds.replace("\x1f", " / ")))
    return "".join(rep)


_Collection.emptyCardReport = emptyCardReport
