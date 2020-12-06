package com.project.ey_hackathon.demo.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.experimental.SuperBuilder;

import javax.persistence.Entity;
import java.time.LocalDateTime;

@SuperBuilder
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Getter
@Setter
public class Job extends BaseEntity {

    private String jobName;

    private LocalDateTime startDate;

    private LocalDateTime endDate;

    private String goal;

    private String dataSources;

    private String domain;

    private String companyName;

    private String companyUrl;

    private int status; //1 = just created, 2 = airflow processing, 3 = processing done

}
