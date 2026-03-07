package com.example.procurement.mapper;

import com.example.procurement.entity.ProcurementFile;
import org.apache.ibatis.annotations.*;
import java.util.List;

@Mapper
public interface FileMapper {
    
    @Insert("INSERT INTO procurement_file (procurement_request_id, file_name, file_size, file_path, upload_time) " +
            "VALUES (#{procurementRequestId}, #{fileName}, #{fileSize}, #{filePath}, #{uploadTime})")
    int insert(ProcurementFile file);
    
    @Select("SELECT * FROM procurement_file WHERE procurement_request_id = #{procurementRequestId}")
    List<ProcurementFile> findByProcurementRequestId(Long procurementRequestId);
    
    @Select("SELECT * FROM procurement_file WHERE file_id = #{fileId}")
    ProcurementFile findById(Long fileId);
    
    @Delete("DELETE FROM procurement_file WHERE file_id = #{fileId}")
    int deleteById(Long fileId);
    
    @Delete("DELETE FROM procurement_file WHERE procurement_request_id = #{procurementRequestId}")
    int deleteByProcurementRequestId(Long procurementRequestId);
}
