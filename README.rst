Introduction
============

This is `Enfold Systems'`_ low level ZODB stats tool [1]_.

Installation
============

Inside Plone
-------------

To install in Plone, add ``collective.stats`` to your ``plone.recipe.zope2instance`` section's eggs parameter e.g.::

    [instance]
    recipe = plone.recipe.zope2instance
    eggs =
        Plone
        …
        collective.stats

Plone 3.3 usage requires appending [oldzope] to ``collective.stats``::

    [instance]
    recipe = plone.recipe.zope2instance
    eggs =
        Plone
        …
        collective.stats [oldzope]

Plone 3.3 on Windows requires a Python 2.4 compilation of the ``psutil`` package which can be found at http://dist.enfoldsystems.com/simple

Run buildout and run Plone in the foreground, and you will see output like this::

    2011-09-22 22:25:30 INFO Zope Ready to handle requests
    2011-09-22 22:25:50 INFO collective.stats | 0.0021 0.0014 0.0018 0.0004 0.0000 0000 0000 0000 | GET:/favicon.ico | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 116708 - 116744
    2011-09-22 22:25:55 INFO collective.stats | 0.1783 0.0021 0.1779 0.0004 0.0000 0000 0000 0000 | GET:/manage_main | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 116756 - 116948
    2011-09-22 22:25:55 INFO collective.stats | 0.0020 0.0013 0.0017 0.0004 0.0000 0000 0000 0000 | GET:/misc_/OFSP/dtmlmethod.gif | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 117076 - 117076
    2011-09-22 22:25:55 INFO collective.stats | 0.0018 0.0012 0.0016 0.0004 0.0000 0000 0000 0000 | GET:/misc_/TemporaryFolder/tempfolder.gif | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 117076 - 117076
    2011-09-22 22:25:55 INFO collective.stats | 0.0021 0.0013 0.0018 0.0004 0.0000 0000 0000 0000 | GET:/misc_/SiteAccess/VirtualHostMonster.gif | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 117076 - 117076
    2011-09-22 22:25:58 INFO collective.stats | 0.3960 0.0015 0.3957 0.0004 0.0000 0000 0000 0000 | GET:/@@plone-addsite | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 117076 - 126352
    2011-09-22 22:25:58 INFO collective.stats | 0.0020 0.0014 0.0017 0.0004 0.0000 0000 0000 0000 | GET:/++resource++plone-admin-ui.css | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 126352 - 126356
    2011-09-22 22:25:58 INFO collective.stats | 0.0014 0.0009 0.0012 0.0004 0.0000 0000 0000 0000 | GET:/++resource++plone-logo.png | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 126356 - 126360


Outside Plone
-------------

To use it outside of Plone, after configuring ``collective.stats`` to be used inside Plone (as described above) configure a ``zc.recipe.egg`` section in your buildout like so::

    [zopepy]
    recipe = zc.recipe.egg
    eggs = ${instance:eggs}
    interpreter = zopepy
    scripts = collective-stats

Run buildout, and this will create a script called ``collective-stats`` you can use to parse Plone logs and produce a ``.csv`` file::

    $ bin/collective-stats var/log/instance.log
    …
    1.3170 0.0196 1.3139 0.0004 0.0000 0000 0000 0003 | GET:/Plone
    0.0283 0.0274 0.0278 0.0004 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/member.css
    0.0153 0.0147 0.0150 0.0003 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/forms.css
    0.0176 0.0167 0.0171 0.0003 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/ploneKss.css
    0.0704 0.0694 0.0699 0.0003 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/++resource++plone.app.discussion.stylesheets/discussion.css
    0.0096 0.0090 0.0093 0.0003 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/print.css
    0.0067 0.0061 0.0064 0.0003 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/mobile.css
    0.0920 0.0709 0.0915 0.0003 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/++resource++tinymce.stylesheets/tinymce.css
    0.0319 0.0313 0.0316 0.0003 0.0034 0004 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/ploneCustom.css
    0.0078 0.0069 0.0075 0.0003 0.0000 0000 0000 0000 | GET:/Plone/portal_kss/Sunburst Theme/plone.kss

Check the current directory and you should see a ``stats.csv`` file::

    $ ls -1
    …
    lib/
    parts/
    setup.py
    src/
    stats.csv
    var/

Take a peek at the top of that file to see the column headers::

    $ head stats.csv 
    url,time,t traverse,t commit,t transchain,setstate,total,total cached,modified,rss before,rss after
    GET:/favicon.ico,0.0021,0.0014,0.0018,0.0000,0000,0000,0000,116708,116744
    GET:/manage_main,0.1783,0.0021,0.1779,0.0000,0000,0000,0000,116756,116948
    GET:/manage_page_style.css,0.0110,0.0014,0.0108,0.0000,0000,0000,0000,116948,117012
    GET:/p_/ltab,0.0023,0.0008,0.0021,0.0000,0000,0000,0000,117020,117032
    GET:/p_/sp,0.0100,0.0054,0.0099,0.0039,0018,0004,0000,116992,117032
    GET:/p_/rtab,0.0020,0.0012,0.0018,0.0000,0000,0000,0000,117032,117032
    GET:/misc_/OFSP/Folder_icon.gif,0.0018,0.0012,0.0016,0.0000,0000,0000,0000,117032,117032
    GET:/p_/ControlPanel_icon,0.0017,0.0009,0.0015,0.0000,0000,0000,0000,117036,117036
    GET:/misc_/OFSP/UserFolder_icon.gif,0.0017,0.0012,0.0015,0.0000,0000,0000,0000,117036,117036


Documentation
=============

Column header details:

+--------------+---------------------------------------------------------------+
|Header        |Detail                                                         |
+--------------+---------------------------------------------------------------+
|time          |Total time inside publisher                                    |
+--------------+---------------------------------------------------------------+
|t traverse    |This is time when zope publisher gets publishable object       |
+--------------+---------------------------------------------------------------+
|t commit      |Time on transaction.commit()                                   |
+--------------+---------------------------------------------------------------+
|t transchain  |Time in plone.transformchain.applyTransform                    |
+--------------+---------------------------------------------------------------+
|setstate      |Total time inside Connection.setstate                          |
+--------------+---------------------------------------------------------------+
|total         |Total zodb object loads                                        |
+--------------+---------------------------------------------------------------+
|total cached  |Total loads from cache                                         |
+--------------+---------------------------------------------------------------+
|modified      |Total modified objects                                         |
+--------------+---------------------------------------------------------------+
|rss before    |RAM usage before request                                       |
+--------------+---------------------------------------------------------------+
|rss after     |RAM usage after request                                        |
+--------------+---------------------------------------------------------------+

An Example
==========

If you enable collective.stats to emit stats in response headers you will see a response line such as::

    X-Stats:4.5556 0.0232 1.2539 0.6334 9266 1244 0000

Deciphering::

    4.555 - (time) is total time in Zope Publisher

    0.023 - (t traverse) is after traverse time (callable object inside Publisher)
            time from BEGINNING of request to after TRAVERSE time.

    1.253 - (t commit) is before commit() (we have a complete RESPONSE object)
            time from BEGINGING of request to before COMMIT

    0.6334 - (setstate) total time in __setstate__ (time of ZODB spent unghostifying # of LOAD objects)

    9266 - (total) total number of LOADS

    1244 - (total cached) total number of HOT LOADS (cache hits in ZODB)

    0000 - (modified) total number of MODIFIED objects.

Summary
-------

t_time - t_commit = total time to commit() (time executed in IPubBeforeCommit)
If you are using plone.app.caching or plone.app.theming both of which use
commit events; so depending how collective.stats gets registered - its possible
those are not being captured.

In this example 3.3 seconds is "lost" in commit.  In this particular case
it was due to unoptimized plone.app.theming / diazo rules file.


Enjoy!

.. _`Enfold Systems'`: http://enfoldsystems.com


.. [1] ``collective.stats`` has been donated to the Plone collective by Enfold Systems under a BSD-like license (ZPL 2.1).
