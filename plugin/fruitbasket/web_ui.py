#!/usr/bin/python
# -*- coding: utf-8 -*-

from trac.core import Component, implements
from trac.env import IEnvironmentSetupParticipant
from trac.web import IRequestHandler
from trac.web.chrome import ITemplateProvider, add_stylesheet

from pkg_resources import resource_filename
from fruitbasket.model import FruitBasketModel as model

import re

class FruitBasketPage(Component):
    implements(IRequestHandler, ITemplateProvider, IEnvironmentSetupParticipant)


    # ---- IRequestHandler methods

    def match_request(self, req):
        pattern = r'^/fruitbasket(/[0-9]+)?$'
        return re.match(pattern, req.path_info) is not None

    def process_request(self, req):
        if req.path_info == '/fruitbasket':
            return self.process_request_main(req)
        return self.process_request_detail(req)

        
    # -------- Process Main methods

    def process_request_main(self, req):
        if req.method == 'POST' and 'action' in req.args:
            if req.args['action'] == 'Add':
                self.process_request_main_add(req)
            
            elif req.args['action'] == 'Remove':
                self.process_request_main_remove(req)

        data = dict(
            fruits=model.select(self.env),
            form_token=req.form_token
        )
        
        add_stylesheet(req, 'fruitbasketplugin/css/fruitbasket.css')
        return 'fruitbasket.main.html', data
    
    def process_request_main_add(self, req):
        nome = req.args['nome']
        sabor = req.args['sabor']
        tamanho = req.args['tamanho']
        peso = req.args['peso']
        cor = req.args['cor']

        model.add(self.env, nome, sabor, tamanho, peso, cor)

    def process_request_main_remove(self, req):
        id = req.args['id']

        model.remove(self.env, id)


    # -------- Process Detail methods

    def process_request_detail(self, req):
        pass


    # ---- ITemplateProvider methods

    def get_templates_dirs(self):
        return [resource_filename(__name__, 'templates')]

    def get_htdocs_dirs(self):
        return [('fruitbasketplugin', resource_filename(__name__, 'htdocs'))]


    # ---- IEnvironmentSetupParticipant methods

    def environment_created(self):
        if self.environment_needs_upgrade():
            self.upgrade_environment()

    def environment_needs_upgrade(self):
        return not model.is_database_okay(self.env)
        
    def upgrade_environment(self):
        model.create_table(self.env)
        