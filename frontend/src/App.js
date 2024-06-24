import React from 'react';
import ExchangeForm from './components/ExchangeForm';
import DataInfo from './components/DataInfo';

function App() {
    return (
        <div className="App">
            <h1>CCXT2SQL</h1>
            <ExchangeForm />
            <DataInfo />
        </div>
    );
}

export default App;
