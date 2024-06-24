import React, { useState } from 'react';

function ExchangeForm() {
    const [exchange, setExchange] = useState('');
    const [ticker, setTicker] = useState('');
    const [timeframe, setTimeframe] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch('/api/exchanges', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ exchange, ticker, timeframe }),
        });
        const data = await response.json();
        console.log(data);
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Exchange:
                <input type="text" value={exchange} onChange={(e) => setExchange(e.target.value)} />
            </label>
            <label>
                Ticker:
                <input type="text" value={ticker} onChange={(e) => setTicker(e.target.value)} />
            </label>
            <label>
                Timeframe:
                <input type="text" value={timeframe} onChange={(e) => setTimeframe(e.target.value)} />
            </label>
            <button type="submit">Add</button>
        </form>
    );
}

export default ExchangeForm;
