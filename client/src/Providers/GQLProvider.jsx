import React from 'react';
import {  ApolloProvider, ApolloClient, HttpLink, InMemoryCache } from '@apollo/client';

const link = new HttpLink({
  uri: 'https://localhost/s/graphql',
})

const client = new ApolloClient({
  link,
  cache: new InMemoryCache(),
});

const GQLProvider = (props) => {
    return (
        <ApolloProvider client={client} >
            {props.children}
        </ApolloProvider>
    )
};

export { GQLProvider };
