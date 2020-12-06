package com.project.ey_hackathon.demo.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.experimental.SuperBuilder;

import javax.persistence.Entity;

@SuperBuilder
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Getter
@Setter
public class JobInsights extends BaseEntity {

    private long jobId;

    private String source;

    private String jsonText;

}
