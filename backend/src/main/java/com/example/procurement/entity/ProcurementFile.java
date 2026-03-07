package com.example.procurement.entity;

import com.fasterxml.jackson.annotation.JsonFormat;
import lombok.Data;
import java.time.LocalDateTime;

@Data
public class ProcurementFile {
    private Long fileId;
    private Long procurementRequestId;
    private String fileName;
    private Long fileSize;
    private String filePath;
    private String fileType;
    
    @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss", timezone = "GMT+8")
    private LocalDateTime uploadTime;
}
