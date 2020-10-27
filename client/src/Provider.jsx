import React from 'react';
import { GQLProvider } from 'Providers';

const Provider = (props) => {
    return (
        <GQLProvider>
            {props.children}
        </GQLProvider>
    )
};

export { Provider };
