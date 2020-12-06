import React, { useEffect, useState } from 'react';
import { Card, CardBody } from 'reactstrap';
import { SERVER_URL } from '../../Constants';
import Source from './source';

const ViewJob = (props) => {

    const data = {'positive': 5, 'negative':10, 'neutral': 7};
    const dict = {
        "risk": 2,
        "vaccine": 8,
        "pfizer": 4,
        "doses": 4,
        "farmers": 2,
        "issues": 2,
        "big": 2,
        "britain": 2,
        "power": 2,
        "coronavirus": 2,
        "hackers": 2,
        "problems": 2,
        "year": 2,
        "xinjiang": 2,
        "uyghur": 2,
        "amazon": 2,
        "boohoo": 2,
        "nice": 1,
        "guys": 1,
        "partyyyy": 1
    };
    
    const [rows, setRows] = useState([]);

    const convertFn = (dict) => {
        let li = [];
        Object.keys(dict).forEach(function(key) {
            li.push({'text': key, 'value': dict[key]});
        });
        return li;
    }

    useEffect(() => {
        var requestOptions = {
            method: 'GET',
            redirect: 'follow'
        };

        console.log('props', localStorage.getItem('jobId'));

        fetch(SERVER_URL+"/job/insights/1", requestOptions)
        .then(response => response.json())
        .then(result => {
            let eleList = [];

            result.map(v => {
                let json = JSON.parse(v.jsonText);

                console.log(json);

                let wordsLi = convertFn(json.keywords);

                eleList.push(<Source key={json.source} sentiment={json.sentiment} words={wordsLi} type={json.source} 
                    count={15} items={json.items} />);
            });

            setRows(eleList);
        })
        .catch(error => console.log('error', error));

    }, []);

    return (
        <div>
            <div>
                {rows && rows.map(v => v)}
            </div>
        </div>
    )
}

export default ViewJob;