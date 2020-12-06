import React, { useEffect, useState } from "react";

import img1 from '../../../assets/images/users/1.jpg';
import img2 from '../../../assets/images/users/2.jpg';
import img3 from '../../../assets/images/users/3.jpg';
import img4 from '../../../assets/images/users/4.jpg';

import {
    Card,
    CardBody,
    CardTitle,
    CardSubtitle,
    Input,
    Table
} from 'reactstrap';
import { SERVER_URL } from "../../../Constants";

const Projects = () => {

    const [jobs, setJobs] = useState([]);

    useEffect(() => {
        fetchJobs();
    }, []);

    // useEffect((b) => {
    //     console.log('updated', jobs);
    //     setJobs([...jobs]);
    // }, [jobs]);

    const fetchJobs = () => {
        var requestOptions = {
            method: 'GET',
            redirect: 'follow'
          };
          
          fetch(SERVER_URL+"/job", requestOptions)
            .then(response => response.json())
            .then(result => {
                
                let li = []
                result.map(v => {
                    li.push(<JobRow job={v} />);
                });

                setJobs(li);
            })
            .catch(error => console.log('error', error));
    }

    const JobRow = ({job}) => {
        return (
            <tr>
                <td>{job.jobName}</td>
                <td>{job.goal}</td>
                <td><i className="fa fa-circle text-warning" id="tlp1"></i></td>
                <td>{job.dataSources}</td>
                <td className="blue-grey-text  text-darken-4 font-medium">
                    <a href="#">{job.id}</a>
                </td>
            </tr>
        )
    }

    return (
        /*--------------------------------------------------------------------------------*/
        /* Used In Dashboard-4 [General]                                                  */
        /*--------------------------------------------------------------------------------*/

        <Card>
            <CardBody>
                <div className="d-flex align-items-center">
                    <div>
                        <CardTitle>Added jobs</CardTitle>
                        <CardSubtitle>Overview</CardSubtitle>
                    </div>
                    {/* <div className="ml-auto d-flex no-block align-items-center">
                        <div className="dl">
                            <Input type="select" className="custom-select">
                                <option value="0">Monthly</option>
                                <option value="1">Daily</option>
                                <option value="2">Weekly</option>
                                <option value="3">Yearly</option>
                            </Input>
                        </div>
                    </div> */}
                </div>
                
                {jobs && 
                    <Table className="no-wrap v-middle" responsive>
                        <thead>
                            <tr className="border-0">
                                <th className="border-0">Job name</th>
                                <th className="border-0">Goal</th>
                                <th className="border-0">Status</th>
                                <th className="border-0">Data sources</th>
                                <th className="border-0">View job</th>
                            </tr>
                        </thead>
                        <tbody>{jobs.map(v => v)}</tbody>
                    </Table>
                }
                        
                        {/* <tr>
                            <td>
                                <div className="d-flex no-block align-items-center">
                                    <div className="mr-2"><img src={img1} alt="user" className="rounded-circle" width="45" /></div>
                                    <div className="">
                                        <h5 className="mb-0 font-16 font-medium">Hanna Gover</h5><span>hgover@gmail.com</span></div>
                                </div>
                            </td>
                            <td>Elite Admin</td>

                            <td>
                                <i className="fa fa-circle text-warning" id="tlp1"></i>

                            </td>
                            <td>35</td>
                            <td className="blue-grey-text  text-darken-4 font-medium">$96K</td>
                        </tr> */}
                
            </CardBody>
        </Card>
    );
}

export default Projects;
