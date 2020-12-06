package com.project.ey_hackathon.demo.service.impl;

import com.project.ey_hackathon.demo.model.Job;
import com.project.ey_hackathon.demo.repository.JobRepository;
import com.project.ey_hackathon.demo.service.JobService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class JobServiceImpl implements JobService {

    private final JobRepository jobRepository;

    @Override
    public Job addJob(Job job) {
        return jobRepository.save(job);
    }

    @Override
    public Job updateJob(Long jobId, int status) {
        Job savedJob = jobRepository.findById(jobId).orElseThrow(() -> new RuntimeException("job not found"));

        savedJob.setStatus(status);
        return jobRepository.save(savedJob);
    }

    @Override
    public Job getJobById(Long jobId) {
        return jobRepository.findById(jobId).orElseThrow(() -> new RuntimeException("job not found"));
    }

    @Override
    public List<Job> getAllJobs() {
        return jobRepository.findAll();
    }

    @Override
    public List<Job> getAllByStatus(int status) {
        return jobRepository.findAllByStatusEquals(status);
    }
}
