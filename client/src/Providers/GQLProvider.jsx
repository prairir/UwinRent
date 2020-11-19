import React from 'react';
import {  ApolloProvider, ApolloClient, InMemoryCache } from '@apollo/client';

const client = new ApolloClient({
  uri: 'http://127.0.0.1:5000/s/graphql',
  cache: new InMemoryCache()
});

const GQLProvider = (props) => {
    return (
        <ApolloProvider client={client} >
            {props.children}
        </ApolloProvider>
    )
};

export { GQLProvider };
