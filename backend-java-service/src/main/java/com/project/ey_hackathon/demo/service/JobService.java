package com.project.ey_hackathon.demo.service;

import com.project.ey_hackathon.demo.model.Job;

import java.util.List;

public interface JobService {

    Job addJob(Job job);

    Job updateJob(Long jobId, int status);

    Job getJobById(Long jobId);

    List<Job> getAllJobs();

    List<Job> getAllByStatus(int status);
}
