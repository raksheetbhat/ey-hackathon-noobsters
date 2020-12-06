import React, { useState } from 'react';
import { Button, Form, FormGroup, Label, Input, FormText } from 'reactstrap';
import { SERVER_URL } from '../../Constants';

const JobForm = (props) => {

    const handleSubmit = (event) => {
      event.preventDefault();

      let formData = {};

      for(let i=0;i<event.target.length;i++) {
        let tg = event.target[i];

        if(tg.name == "dataSources") {
          let ds = Array.from(tg.selectedOptions).map(v => v.value);
          
          formData[tg.name] = ds.join();
        }else{
          if(tg.name == "startDate" || tg.name == "endDate"){
            formData[tg.name] = tg.value + "T00:00:00";
          }else{
            formData[tg.name] = tg.value;
          }
        }
      }

      var myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json");

      var raw = JSON.stringify(formData);

      var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
      };

      fetch(SERVER_URL+"/job", requestOptions)
        .then(response => response.text())
        .then(result => {
          let res = JSON.parse(result);

          let formEle = document.getElementById("job-form");
          formEle.reset();

          alert('Job with id '+res.id+' added successfully');
        })
        .catch(error => console.log('error', error));

      }

    return (
      <Form id="job-form" onSubmit={handleSubmit.bind(this)}>
        <FormGroup>
          <Label for="jobName">Job name</Label>
          <Input type="text" name="jobName" id="jobName" placeholder="test 1"/>
        </FormGroup>
        <FormGroup>
          <Label for="startDate">Start date</Label>
          <Input
            type="date"
            name="startDate"
            id="startDate"
            placeholder="start date"
          />
        </FormGroup>
        <FormGroup>
          <Label for="endDate">End date</Label>
          <Input
            type="date"
            name="endDate"
            id="endDate"
            placeholder="end date"
          />
        </FormGroup>
        <FormGroup>
          <Label for="goal">Choose goal</Label>
          <Input type="select" name="goal" id="goal">
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
          </Input>
        </FormGroup>
        <FormGroup>
          <Label for="dataSources">Choose data sources (can be multiple)</Label>
          <Input type="select" name="dataSources" id="dataSources" multiple>
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
          </Input>
        </FormGroup>
        <FormGroup>
          <Label for="domain">Domain</Label>
          <Input type="text" name="domain" id="domain" placeholder="supply chain"/>
        </FormGroup>
        <FormGroup>
          <Label for="companyName">Company name</Label>
          <Input type="text" name="companyName" id="companyName" placeholder="KPMG"/>
        </FormGroup>
        <FormGroup>
          <Label for="companyUrl">Company url</Label>
          <Input
            type="url"
            name="companyUrl"
            id="companyUrl"
            placeholder="http://kpmg.com"
          />
        </FormGroup>
        <FormGroup>
          <Label for="status">Status</Label>
          <Input type="select" name="status" id="status">
            <option>1</option>
            <option>0</option>
          </Input>
        </FormGroup>
        <Button>Submit</Button>
      </Form>
    );
  }
  
  export default JobForm;