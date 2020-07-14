# -*- coding: utf-8 -*-
from odoo import http

# class ProjectScrumSprint(http.Controller):
#     @http.route('/project_scrum_sprint/project_scrum_sprint/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_scrum_sprint/project_scrum_sprint/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_scrum_sprint.listing', {
#             'root': '/project_scrum_sprint/project_scrum_sprint',
#             'objects': http.request.env['project_scrum_sprint.project_scrum_sprint'].search([]),
#         })

#     @http.route('/project_scrum_sprint/project_scrum_sprint/objects/<model("project_scrum_sprint.project_scrum_sprint"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_scrum_sprint.object', {
#             'object': obj
#         })