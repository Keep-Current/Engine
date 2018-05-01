#!/usr/bin/python
# encoding: utf-8
"""
custom_stopwords
Purpose: Collect custom stopwords lists

Author: datadonk23 (datadonk23@gmail.com)
Date: 2018-05-01
"""

arxiv_stopwords = ["arxiv",
                   "astro-ph", "astro-ph.co", "astro-ph.ep", "astro-ph.ga", "astro-ph.he", "astro-ph.im", "astro-ph.sr",
                   "cond-mat.dis-nn", "cond-mat.mes-hall", "cond-mat.mtrl-sci", "cond-mat.other", "cond-mat.quant-gas", "cond-mat.soft", "cond-mat.stat-mech", "cond-mat.str-el", "cond-mat.supr-con",
                   "cs.ai", "cs.ar", "cs.CC", "cs.ce", "cs.cg", "cs.cl", "cs.cr", "cs.cv", "cs.cy", "cs.db", "cs.dc", "cs.dl", "cs.dm", "cs.ds", "cs.et", "cs.fl", "cs.gl", "cs.gr", "cs.gt", "cs.hc", "cs.ir", "cs.it", "cs.lg", "cs.lo", "cs.ma","cs.mm", "cs.ms", "cs.na", "cs.ne", "cs.ni", "cs.oh", "cs.os", "cs.pf", "cs.pl", "cs.ro", "cs.sc", "cs.sd", "cs.se", "cs.si", "cs.sy", "econ.em",
                   "eess.as", "eess.iv", "eess.sp",
                   "gr-qc",
                   "hep-ex", "hep-lat", "hep-ph", "hep-th",
                   "math.ac", "math.ag", "math.ap","math.at", "math.ca", "math.co", "math.ct", "math.cv", "math.dg", "math.ds", "math.fa", "math.gm", "math.gn", "math.gr", "math.gt", "math.ho", "math.it", "math.kt", "math.lo", "math.mg", "math.mp", "math.na", "math.nt", "math.oa", "math.oc", "math.pr", "math.qa", "math.ra", "math.rt", "math.sg", "math.sp", "math.st", "math-ph",
                   "nlin.ao", "nlin.cd", "nlin.cg", "nlin.ps", "nlin.si",
                   "nucl-ex", "nucl-th",
                   "physics.acc-ph", "physics.ao-ph", "physics.app-ph", "physics.atm-clus", "physics.atom-ph", "physics.bio-ph", "physics.chem-ph", "physics.class-ph", "physics.comp-ph", "physics.data-an", "physics.ed-ph", "physics.flu-dyn", "physics.gen-ph", "physics.geo-ph", "physics.hist-ph", "physics.ins-det", "physics.med-ph", "physics.optics", "physics.plasm-ph", "physics.pop-ph", "physics.soc-ph", "physics.space-ph",
                   "q-bio.bm", "q-bio.cb","q-bio.gn", "q-bio.mn", "q-bio.nc", "q-bio.ot", "q-bio.pe", "q-bio.qm", "q-bio.sc", "q-bio.to", "q-fin.cp", "q-fin.ec", "q-fin.gn", "q-fin.mf", "q-fin.PM", "q-fin.PR", "q-fin.RM", "q-fin.ST", "q-fin.tr",
                   "quant-ph",
                   "stat.ap", "stat.co", "stat.me", "stat.ml", "stat.ot", "stat.th"]

def get_stopwords():
    """ Make custom stopwords list accessible

    :return: [stopwords] - List of stopwords
    """
    stopwords_list = arxiv_stopwords # add additional lists with +

    return stopwords_list
