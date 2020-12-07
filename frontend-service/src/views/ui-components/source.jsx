import React, { useEffect, useState } from 'react';
import { PieChart } from 'react-minimal-pie-chart';
import ReactWordcloud from 'react-wordcloud';
import {
    Card,
    CardImg,
    CardImgOverlay,
    CardText,
    CardBody,
    CardTitle,
    CardSubtitle,
    CardColumns,
    CardGroup,
    CardDeck,
    CardLink,
    CardHeader,
    CardFooter,
    Button,
    Row,
    Col, Modal, ModalHeader, ModalBody, ModalFooter,Table
} from 'reactstrap';

import externallink from '../../assets/images/icon/external.svg';

const Source = (props) => {

    const {
        buttonLabel,
        className
    } = props;

    const [modal, setModal] = useState(false);

    const [source, setSource] = useState('');

    const toggle = () => {
        setModal(!modal);
    }

    const options = {
        rotations: 2,
        rotationAngles: [-10, 10],
        fontSizes: [25, 80],
        padding: 5
    };
    
    //const size = [600, 400];

    const getContent = (type) => {
        switch(type){
            case 'twitter': return ['Twitter', '# Tweets'];
            case 'linkedin': return ['Linkedin', '# Linkedin posts'];
            case 'youtube': return ['YouTube', '# YouTube videos'];
            case 'website': return ['Website', '# websites'];
            case 'news': return ['News', '# News articles'];
            case 'aggregated': return ['Aggregated', '# data points in total'];
        }
    }

    const createRow = (arr) => <tr>{arr.map(k => <td>{k}</td>)}</tr>;

    return (
        <div>
            <div style={{display: 'inline-block'}}>
                <h5 style={{float: 'left', marginRight: 10}}>{getContent(props.type)[0]}</h5>
                {props.source != 'aggregated' && <img src={externallink} onClick={toggle} 
                    style={{width: 17, height: 'auto', cursor: 'pointer'}} />}
            </div>
            <Row>
                <Col xs="12" md="4" >
                    <Card style={{marginBottom: "10px"}}>
                        <CardBody style={{textAlign: 'center'}}>
                            <CardTitle>{getContent(props.type)[1]}</CardTitle>
                            <CardText>{props.count}</CardText>
                        </CardBody>
                    </Card>
                    <Card>
                        <CardBody style={{textAlign: 'center'}}>
                            <CardTitle>Sentiments</CardTitle>
                            <PieChart
                                data={[
                                    { title: 'positive', value: props.sentiment.positive, color: '#66bb6a' },
                                    { title: 'negative', value: props.sentiment.negative, color: '#ef5350' },
                                    { title: 'neutral', value: props.sentiment.neutral, color: '#ffee58' },
                                ]}
                                //label={({ dataEntry }) => dataEntry.title}
                                style={{width: "70%"}}
                            />
                        </CardBody>
                    </Card>
                </Col>
                <Col xs="12" md="8">
                    <Card>
                        <CardBody style={{textAlign: 'center'}}>
                            <CardTitle>Keywords</CardTitle>
                            <ReactWordcloud words={props.words} options={options} 
                                style={{paddingBottom: "14px", paddingTop: "12px"}} />
                        </CardBody>
                    </Card>
                </Col>
            </Row>
            <Modal isOpen={modal} toggle={toggle} className={"modal-lg"} style={{maxWidth: '1200px'}}>
                <ModalHeader toggle={toggle}>Data</ModalHeader>
                <ModalBody>
                    <Table>
                        <thead>
                            <tr>
                                <th>#</th>
                                {props.items.length > 0 && Object.keys(props.items[0]).map(v => <th>{v}</th>)}
                            </tr>
                        </thead>
                        <tbody>
                            {props.items.map((v, i) => {
                                let arr = [i+1];

                                Object.keys(v).forEach(function(key) {
                                    let obj = v[key];
                                    if(!Array.isArray(obj) && typeof obj !== 'object'){
                                        if(key === "link"){
                                            arr.push(<a target="_blank" href={obj}>{obj}</a>)
                                        }else{
                                            arr.push(obj);
                                        }
                                    }else{
                                        arr.push("");
                                    }
                                });

                                return createRow(arr);
                            })}
                        </tbody>
                    </Table>
                </ModalBody>
            </Modal>
        </div>
    )
}

export default Source;