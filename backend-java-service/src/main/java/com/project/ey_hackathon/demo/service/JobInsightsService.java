package com.project.ey_hackathon.demo.service;

import com.project.ey_hackathon.demo.model.JobInsights;

import java.util.List;

public interface JobInsightsService {

    JobInsights addJobInsights(JobInsights jobInsights);

    List<JobInsights> findAllByJobId(long jobId);

}
