
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

Run buildout and run Plone in the foreground, and you will see output like this::

    2011-09-22 22:25:30 INFO Zope Ready to handle requests
    2011-09-22 22:25:50 INFO collective.stats | 0.0021 0.0014 0.0018 0.0000 0000 0000 0000 | GET:/favicon.ico | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 116708 - 116744
    2011-09-22 22:25:55 INFO collective.stats | 0.1783 0.0021 0.1779 0.0000 0000 0000 0000 | GET:/manage_main | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 116756 - 116948
    2011-09-22 22:25:55 INFO collective.stats | 0.0110 0.0014 0.0108 0.0000 0000 0000 0000 | GET:/manage_page_style.css | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 116948 - 117012
    2011-09-22 22:25:55 INFO collective.stats | 0.0023 0.0008 0.0021 0.0000 0000 0000 0000 | GET:/p_/ltab | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 117020 - 117032
    2011-09-22 22:25:55 INFO collective.stats | 0.0100 0.0054 0.0099 0.0039 0018 0004 0000 | GET:/p_/sp | t: 0.0002, t_c: 0.0000, t_nc: 0.0002 | RSS: 116992 - 117032
    2011-09-22 22:25:55 INFO collective.stats | 0.0020 0.0012 0.0018 0.0000 0000 0000 0000 | GET:/p_/rtab | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 117032 - 117032
    2011-09-22 22:25:55 INFO collective.stats | 0.0018 0.0012 0.0016 0.0000 0000 0000 0000 | GET:/misc_/OFSP/Folder_icon.gif | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 117032 - 117032
    2011-09-22 22:25:55 INFO collective.stats | 0.0017 0.0009 0.0015 0.0000 0000 0000 0000 | GET:/p_/ControlPanel_icon | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 117036 - 117036
    2011-09-22 22:25:55 INFO collective.stats | 0.0017 0.0012 0.0015 0.0000 0000 0000 0000 | GET:/misc_/OFSP/UserFolder_icon.gif | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 117036 - 117036
    2011-09-22 22:25:55 INFO collective.stats | 0.0057 0.0046 0.0054 0.0000 0000 0000 0000 | GET:/misc_/Sessions/idmgr.gif | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 117056 - 117060
    2011-09-22 22:25:55 INFO collective.stats | 0.0023 0.0015 0.0021 0.0000 0000 0000 0000 | GET:/misc_/SiteErrorLog/error.gif | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 117060 - 117060
    2011-09-22 22:25:55 INFO collective.stats | 0.0019 0.0014 0.0016 0.0000 0000 0000 0000 | GET:/misc_/OFSP/Image_icon.gif | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 117072 - 117072
    2011-09-22 22:25:55 INFO collective.stats | 0.0022 0.0014 0.0019 0.0000 0000 0000 0000 | GET:/misc_/ExternalEditor/edit_icon | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 117072 - 117072
    2011-09-22 22:25:55 INFO collective.stats | 0.0020 0.0013 0.0018 0.0000 0000 0000 0000 | GET:/misc_/PageTemplates/zpt.gif | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 117072 - 117072
    2011-09-22 22:25:55 INFO collective.stats | 0.0023 0.0012 0.0021 0.0000 0000 0000 0000 | GET:/misc_/Sessions/datamgr.gif | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 117072 - 117072
    2011-09-22 22:25:55 INFO collective.stats | 0.0020 0.0013 0.0017 0.0000 0000 0000 0000 | GET:/misc_/OFSP/dtmlmethod.gif | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 117076 - 117076
    2011-09-22 22:25:55 INFO collective.stats | 0.0018 0.0012 0.0016 0.0000 0000 0000 0000 | GET:/misc_/TemporaryFolder/tempfolder.gif | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 117076 - 117076
    2011-09-22 22:25:55 INFO collective.stats | 0.0021 0.0013 0.0018 0.0000 0000 0000 0000 | GET:/misc_/SiteAccess/VirtualHostMonster.gif | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 117076 - 117076
    2011-09-22 22:25:58 INFO collective.stats | 0.3960 0.0015 0.3957 0.0000 0000 0000 0000 | GET:/@@plone-addsite | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 117076 - 126352
    2011-09-22 22:25:58 INFO collective.stats | 0.0020 0.0014 0.0017 0.0000 0000 0000 0000 | GET:/++resource++plone-admin-ui.css | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 126352 - 126356
    2011-09-22 22:25:58 INFO collective.stats | 0.0014 0.0009 0.0012 0.0000 0000 0000 0000 | GET:/++resource++plone-logo.png | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 126356 - 126360


Outside Plone
-------------

To use it outside of Plone, configure a ``zc.recipe.egg`` section in your buildout like so::

    [zopepy]
    recipe = zc.recipe.egg
    eggs = ${instance:eggs}
    interpreter = zopepy

Run buildout, and this will create a script called ``collective-stats`` you can use to parse Plone logs and produce a ``.csv`` file::

    $ bin/collective-stats var/log/plone.log
    …
    1.3170 0.0196 1.3139 0.0000 0000 0000 0003 | GET:/Plone
    0.0283 0.0274 0.0278 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/member.css
    0.0152 0.0145 0.0148 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/portlets.css
    0.0166 0.0157 0.0161 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/public.css
    0.0733 0.0725 0.0728 0.0485 0371 0097 0000 | GET:/Plone/portal_css/Sunburst Theme/authoring.css
    0.0310 0.0304 0.0307 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/columns.css
    0.0269 0.0262 0.0265 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/base.css
    0.0228 0.0221 0.0224 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/controlpanel.css
    0.0135 0.0126 0.0130 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/navtree.css
    0.0261 0.0254 0.0257 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/deprecated.css
    0.0154 0.0148 0.0151 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/invisibles.css
    0.0153 0.0147 0.0150 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/forms.css
    0.0176 0.0167 0.0171 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/ploneKss.css
    0.0704 0.0694 0.0699 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/++resource++plone.app.discussion.stylesheets/discussion.css
    0.0096 0.0090 0.0093 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/print.css
    0.0067 0.0061 0.0064 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/mobile.css
    0.0920 0.0709 0.0915 0.0000 0000 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/++resource++tinymce.stylesheets/tinymce.css
    0.0319 0.0313 0.0316 0.0034 0004 0000 0000 | GET:/Plone/portal_css/Sunburst Theme/ploneCustom.css
    0.0197 0.0187 0.0192 0.0000 0000 0000 0000 | GET:/Plone/portal_kss/Sunburst Theme/++resource++tinymce.kss/tinymce.kss
    0.0350 0.0344 0.0347 0.0024 0023 0000 0000 | GET:/Plone/portal_kss/Sunburst Theme/at.kss
    0.0271 0.0264 0.0268 0.0000 0000 0000 0000 | GET:/Plone/portal_kss/Sunburst Theme/plone.kss
    0.0193 0.0182 0.0188 0.0000 0000 0000 0000 | GET:/Plone/portal_kss/Sunburst Theme/++resource++plone.app.form.kss
    0.0208 0.0196 0.0203 0.0000 0000 0000 0000 | GET:/Plone/portal_kss/Sunburst Theme/++resource++plone.app.z3cform
    0.0370 0.0364 0.0367 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/jquery-integration.js
    0.0073 0.0063 0.0068 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/++resource++plone.app.jquerytools.js
    0.0073 0.0064 0.0068 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/++resource++plone.app.jquerytools.overlayhelpers.js
    0.0077 0.0067 0.0072 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/++resource++plone.app.jquerytools.form.js
    0.1040 0.1021 0.1037 0.0193 0144 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/jquery.js
    0.0255 0.0242 0.0250 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/register_function.js
    0.0199 0.0193 0.0196 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/plone_javascript_variables.js
    0.0278 0.0270 0.0274 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/cookie_functions.js
    0.0342 0.0335 0.0338 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/nodeutilities.js
    0.0309 0.0302 0.0305 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/livesearch.js
    0.0083 0.0066 0.0078 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/++resource++search.js
    0.0465 0.0460 0.0462 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/modernizr.js
    0.0273 0.0267 0.0270 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/dragdropreorder.js
    0.0307 0.0302 0.0304 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/select_all.js
    0.0168 0.0161 0.0164 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/collapsiblesections.js
    0.0090 0.0084 0.0087 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/jquery.highlightsearchterms.js
    0.0434 0.0427 0.0430 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/popupforms.js
    0.0203 0.0196 0.0199 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/first_input_focus.js
    0.1155 0.1148 0.1151 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/form_tabbing.js
    0.0282 0.0276 0.0279 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/accessibility.js
    0.0322 0.0316 0.0319 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/styleswitcher.js
    0.0174 0.0167 0.0170 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/toc.js
    0.0205 0.0198 0.0201 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/collapsibleformfields.js
    0.0366 0.0357 0.0361 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/dropdown.js
    0.0800 0.0789 0.0795 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/++resource++plone.app.discussion.javascripts/comments.js
    0.0304 0.0298 0.0301 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/sarissa.js
    0.0299 0.0293 0.0296 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/calendar_formfield.js
    0.0567 0.0560 0.0563 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/table_sorter.js
    0.0256 0.0250 0.0253 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/formsubmithelpers.js
    0.0345 0.0339 0.0342 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/formUnload.js
    0.0460 0.0449 0.0454 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/unlockOnFormUnload.js
    0.2281 0.1196 0.2276 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/tiny_mce.js
    0.0136 0.0128 0.0132 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/tiny_mce_init.js
    0.0064 0.0048 0.0060 0.0000 0000 0000 0000 | GET:/Plone/logo.png
    0.1291 0.0044 0.1287 0.0000 0000 0000 0000 | GET:/Plone/spinner.gif
    5.7199 0.0509 5.7192 0.0000 0000 0000 0000 | GET:/Plone/portal_javascripts/Sunburst Theme/++resource++kukit.js
    0.0087 0.0078 0.0083 0.0000 0000 0000 0000 | GET:/Plone/portal_kss/Sunburst Theme/at.kss
    0.0078 0.0069 0.0075 0.0000 0000 0000 0000 | GET:/Plone/portal_kss/Sunburst Theme/plone.kss

Check the current directory and you should see a ``stats.csv`` file::

    $ ls -1
    …
    lib/
    parts/
    setup.py
    src/
    stats.csv
    var/

Take a peak at the top of that file to see the column headers::

    $ head stats.csv 
    url,time,t traverse,t commit,setstate,total,total cached,modified,rss before,rss after
    GET:/favicon.ico,0.0021,0.0014,0.0018,0.0000,0000,0000,0000,116708,116744
    GET:/manage_main,0.1783,0.0021,0.1779,0.0000,0000,0000,0000,116756,116948
    GET:/manage_page_style.css,0.0110,0.0014,0.0108,0.0000,0000,0000,0000,116948,117012
    GET:/p_/ltab,0.0023,0.0008,0.0021,0.0000,0000,0000,0000,117020,117032
    GET:/p_/sp,0.0100,0.0054,0.0099,0.0039,0018,0004,0000,116992,117032
    GET:/p_/rtab,0.0020,0.0012,0.0018,0.0000,0000,0000,0000,117032,117032
    GET:/misc_/OFSP/Folder_icon.gif,0.0018,0.0012,0.0016,0.0000,0000,0000,0000,117032,117032
    GET:/p_/ControlPanel_icon,0.0017,0.0009,0.0015,0.0000,0000,0000,0000,117036,117036
    GET:/misc_/OFSP/UserFolder_icon.gif,0.0017,0.0012,0.0015,0.0000,0000,0000,0000,117036,117036

Enjoy!

.. _`Enfold Systems'`: http://enfoldsystems.com


.. [1] ``collective.stats`` has been donated to the Plone collective by Enfold Systems under a BSD-like license (ZPL 2.1).
