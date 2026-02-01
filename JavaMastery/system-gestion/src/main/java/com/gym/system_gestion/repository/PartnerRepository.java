package com.gym.system_gestion.repository;

import com.gym.system_gestion.model.Partner;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PartnerRepository extends JpaRepository<Partner, Long>{
    Page<Partner> findByNombreContainingIgnoreCase(String palabraClave, Pageable pageable);
}
