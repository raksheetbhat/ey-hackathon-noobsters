package com.project.ey_hackathon.demo.controller;

import com.project.ey_hackathon.demo.model.JobInsights;
import com.project.ey_hackathon.demo.service.JobInsightsService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/job/insights")
@RequiredArgsConstructor
public class JobInsightsController {

    private final JobInsightsService jobInsightsService;

    @PostMapping
    public JobInsights addJobInsights(@RequestBody JobInsights jobInsights) {
        return jobInsightsService.addJobInsights(jobInsights);
    }

    @GetMapping("/{jobid}")
    public List<JobInsights> getAllByJobId(@PathVariable("jobid") long jobId) {
        return jobInsightsService.findAllByJobId(jobId);
    }

}
