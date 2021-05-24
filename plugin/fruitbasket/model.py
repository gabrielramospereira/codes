#!/usr/bin/python
# -*- coding: utf-8 -*-

from trac.db import Column, Table, DatabaseManager

class FruitBasketSchema(object):
    class columns(object):
        ID = 'id'
        NOME = 'nome'
        SABOR = 'sabor'
        TAMANHO = 'tamanho'
        PESO = 'peso'
        COR = 'cor'

    tablename = 'fruitbasket_plugin'
    table = Table(tablename, key=columns.ID)[
        Column(columns.ID, auto_increment=True),
        Column(columns.NOME),
        Column(columns.SABOR),
        Column(columns.TAMANHO),
        Column(columns.PESO),
        Column(columns.COR)
    ]

class FruitBasketModel(object):

    @classmethod
    def is_database_okay(cls, env):
        dbmgr = DatabaseManager(env)
        schema = FruitBasketSchema

        if dbmgr.has_table(schema.tablename):
            columns_in_db = set(dbmgr.get_column_names(schema.tablename))
            columns_needed = set([column.name for column in schema.table.columns])

            columns_is_equals = True
            for column in columns_needed:
                if column not in columns_in_db:
                    columns_is_equals = False
                    break

            if columns_is_equals:
                return True
        return False

    @classmethod
    def create_table(cls, env):
        dbmgr = DatabaseManager(env)
        connector, _ = dbmgr._get_connector()
        schema = FruitBasketSchema

        with env.db_transaction as db:
            for sql in connector.to_sql(schema.table):
                db(sql)

    @classmethod
    def select(cls, env):
        schema = FruitBasketSchema
        columns = [
            schema.columns.ID, 
            schema.columns.NOME, 
            schema.columns.SABOR, 
            schema.columns.TAMANHO, 
            schema.columns.PESO, 
            schema.columns.COR
        ]
        
        sql = (
            'SELECT ' + ','.join(columns) + '\n'
            'FROM ' + schema.tablename + ';'
        )

        fruitbasket = []
        for row in env.db_query(sql):
            fruit = dict(zip(columns, row))
            fruitbasket.append(fruit)

        return fruitbasket

    @classmethod
    def add(cls, env, nome, sabor, tamanho, peso, cor):
        def sql_safe(value):
            return value.replace("'", "\\'").replace('"', '\\"')

        schema = FruitBasketSchema
        columns = [
            schema.columns.NOME, 
            schema.columns.SABOR, 
            schema.columns.TAMANHO, 
            schema.columns.PESO, 
            schema.columns.COR
        ]
        values=[
            "'"+sql_safe(nome)+"'", 
            "'"+sql_safe(sabor)+"'", 
            "'"+sql_safe(tamanho)+"'", 
            "'"+sql_safe(peso)+"'", 
            "'"+sql_safe(cor)+"'"
        ]

        sql = (
            'INSERT INTO ' + schema.tablename + '\n'
            '(' + ','.join(columns) + ')\n'
            'VALUES (' + ','.join(values) + ');'
        )

        env.db_transaction(sql)

    @classmethod
    def remove(cls, env, id):
        schema = FruitBasketSchema

        sql = (
            'DELETE FROM ' + schema.tablename + '\n'
            'WHERE ' + schema.columns.ID + ' = ' + str(id) + '\n'
        )

        env.db_transaction(sql)

