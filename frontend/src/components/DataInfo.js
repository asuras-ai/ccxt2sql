import React, { useEffect, useState } from 'react';

function DataInfo() {
    const [dataInfo, setDataInfo] = useState([]);

    useEffect(() => {
        fetch('/api/data_info')
            .then(response => response.json())
            .then(data => setDataInfo(data));
    }, []);

    return (
        <div>
            <h2>Data Information</h2>
            <table>
                <thead>
                    <tr>
                        <th>Table</th>
                        <th>First Timestamp</th>
                        <th>Last Timestamp</th>
                    </tr>
                </thead>
                <tbody>
                    {dataInfo.map(info => (
                        <tr key={info.table}>
                            <td>{info.table}</td>
                            <td>{new Date(info.first_timestamp).toLocaleString()}</td>
                            <td>{new Date(info.last_timestamp).toLocaleString()}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default DataInfo;
