import React, { useEffect, useState } from 'react';
import { Card, CardBody } from 'reactstrap';
import { SERVER_URL } from '../../Constants';
import Source from './source';
import { useLocation } from 'react-router-dom';
import { useHistory } from 'react-router-dom';

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

    const location = useLocation();
    const history = useHistory();
    
    const [rows, setRows] = useState([]);

    const convertFn = (dict) => {
        let li = [];
        Object.keys(dict).forEach(function(key) {
            li.push({'text': key, 'value': dict[key]});
        });
        return li;
    }

    const isInt = (value) => {
        return !isNaN(value) && 
               parseInt(Number(value)) == value && 
               !isNaN(parseInt(value, 10));
      }

    useEffect(() => {
        let locArr = location.pathname.split('/'), jobId = locArr[locArr.length-1];

        if(!isInt(jobId)){
            jobId = 1;
            history.push('/ui-components/view-job/1');
        }

        var requestOptions = {
            method: 'GET',
            redirect: 'follow'
        };

        fetch(SERVER_URL+"/job/insights/"+jobId, requestOptions)
        .then(response => response.json())
        .then(result => {
            let eleList = [];

            result.map(v => {
                let json = JSON.parse(v.jsonText);

                let wordsLi = convertFn(json.keywords);

                let ele = <Source key={json.source} sentiment={json.sentiment} words={wordsLi} type={json.source} 
                    count={json.count} items={json.items} />;

                if(json.source == 'aggregated'){
                    eleList.unshift(ele);
                }else{
                    eleList.push(ele);
                }
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