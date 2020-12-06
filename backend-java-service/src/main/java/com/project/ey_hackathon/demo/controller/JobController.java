package com.project.ey_hackathon.demo.controller;

import com.project.ey_hackathon.demo.model.Job;
import com.project.ey_hackathon.demo.service.JobService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/job")
@RequiredArgsConstructor
public class JobController {

    private final JobService jobService;

    @PostMapping
    public Job addJob(@RequestBody Job job) {
        return jobService.addJob(job);
    }

    @PutMapping("/{jobid}/status/{status}")
    public Job updateJobStatus(@PathVariable("jobid") long jobId, @PathVariable("status") int status) {
        return jobService.updateJob(jobId, status);
    }

    @GetMapping("/{jobid}")
    public Job getJobById(@PathVariable("jobid") long jobId) {
        return jobService.getJobById(jobId);
    }

    @GetMapping
    public List<Job> getAllJobs() {
        return jobService.getAllJobs();
    }

    @GetMapping("/status/{status}")
    public List<Job> getByStatus(@PathVariable("status") int status) {
        return jobService.getAllByStatus(status);
    }

}
