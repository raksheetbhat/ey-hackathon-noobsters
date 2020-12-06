package com.project.ey_hackathon.demo.repository;

import com.project.ey_hackathon.demo.model.JobInsights;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface JobInsightsRepository extends JpaRepository<JobInsights, Long> {

    List<JobInsights> findAllByJobId(long jobId);
}
