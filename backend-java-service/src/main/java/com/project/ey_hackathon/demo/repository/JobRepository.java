package com.project.ey_hackathon.demo.repository;

import com.project.ey_hackathon.demo.model.Job;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface JobRepository extends JpaRepository<Job, Long> {

    List<Job> findAll();

    List<Job> findAllByStatusEquals(int status);

}
