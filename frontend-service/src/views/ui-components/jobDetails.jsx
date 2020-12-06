import React from 'react';
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
    Col
} from 'reactstrap';

const JobDetails = (props) => {

    return (
        <div>
            <Card>
            <CardBody>
                <div className="d-flex align-items-center">
                    <div>
                        <CardTitle>Job details</CardTitle>
                    </div>
                </div>
                <Table>
                    <thead>
                        <tr>
                            {Object.keys(props.data[0]).map(v => <th>{v}</th>)}
                        </tr>
                    </thead>
                </Table>
            </CardBody>
            </Card>
        </div>
    )
}

export default JobDetails;