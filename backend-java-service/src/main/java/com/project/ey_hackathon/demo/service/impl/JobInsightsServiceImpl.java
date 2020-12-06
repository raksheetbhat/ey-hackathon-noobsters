package com.project.ey_hackathon.demo.service.impl;

import com.project.ey_hackathon.demo.model.JobInsights;
import com.project.ey_hackathon.demo.repository.JobInsightsRepository;
import com.project.ey_hackathon.demo.service.JobInsightsService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class JobInsightsServiceImpl implements JobInsightsService {

    private final JobInsightsRepository jobInsightsRepository;

    @Override
    public JobInsights addJobInsights(JobInsights jobInsights) {
        return jobInsightsRepository.save(jobInsights);
    }

    @Override
    public List<JobInsights> findAllByJobId(long jobId) {
        return jobInsightsRepository.findAllByJobId(jobId);
    }
}
