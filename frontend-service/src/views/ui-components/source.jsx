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
            case 'Twitter': return ['Twitter', '# Tweets'];
            case 'Linkedin': return ['Linkedin', '# Linkedin posts'];
            case 'youtube': return ['YouTube', '# YouTube videos'];
            case 'website': return ['Website', '# websites'];
            case 'news': return ['News', '# News articles'];
        }
    }

    const createRow = (arr) => <tr>{arr.map(k => <td>{k}</td>)}</tr>;

    return (
        <div>
            <Row className="mb-3">
                <Col xs="12" md="1">
                    <h5 >{getContent(props.type)[0]}</h5>
                </Col>
                <Col xs="12" md="2">
                    {props.source != 'aggregated' && <Button color="danger" onClick={toggle}>view data</Button>}
                </Col>
            </Row>
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
                                    { title: 'positive', value: props.sentiment.positive, color: '#43a047' },
                                    { title: 'negative', value: props.sentiment.negative, color: '#f4511e' },
                                    { title: 'neutral', value: props.sentiment.neutral, color: '#fdd835' },
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
                                {Object.keys(props.items[0]).map(v => <th>{v}</th>)}
                            </tr>
                        </thead>
                        <tbody>
                            {props.items.map((v, i) => {
                                //console.log('index', i);
                                // let key = Object.keys(props.items[0])[i];

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

                                // if(typeof key !== 'undefined' && key in v && !Array.isArray(v[key]) 
                                //     && typeof v[key] !== 'object'){
                                //     //console.log(key, v[key]);

                                //     return <td>{v[key]}</td>;
                                // }
                            })}
                        </tbody>
                    </Table>
                </ModalBody>
            </Modal>
        </div>
    )
}

export default Source;