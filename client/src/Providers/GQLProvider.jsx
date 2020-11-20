import React from 'react';
import {  ApolloProvider, ApolloClient, HttpLink, InMemoryCache } from '@apollo/client';

// the `s` is important and will cause a CORS issue if you forget it
// Ryan forgot it and spent 45 min debugging 1/10 wouldnt reccomend
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
