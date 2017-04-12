#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright (c) 2002-2017 "Neo Technology,"
# Network Engine for Objects in Lund AB [http://neotechnology.com]
#
# This file is part of Neo4j.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# tag::hello-world-import[]
from neo4j.v1 import GraphDatabase
# end::hello-world-import[]

# tag::hello-world[]
class HelloWorldExample:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver( uri, auth=(user, password))

    #FIXME: this goes in if __name__ == '__main__'
    public static void main( String... args ) throws Exception
    {
        HelloWorldExample greeter = new HelloWorldExample( "bolt://localhost:7687", "neo4j", "password" );
        greeter.printGreeting( "hello, world" );
    }

    def close(self):
        self._driver.close();

    def printGreeting(self, message):
        try ( Session session = driver.session() )
        {
            String greeting = session.writeTransaction( new TransactionWork<String>()
            {
                @Override
                public String execute( Transaction tx )
                {
                    StatementResult result = tx.run( "CREATE (a:Greeting) " +
                                                     "SET a.message = $message " +
                                                     "RETURN a.message + ', from node ' + id(a)",
                            parameters( "message", message ) );
                    return result.single().get( 0 ).asString();
                }
            } );
            print(greeting)
        }
    }
}
# end::hello-world[]

# tag::hello-world-output[]
# hello, world, from node 1234
# end::hello-world-output[]
