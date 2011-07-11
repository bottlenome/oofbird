from mako.template import Template

tmpl = Template("""\
%if user:
* Hello ${user}
%else:
* Hello guest!!
%endif
** Test services
%for service in services:
- ${service}
%endfor
""")

print tmpl.render(**{'user' : 'urota',
                     'services' : ['moge',
                                   'hoge']})

